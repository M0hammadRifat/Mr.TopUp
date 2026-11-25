import { query, mutation } from "./_generated/server";
import { v } from "convex/values";

// Helper function to parse bKash, Nagad, Rocket, Upay incoming payment SMS
export function parsePaymentSms(sender, message) {
  if (!message) return null;
  const text = message.trim();
  const lower = text.toLowerCase();
  const senderLower = (sender || "").toLowerCase();

  let gateway = "other";
  if (lower.includes("bkash") || senderLower.includes("16247") || senderLower.includes("bkash")) {
    gateway = "bkash";
  } else if (lower.includes("nagad") || senderLower.includes("16167") || senderLower.includes("nagad") || (lower.includes("txnid") && lower.includes("money received"))) {
    gateway = "nagad";
  } else if (lower.includes("rocket") || senderLower.includes("16216") || senderLower.includes("rocket")) {
    gateway = "rocket";
  } else if (lower.includes("upay") || senderLower.includes("upay")) {
    gateway = "upay";
  } else if (lower.includes("cellfin") || senderLower.includes("cellfin")) {
    gateway = "cellfin";
  }

  // Reject outgoing transactions so syncing all phone SMS never causes false-positive deposits
  const isOutgoing =
    lower.includes("cash out") ||
    lower.includes("you have sent") ||
    lower.includes("sent tk") ||
    lower.includes("send money") ||
    lower.includes("mobile recharge") ||
    lower.includes("recharge of") ||
    lower.includes("paid tk") ||
    lower.includes("payment of") ||
    lower.includes("bill pay") ||
    lower.includes("your otp") ||
    lower.includes("verification code");

  if (isOutgoing && !lower.includes("received")) {
    return null;
  }

  // Extract TrxID: e.g. TrxID 9K8L7M6N5P or TxnID: 71ABCDEF or Trx ID: 9K8L7M6N5P or 76B8FLCZ
  const trxMatch = text.match(/(?:TrxID|TxnID|Trx\s*ID|Txn\s*ID|Transaction\s*ID|TXN|TRX)[:\s#]*([A-Za-z0-9]{4,30})/i);
  const trxId = trxMatch ? trxMatch[1].trim().toUpperCase() : null;

  // Extract Amount: e.g. Tk 500.00, Tk. 500, Amount: Tk 500.00, 500 Tk, 500/-, Amount 500
  let amount = null;
  const amtMatch1 = text.match(/(?:Amount:?\s*(?:Tk\.?|৳)?|received(?:\s+deposit\s+of)?\s*(?:Tk\.?|৳)?|cash\s*in\s*(?:of)?\s*(?:Tk\.?|৳)?|(?:Tk\.?|৳))\s*([0-9,]+(?:\.[0-9]{1,2})?)/i);
  const amtMatch2 = text.match(/([0-9,]+(?:\.[0-9]{1,2})?)\s*(?:Tk\.?|৳|BDT|\/-|টাকা)/i);
  const amtMatch3 = text.match(/(?:Amount|টাকা)[:\s]*([0-9,]+(?:\.[0-9]{1,2})?)/i);

  if (amtMatch1) {
    amount = parseFloat(amtMatch1[1].replace(/,/g, ""));
  } else if (amtMatch2) {
    amount = parseFloat(amtMatch2[1].replace(/,/g, ""));
  } else if (amtMatch3) {
    amount = parseFloat(amtMatch3[1].replace(/,/g, ""));
  }

  // Extract Sender phone number: e.g. from 01712345678 or Sender: 01812345678
  const phoneMatch = text.match(/(?:from|Sender:?)\s*(\+?8801[0-9]{9}|01[0-9]{9})/i);
  const senderNumber = phoneMatch ? phoneMatch[1].replace(/^\+?88/, "") : "";

  if (!trxId || !amount || isNaN(amount) || amount <= 0) {
    return null;
  }

  return { gateway, trxId, amount, senderNumber, rawMessage: text };
}

// Shared helper to process a single SMS, log raw record if requested, and auto-match deposits/orders
async function processSingleSms(ctx, args) {
  const parsed = parsePaymentSms(args.sender, args.message);
  const nowStr = new Date().toISOString();

  if (args.log_raw || !parsed) {
    const existingRaw = await ctx.db
      .query("raw_sms_logs")
      .order("desc")
      .take(40);
    const isDupRaw = existingRaw.some(
      (r) => r.sender === args.sender && r.message === args.message
    );
    if (!isDupRaw) {
      await ctx.db.insert("raw_sms_logs", {
        sender: args.sender || "unknown",
        message: args.message,
        gateway: parsed ? parsed.gateway : "general",
        is_payment: Boolean(parsed),
        trx_id: parsed ? parsed.trxId : undefined,
        amount: parsed ? parsed.amount : undefined,
        sim_slot: args.sim_slot,
        device_id: args.device_id,
        received_at: args.received_at,
        created_at: nowStr,
      });
    }
  }

  if (!parsed) {
    return {
      success: true,
      ignored: true,
      auto_matched: false,
      reason: "Non-payment or outgoing SMS logged safely",
    };
  }

  // Check if SMS with this TrxID already recorded
  const existingSms = await ctx.db
    .query("sms_payments")
    .withIndex("by_trx_id", (q) => q.eq("trx_id", parsed.trxId))
    .first();

  if (existingSms) {
    return {
      success: true,
      duplicate: true,
      auto_matched: existingSms.status === "claimed",
      message: "Duplicate SMS ignored",
      trx_id: parsed.trxId,
      amount: existingSms.amount,
      gateway: existingSms.gateway,
    };
  }

  // 1. Check if there is a pending deposit waiting for this TrxID & Amount
  const allPendingDeposits = await ctx.db
    .query("wallet_transactions")
    .filter((q) => q.eq(q.field("status"), "pending"))
    .collect();

  const matchedDeposit = allPendingDeposits.find(
    (d) => d.trx_id && d.trx_id.trim().toUpperCase() === parsed.trxId && Math.abs(d.amount - parsed.amount) <= 1
  );

  if (matchedDeposit) {
    await ctx.db.patch(matchedDeposit._id, { status: "completed" });

    let user = await ctx.db
      .query("users")
      .withIndex("by_phone", (q) => q.eq("phone", matchedDeposit.user_phone))
      .first();

    let newBal = matchedDeposit.amount;
    if (user) {
      newBal = (user.balance || 0) + matchedDeposit.amount;
      await ctx.db.patch(user._id, { balance: newBal });
    } else {
      await ctx.db.insert("users", {
        name: `User ${matchedDeposit.user_phone.slice(-4)}`,
        phone: matchedDeposit.user_phone,
        balance: matchedDeposit.amount,
        created_at: nowStr,
      });
    }

    await ctx.db.insert("sms_payments", {
      gateway: parsed.gateway,
      trx_id: parsed.trxId,
      amount: parsed.amount,
      sender_number: parsed.senderNumber,
      raw_message: parsed.rawMessage,
      status: "claimed",
      matched_type: "deposit",
      matched_id: matchedDeposit._id,
      matched_phone: matchedDeposit.user_phone,
      created_at: nowStr,
      claimed_at: nowStr,
    });

    return {
      success: true,
      auto_matched: true,
      type: "deposit",
      trx_id: parsed.trxId,
      amount: parsed.amount,
      gateway: parsed.gateway,
      user_phone: matchedDeposit.user_phone,
      new_balance: newBal,
    };
  }

  // 2. Check if there is a pending order waiting for this TrxID & Amount
  const allPendingOrders = await ctx.db
    .query("orders")
    .filter((q) => q.eq(q.field("status"), "pending"))
    .collect();

  const matchedOrder = allPendingOrders.find(
    (o) => o.trx_id && o.trx_id.trim().toUpperCase() === parsed.trxId && Math.abs(o.amount - parsed.amount) <= 1
  );

  if (matchedOrder) {
    await ctx.db.patch(matchedOrder._id, { status: "processing" });

    await ctx.db.insert("sms_payments", {
      gateway: parsed.gateway,
      trx_id: parsed.trxId,
      amount: parsed.amount,
      sender_number: parsed.senderNumber,
      raw_message: parsed.rawMessage,
      status: "claimed",
      matched_type: "order",
      matched_id: matchedOrder._id,
      matched_phone: matchedOrder.user_phone || "",
      created_at: nowStr,
      claimed_at: nowStr,
    });

    return {
      success: true,
      auto_matched: true,
      type: "order",
      trx_id: parsed.trxId,
      amount: parsed.amount,
      gateway: parsed.gateway,
      order_id: matchedOrder.order_id,
    };
  }

  // 3. Not matched yet (SMS arrived before user submitted form) -> Save as unclaimed!
  const smsId = await ctx.db.insert("sms_payments", {
    gateway: parsed.gateway,
    trx_id: parsed.trxId,
    amount: parsed.amount,
    sender_number: parsed.senderNumber,
    raw_message: parsed.rawMessage,
    status: "unclaimed",
    created_at: nowStr,
  });

  return {
    success: true,
    auto_matched: false,
    sms_id: smsId,
    trx_id: parsed.trxId,
    amount: parsed.amount,
    gateway: parsed.gateway,
  };
}

// Mutation: Save SMS from Webhook & Auto-match with Pending Deposits/Orders
export const saveSms = mutation({
  args: {
    sender: v.string(),
    message: v.string(),
    secret: v.optional(v.string()),
    sim_slot: v.optional(v.string()),
    device_id: v.optional(v.string()),
    received_at: v.optional(v.string()),
    log_raw: v.optional(v.boolean()),
  },
  handler: async (ctx, args) => {
    return await processSingleSms(ctx, args);
  },
});

// Mutation: Batch Sync SMS from Android Inbox (old + new SMS)
export const saveSmsBatch = mutation({
  args: {
    messages: v.array(
      v.object({
        sender: v.string(),
        message: v.string(),
        sim_slot: v.optional(v.string()),
        device_id: v.optional(v.string()),
        received_at: v.optional(v.string()),
        log_raw: v.optional(v.boolean()),
      })
    ),
    secret: v.optional(v.string()),
  },
  handler: async (ctx, args) => {
    const results = [];
    let matchedCount = 0;
    let savedPaymentCount = 0;
    for (const item of args.messages) {
      const res = await processSingleSms(ctx, item);
      if (res.auto_matched) matchedCount++;
      if (!res.ignored && !res.duplicate) savedPaymentCount++;
      results.push(res);
    }
    return {
      success: true,
      processed: args.messages.length,
      matched: matchedCount,
      new_payments: savedPaymentCount,
      results,
    };
  },
});

// Mutation: Verify and Claim Deposit from Website (Strict SMS Verification)
export const verifyAndClaimDeposit = mutation({
  args: {
    phone: v.string(),
    amount: v.number(),
    payment_method: v.string(),
    sender_number: v.string(),
    trx_id: v.string(),
  },
  handler: async (ctx, args) => {
    const cleanTrx = args.trx_id.trim().toUpperCase();
    const nowStr = new Date().toISOString();

    if (!cleanTrx || cleanTrx.length < 4) {
      return { success: false, error: "সঠিক ট্রানজেকশন আইডি (TrxID) লিখুন!" };
    }
    if (!args.amount || args.amount < 10) {
      return { success: false, error: "কমপক্ষে ১০ ৳ ডিপোজিট করতে হবে!" };
    }

    // 1. Anti-Fraud Check: Check if TrxID was already claimed or used
    const existingClaimed = await ctx.db
      .query("sms_payments")
      .withIndex("by_trx_id", (q) => q.eq("trx_id", cleanTrx))
      .first();

    if (existingClaimed && existingClaimed.status === "claimed") {
      return {
        success: false,
        error: `এই TrxID (${cleanTrx}) ইতিপূর্বে ব্যবহার করা হয়েছে! নতুন ট্রানজেকশন আইডি দিন।`,
      };
    }

    const existingTx = await ctx.db
      .query("wallet_transactions")
      .filter((q) => q.eq(q.field("trx_id"), cleanTrx))
      .first();

    if (existingTx && existingTx.status === "completed") {
      return {
        success: false,
        error: `এই TrxID (${cleanTrx}) ইতিপূর্বে সম্পন্ন হয়েছে!`,
      };
    }

    if (existingTx && existingTx.status === "pending") {
      return {
        success: true,
        autoApproved: false,
        pending: true,
        transaction_id: existingTx._id,
        message: `এই TrxID (${cleanTrx}) ইতিমধ্যে পেন্ডিং রয়েছে। এসএমএস যাচাই হওয়া পর্যন্ত অপেক্ষা করুন।`,
      };
    }

    // 2. CHECK IF MATCHING SMS EXISTS IN DATABASE!
    // A matching SMS MUST exist in sms_payments with status 'unclaimed' and matching amount!
    const smsRecord = existingClaimed && existingClaimed.status === "unclaimed" ? existingClaimed : null;

    if (smsRecord) {
      // Amount verification: Must match SMS amount
      if (Math.abs(smsRecord.amount - args.amount) > 1) {
        return {
          success: false,
          error: `এসএমএস অনুযায়ী প্রাপ্ত টাকা (৳${smsRecord.amount}) এবং আপনার উল্লেখিত টাকা (৳${args.amount}) মিলছে না!`,
        };
      }

      // SMS verified! Mark SMS as claimed
      await ctx.db.patch(smsRecord._id, {
        status: "claimed",
        matched_type: "deposit",
        matched_phone: args.phone,
        claimed_at: nowStr,
      });

      // Complete transaction immediately (Verified)
      const txId = await ctx.db.insert("wallet_transactions", {
        user_phone: args.phone,
        amount: smsRecord.amount,
        payment_method: args.payment_method,
        sender_number: smsRecord.sender_number || args.sender_number,
        trx_id: cleanTrx,
        status: "completed",
        created_at: nowStr,
      });

      // Credit user's wallet
      let user = await ctx.db
        .query("users")
        .withIndex("by_phone", (q) => q.eq("phone", args.phone))
        .first();

      let newBalance = smsRecord.amount;
      if (user) {
        newBalance = (user.balance || 0) + smsRecord.amount;
        await ctx.db.patch(user._id, { balance: newBalance });
      } else {
        await ctx.db.insert("users", {
          name: `User ${args.phone.slice(-4)}`,
          phone: args.phone,
          balance: smsRecord.amount,
          created_at: nowStr,
        });
      }

      return {
        success: true,
        autoApproved: true,
        transaction_id: txId,
        newBalance: newBalance,
        message: `⚡ বিকাশ/নগদ পেমেন্ট সফলভাবে যাচাই হয়েছে! ওয়ালেটে ৳${smsRecord.amount} যোগ করা হয়েছে।`,
      };
    } else {
      // NO MATCHING SMS FOUND YET!
      // DO NOT CREDIT ANY MONEY TO WALLET! (Zero balance added, anti-fraud)
      // Save transaction as PENDING so when SMS arrives via webhook, saveSms will automatically verify and credit!
      const txId = await ctx.db.insert("wallet_transactions", {
        user_phone: args.phone,
        amount: args.amount,
        payment_method: args.payment_method,
        sender_number: args.sender_number,
        trx_id: cleanTrx,
        status: "pending",
        created_at: nowStr,
      });

      return {
        success: true,
        autoApproved: false,
        pending: true,
        transaction_id: txId,
        message: `আপনার পেমেন্ট তথ্য জমা হয়েছে। এসএমএস যাচাই হওয়া মাত্রই ওয়ালেটে ব্যালেন্স যুক্ত হবে!`,
      };
    }
  },
});

// Mutation: Verify and Claim Direct Order Checkout
export const verifyAndClaimOrder = mutation({
  args: {
    order_id: v.string(),
    product_id: v.number(),
    product_name: v.string(),
    package_name: v.string(),
    amount: v.number(),
    player_uid: v.string(),
    payment_method: v.string(),
    sender_number: v.optional(v.string()),
    trx_id: v.optional(v.string()),
    user_phone: v.optional(v.string()),
  },
  handler: async (ctx, args) => {
    const nowStr = new Date().toISOString();
    const cleanTrx = args.trx_id ? args.trx_id.trim().toUpperCase() : "";

    let orderStatus = "pending";
    let isAutoApproved = false;

    if (args.payment_method === "wallet") {
      // Wallet payment: check balance
      if (args.user_phone) {
        let user = await ctx.db
          .query("users")
          .withIndex("by_phone", (q) => q.eq("phone", args.user_phone))
          .first();

        if (user && (user.balance || 0) >= args.amount) {
          await ctx.db.patch(user._id, { balance: (user.balance || 0) - args.amount });
          orderStatus = "completed";
          isAutoApproved = true;
        } else {
          return { success: false, error: "আপনার ওয়ালেটে পর্যাপ্ত ব্যালেন্স নেই! আগে ডিপোজিট করুন।" };
        }
      }
    } else if (cleanTrx) {
      // bKash or Nagad TrxID
      const existingClaimed = await ctx.db
        .query("sms_payments")
        .withIndex("by_trx_id", (q) => q.eq("trx_id", cleanTrx))
        .first();

      if (existingClaimed && existingClaimed.status === "claimed") {
        return { success: false, error: "এই TrxID ইতিপূর্বে ব্যবহার করা হয়েছে!" };
      }

      if (existingClaimed && existingClaimed.status === "unclaimed") {
        if (Math.abs(existingClaimed.amount - args.amount) > 1) {
          return { success: false, error: `এসএমএস-এর টাকার পরিমাণ (৳${existingClaimed.amount}) এবং অর্ডারের টাকার পরিমাণ (৳${args.amount}) মিলছে না!` };
        }
        await ctx.db.patch(existingClaimed._id, {
          status: "claimed",
          matched_type: "order",
          matched_phone: args.user_phone || "",
          claimed_at: nowStr,
        });
        orderStatus = "processing";
        isAutoApproved = true;
      } else {
        // No SMS received yet -> order remains pending until SMS arrives
        orderStatus = "pending";
        isAutoApproved = false;
      }
    }

    const orderData = {
      order_id: args.order_id,
      product_id: args.product_id,
      product_name: args.product_name,
      package_name: args.package_name,
      amount: args.amount,
      player_uid: args.player_uid,
      payment_method: args.payment_method,
      sender_number: args.sender_number,
      trx_id: cleanTrx || undefined,
      status: orderStatus,
      user_phone: args.user_phone,
      created_at: nowStr,
    };

    const id = await ctx.db.insert("orders", orderData);

    // Insert to live_orders
    await ctx.db.insert("live_orders", {
      full_name: args.sender_number ? `User (${args.sender_number.slice(-4)})` : "BD Player",
      avatar: "https://lh3.googleusercontent.com/a/ACg8ocLDlfC4vHjXm1TtshnotB4DGPMl1fHvHqpJpHCykwaT-f-nbWQ=s96-c",
      name: `${args.package_name}`,
      amount: args.amount,
      status: orderStatus,
      created_at: nowStr,
    });

    return {
      success: true,
      autoApproved: isAutoApproved,
      id,
      order_id: args.order_id,
      status: orderStatus,
    };
  },
});

// Query: List all SMS logs (Admin)
export const listSms = query({
  args: {},
  handler: async (ctx) => {
    return await ctx.db.query("sms_payments").order("desc").take(50);
  },
});

// Mutation: Delete an SMS record (Admin)
export const deleteSms = mutation({
  args: { id: v.id("sms_payments") },
  handler: async (ctx, args) => {
    await ctx.db.delete(args.id);
    return { success: true };
  },
});
