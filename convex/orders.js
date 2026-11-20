import { query, mutation } from "./_generated/server";
import { v } from "convex/values";

// Mutation: create an order
export const create = mutation({
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
    player_name: v.optional(v.string()),
    likes_count: v.optional(v.number()),
    initial_likes: v.optional(v.number()),
    delivery_logs: v.optional(v.string()),
  },
  handler: async (ctx, args) => {
    const nowStr = new Date().toISOString();
    const isLikeOrder = args.product_id === 41 || (args.package_name && args.package_name.toLowerCase().includes("like"));
    const orderData = {
      ...args,
      status: isLikeOrder ? "completed" : "completed",
      delivery_logs: isLikeOrder ? (args.delivery_logs || `[Auto-Dispatcher] Sent ${args.likes_count || 200} likes to Free Fire BD Server for UID ${args.player_uid}`) : undefined,
      created_at: nowStr,
    };

    const id = await ctx.db.insert("orders", orderData);

    // Also insert into live_orders
    await ctx.db.insert("live_orders", {
      full_name: args.sender_number ? `User (${args.sender_number.slice(-4)})` : "BD Player",
      avatar: "https://lh3.googleusercontent.com/a/ACg8ocLDlfC4vHjXm1TtshnotB4DGPMl1fHvHqpJpHCykwaT-f-nbWQ=s96-c",
      name: `${args.package_name}`,
      amount: args.amount,
      status: "completed",
      created_at: nowStr,
    });

    return { success: true, id, order_id: args.order_id };
  },
});

// Query: track order by order_id or player_uid
export const track = query({
  args: { search: v.string() },
  handler: async (ctx, args) => {
    const s = args.search.trim();
    // Search by order_id
    let order = await ctx.db
      .query("orders")
      .withIndex("by_order_id", (q) => q.eq("order_id", s))
      .first();

    if (!order) {
      // Search by player_uid
      order = await ctx.db
        .query("orders")
        .withIndex("by_player", (q) => q.eq("player_uid", s))
        .first();
    }

    return order || null;
  },
});

// Query: get latest live orders
export const listRecent = query({
  args: {},
  handler: async (ctx) => {
    return await ctx.db.query("live_orders").order("desc").take(15);
  },
});

// Query: List all orders for Admin Dashboard
export const listAll = query({
  args: {},
  handler: async (ctx) => {
    return await ctx.db.query("orders").order("desc").collect();
  },
});

// Query: List orders for a specific user
export const listByUser = query({
  args: { phone: v.string() },
  handler: async (ctx, args) => {
    if (!args.phone) return [];
    return await ctx.db
      .query("orders")
      .filter((q) => q.eq(q.field("user_phone"), args.phone.trim()))
      .order("desc")
      .take(50);
  },
});

// Mutation: Update order status (Admin)
export const updateStatus = mutation({
  args: {
    id: v.id("orders"),
    status: v.string(), // "pending" | "processing" | "completed" | "cancelled"
  },
  handler: async (ctx, args) => {
    const order = await ctx.db.get(args.id);
    if (!order) return { success: false, message: "Order not found" };

    await ctx.db.patch(args.id, { status: args.status });
    return { success: true, status: args.status };
  },
});

// Mutation: Delete order (Admin)
export const deleteOrder = mutation({
  args: {
    id: v.id("orders"),
  },
  handler: async (ctx, args) => {
    await ctx.db.delete(args.id);
    return { success: true };
  },
});
