import { query, mutation } from "./_generated/server";
import { v } from "convex/values";

// Mutation: Register a new user
export const register = mutation({
  args: {
    name: v.string(),
    phone: v.string(),
    password: v.string(),
    email: v.optional(v.string()),
  },
  handler: async (ctx, args) => {
    const cleanPhone = args.phone.trim();
    const existing = await ctx.db
      .query("users")
      .withIndex("by_phone", (q) => q.eq("phone", cleanPhone))
      .first();

    if (existing) {
      return { success: false, message: "এই মোবাইল নাম্বার দিয়ে ইতিমধ্যে অ্যাকাউন্ট রয়েছে! অনুগ্রহ করে লগইন করুন।" };
    }

    const nowStr = new Date().toISOString();
    const id = await ctx.db.insert("users", {
      name: args.name.trim(),
      phone: cleanPhone,
      password: args.password,
      email: args.email ? args.email.trim() : undefined,
      role: "user",
      balance: 0,
      created_at: nowStr,
    });

    return {
      success: true,
      user: {
        _id: id,
        name: args.name.trim(),
        phone: cleanPhone,
        balance: 0,
        role: "user",
      },
    };
  },
});

// Mutation: Login with Phone & Password
export const loginWithPassword = mutation({
  args: {
    phone: v.string(),
    password: v.string(),
  },
  handler: async (ctx, args) => {
    const cleanPhone = args.phone.trim();
    const user = await ctx.db
      .query("users")
      .withIndex("by_phone", (q) => q.eq("phone", cleanPhone))
      .first();

    if (!user) {
      return { success: false, message: "কোনো অ্যাকাউন্ট পাওয়া যায়নি! অনুগ্রহ করে সাইন-আপ করুন।" };
    }

    if (user.password && user.password !== args.password) {
      return { success: false, message: "ভুল পাসওয়ার্ড! দয়া করে সঠিক পাসওয়ার্ড দিন।" };
    }

    return {
      success: true,
      user: {
        _id: user._id,
        name: user.name,
        phone: user.phone,
        balance: user.balance,
        role: user.role || "user",
      },
    };
  },
});

// Mutation: Quick phone/name login (backward-compatibility)
export const login = mutation({
  args: {
    name: v.string(),
    phone: v.string(),
  },
  handler: async (ctx, args) => {
    let user = await ctx.db
      .query("users")
      .withIndex("by_phone", (q) => q.eq("phone", args.phone.trim()))
      .first();

    if (!user) {
      const nowStr = new Date().toISOString();
      const id = await ctx.db.insert("users", {
        name: args.name.trim(),
        phone: args.phone.trim(),
        role: "user",
        balance: 0,
        created_at: nowStr,
      });
      user = { _id: id, name: args.name.trim(), phone: args.phone.trim(), balance: 0, role: "user" };
    } else if (args.name && user.name !== args.name) {
      await ctx.db.patch(user._id, { name: args.name });
      user.name = args.name;
    }

    return user;
  },
});

// Query: List all users (Admin Dashboard)
export const listAll = query({
  args: {},
  handler: async (ctx) => {
    return await ctx.db.query("users").order("desc").collect();
  },
});

// Mutation: Update user balance (Admin action)
export const updateBalance = mutation({
  args: {
    id: v.id("users"),
    amount: v.number(),
    type: v.string(), // "add" | "deduct" | "set"
  },
  handler: async (ctx, args) => {
    const user = await ctx.db.get(args.id);
    if (!user) return { success: false, message: "ইউজার পাওয়া যায়নি" };

    let newBal = user.balance;
    if (args.type === "add") newBal += args.amount;
    else if (args.type === "deduct") newBal = Math.max(0, newBal - args.amount);
    else if (args.type === "set") newBal = args.amount;

    await ctx.db.patch(args.id, { balance: newBal });
    return { success: true, newBalance: newBal };
  },
});

// Mutation: Configure Admin user credentials
export const setAdmin = mutation({
  args: {
    email: v.string(),
    password: v.string(),
  },
  handler: async (ctx, args) => {
    const cleanEmail = args.email.trim();
    let user = await ctx.db
      .query("users")
      .withIndex("by_email", (q) => q.eq("email", cleanEmail))
      .first();

    if (!user) {
      user = await ctx.db
        .query("users")
        .withIndex("by_phone", (q) => q.eq("phone", "01700000000"))
        .first();
    }

    if (user) {
      await ctx.db.patch(user._id, {
        email: cleanEmail,
        role: "admin",
        password: args.password,
      });
      return { success: true, updated: user._id };
    } else {
      const nowStr = new Date().toISOString();
      const id = await ctx.db.insert("users", {
        name: "Super Admin (Rifat)",
        phone: "01700000000",
        email: cleanEmail,
        password: args.password,
        role: "admin",
        balance: 10000,
        created_at: nowStr,
      });
      return { success: true, created: id };
    }
  },
});
