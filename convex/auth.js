import { query, mutation } from "./_generated/server";
import { v } from "convex/values";

// Helper: Secure password hashing using Web Crypto API (SHA-256 with Salt)
async function hashPassword(password, salt) {
  const encoder = new TextEncoder();
  const data = encoder.encode(password + "::" + salt);
  const hashBuffer = await crypto.subtle.digest("SHA-256", data);
  const hashArray = Array.from(new Uint8Array(hashBuffer));
  return hashArray.map((b) => b.toString(16).padStart(2, "0")).join("");
}

function generateRandomHex(byteCount = 16) {
  const arr = new Uint8Array(byteCount);
  crypto.getRandomValues(arr);
  return Array.from(arr).map((b) => b.toString(16).padStart(2, "0")).join("");
}

// ============================================================
// CONVEX AUTH: Sign Up (Zero OTP, Instant Password-based)
// ============================================================
export const signUp = mutation({
  args: {
    name: v.string(),
    phone: v.string(),
    password: v.string(),
    email: v.optional(v.string()),
  },
  handler: async (ctx, args) => {
    const cleanPhone = args.phone.trim();
    const cleanName = args.name.trim();
    const cleanEmail = args.email ? args.email.trim() : undefined;

    if (!cleanName) {
      return { success: false, message: "সম্পূর্ণ নাম দেওয়া আবশ্যক!" };
    }
    if (!cleanPhone) {
      return { success: false, message: "মোবাইল নম্বর দেওয়া আবশ্যক!" };
    }
    if (!args.password || args.password.length < 6) {
      return { success: false, message: "পাসওয়ার্ড কমপক্ষে ৬ অক্ষরের হতে হবে!" };
    }

    // Check if phone already exists
    const existingPhone = await ctx.db
      .query("users")
      .withIndex("by_phone", (q) => q.eq("phone", cleanPhone))
      .first();

    if (existingPhone) {
      return { success: false, message: "এই মোবাইল নম্বর দিয়ে ইতিমধ্যে অ্যাকাউন্ট খোলা আছে! অনুগ্রহ করে লগইন করুন।" };
    }

    // Hash password securely with random salt
    const salt = generateRandomHex(16);
    const hash = await hashPassword(args.password, salt);
    const nowStr = new Date().toISOString();

    // Create user in Convex Database
    const userId = await ctx.db.insert("users", {
      name: cleanName,
      phone: cleanPhone,
      email: cleanEmail,
      password_hash: hash,
      password_salt: salt,
      password: args.password, // fallback
      role: "user",
      balance: 0,
      created_at: nowStr,
    });

    // Generate secure session token (30 days validity)
    const token = generateRandomHex(32);
    const expiresAt = Date.now() + 30 * 24 * 60 * 60 * 1000;

    await ctx.db.insert("sessions", {
      userId: userId,
      token: token,
      expiresAt: expiresAt,
      created_at: nowStr,
    });

    return {
      success: true,
      message: "অ্যাকাউন্ট সফলভাবে তৈরি হয়েছে! (কোনো ওটিপি ছাড়াই)",
      token: token,
      user: {
        _id: userId,
        name: cleanName,
        phone: cleanPhone,
        email: cleanEmail || "",
        balance: 0,
        role: "user",
      },
    };
  },
});

// ============================================================
// CONVEX AUTH: Sign In (Zero OTP, Instant Password-based)
// ============================================================
export const signIn = mutation({
  args: {
    identifier: v.string(), // can be phone number or email
    password: v.string(),
  },
  handler: async (ctx, args) => {
    const idStr = args.identifier.trim();
    if (!idStr || !args.password) {
      return { success: false, message: "মোবাইল নম্বর/ইমেইল এবং পাসওয়ার্ড দুইটিই দিন!" };
    }

    // 1. Try search by phone
    let user = await ctx.db
      .query("users")
      .withIndex("by_phone", (q) => q.eq("phone", idStr))
      .first();

    // 2. If not found by phone, try search by email
    if (!user) {
      user = await ctx.db
        .query("users")
        .withIndex("by_email", (q) => q.eq("email", idStr))
        .first();
    }

    if (!user) {
      return { success: false, message: "কোনো অ্যাকাউন্ট পাওয়া যায়নি! অনুগ্রহ করে সাইন-আপ করুন।" };
    }

    // Verify Password
    let passwordMatches = false;
    if (user.password_hash && user.password_salt) {
      const computedHash = await hashPassword(args.password, user.password_salt);
      passwordMatches = computedHash === user.password_hash;
    }
    if (!passwordMatches && user.password) {
      // Direct plaintext password match / update
      passwordMatches = user.password === args.password;
      if (passwordMatches) {
        // Upgrade to salt+hash on login
        const salt = generateRandomHex(16);
        const hash = await hashPassword(args.password, salt);
        await ctx.db.patch(user._id, { password_hash: hash, password_salt: salt });
      }
    }

    if (!passwordMatches) {
      return { success: false, message: "ভুল পাসওয়ার্ড! দয়া করে সঠিক পাসওয়ার্ড দিন।" };
    }

    // Generate session token (30 days validity)
    const token = generateRandomHex(32);
    const expiresAt = Date.now() + 30 * 24 * 60 * 60 * 1000;
    const nowStr = new Date().toISOString();

    await ctx.db.insert("sessions", {
      userId: user._id,
      token: token,
      expiresAt: expiresAt,
      created_at: nowStr,
    });

    return {
      success: true,
      message: "সফলভাবে লগইন হয়েছে! (Zero OTP)",
      token: token,
      user: {
        _id: user._id,
        name: user.name,
        phone: user.phone,
        email: user.email || "",
        balance: user.balance || 0,
        role: user.role || "user",
      },
    };
  },
});

// ============================================================
// CONVEX AUTH: Get Current User (Session Token Verification)
// ============================================================
export const getMe = query({
  args: {
    token: v.string(),
  },
  handler: async (ctx, args) => {
    if (!args.token) return null;

    const session = await ctx.db
      .query("sessions")
      .withIndex("by_token", (q) => q.eq("token", args.token.trim()))
      .first();

    if (!session || session.expiresAt < Date.now()) {
      return null;
    }

    const user = await ctx.db.get(session.userId);
    if (!user) return null;

    return {
      _id: user._id,
      name: user.name,
      phone: user.phone,
      email: user.email || "",
      balance: user.balance || 0,
      role: user.role || "user",
    };
  },
});

// ============================================================
// CONVEX AUTH: Sign Out (Invalidate Session Token)
// ============================================================
export const signOut = mutation({
  args: {
    token: v.string(),
  },
  handler: async (ctx, args) => {
    if (!args.token) return { success: true };

    const session = await ctx.db
      .query("sessions")
      .withIndex("by_token", (q) => q.eq("token", args.token.trim()))
      .first();

    if (session) {
      await ctx.db.delete(session._id);
    }

    return { success: true };
  },
});
