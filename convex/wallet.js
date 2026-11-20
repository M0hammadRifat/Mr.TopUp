import { query, mutation } from "./_generated/server";
import { v } from "convex/values";

// Mutation: Add money to wallet
export const addMoney = mutation({
  args: {
    phone: v.string(),
    amount: v.number(),
    payment_method: v.string(),
    sender_number: v.string(),
    trx_id: v.string(),
  },
  handler: async (ctx, args) => {
    const nowStr = new Date().toISOString();

    // Insert wallet transaction record
    const trxId = await ctx.db.insert("wallet_transactions", {
      user_phone: args.phone,
      amount: args.amount,
      payment_method: args.payment_method,
      sender_number: args.sender_number,
      trx_id: args.trx_id,
      status: "completed",
      created_at: nowStr,
    });

    // Update user balance
    let user = await ctx.db
      .query("users")
      .withIndex("by_phone", (q) => q.eq("phone", args.phone))
      .first();

    let newBalance = args.amount;
    if (user) {
      newBalance = (user.balance || 0) + args.amount;
      await ctx.db.patch(user._id, { balance: newBalance });
    } else {
      await ctx.db.insert("users", {
        name: `User ${args.phone.slice(-4)}`,
        phone: args.phone,
        balance: args.amount,
        created_at: nowStr,
      });
    }

    return {
      success: true,
      transaction_id: trxId,
      newBalance: newBalance,
    };
  },
});

// Query: Get balance for a user
export const getBalance = query({
  args: { phone: v.string() },
  handler: async (ctx, args) => {
    const user = await ctx.db
      .query("users")
      .withIndex("by_phone", (q) => q.eq("phone", args.phone))
      .first();

    return user ? user.balance : 0;
  },
});

// Query: List all wallet transactions (Admin)
export const listAll = query({
  args: {},
  handler: async (ctx) => {
    return await ctx.db.query("wallet_transactions").order("desc").collect();
  },
});

// Query: List wallet transactions for a specific user
export const listByUser = query({
  args: { phone: v.string() },
  handler: async (ctx, args) => {
    if (!args.phone) return [];
    return await ctx.db
      .query("wallet_transactions")
      .withIndex("by_phone", (q) => q.eq("user_phone", args.phone.trim()))
      .order("desc")
      .take(50);
  },
});

// Mutation: Update transaction status (Admin)
export const updateStatus = mutation({
  args: {
    id: v.id("wallet_transactions"),
    status: v.string(),
  },
  handler: async (ctx, args) => {
    await ctx.db.patch(args.id, { status: args.status });
    return { success: true };
  },
});

// Mutation: Approve Deposit & Automatically Credit User Wallet (Admin)
export const approveDeposit = mutation({
  args: {
    id: v.id("wallet_transactions"),
  },
  handler: async (ctx, args) => {
    const tx = await ctx.db.get(args.id);
    if (!tx) return { success: false, message: "Transaction not found" };
    if (tx.status === "completed") return { success: false, message: "Already approved and credited!" };

    await ctx.db.patch(args.id, { status: "completed" });

    // Credit user wallet
    let user = await ctx.db
      .query("users")
      .withIndex("by_phone", (q) => q.eq("phone", tx.user_phone))
      .first();

    let newBal = tx.amount;
    if (user) {
      newBal = (user.balance || 0) + tx.amount;
      await ctx.db.patch(user._id, { balance: newBal });
    } else {
      const nowStr = new Date().toISOString();
      await ctx.db.insert("users", {
        name: `User ${tx.user_phone.slice(-4)}`,
        phone: tx.user_phone,
        balance: tx.amount,
        created_at: nowStr,
      });
    }

    return { success: true, newBalance: newBal };
  },
});

// Mutation: Delete transaction (Admin)
export const deleteTransaction = mutation({
  args: {
    id: v.id("wallet_transactions"),
  },
  handler: async (ctx, args) => {
    await ctx.db.delete(args.id);
    return { success: true };
  },
});
