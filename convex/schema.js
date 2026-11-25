import { defineSchema, defineTable } from "convex/server";
import { v } from "convex/values";

export default defineSchema({
  products: defineTable({
    id: v.number(),
    name: v.string(),
    logo: v.string(),
    category_id: v.number(),
    sort_order: v.number(),
    topup_type: v.string(),
    brand: v.optional(v.any()),
  }).index("by_category", ["category_id"]).index("by_pid", ["id"]),

  packages: defineTable({
    id: v.number(),
    product_id: v.number(),
    name: v.string(),
    price: v.number(),
    tag: v.optional(v.string()),
    in_stock: v.optional(v.number()),
  }).index("by_product", ["product_id"]),

  orders: defineTable({
    order_id: v.string(),
    product_id: v.number(),
    product_name: v.string(),
    package_name: v.string(),
    amount: v.number(),
    player_uid: v.string(),
    payment_method: v.string(),
    sender_number: v.optional(v.string()),
    trx_id: v.optional(v.string()),
    status: v.string(),
    user_phone: v.optional(v.string()),
    player_name: v.optional(v.string()),
    likes_count: v.optional(v.number()),
    initial_likes: v.optional(v.number()),
    delivery_logs: v.optional(v.string()),
    created_at: v.string(),
  }).index("by_order_id", ["order_id"]).index("by_player", ["player_uid"]),

  wallet_transactions: defineTable({
    user_phone: v.string(),
    amount: v.number(),
    payment_method: v.string(),
    sender_number: v.string(),
    trx_id: v.string(),
    status: v.string(),
    created_at: v.string(),
  }).index("by_phone", ["user_phone"]),

  users: defineTable({
    name: v.string(),
    phone: v.string(),
    password: v.optional(v.string()),
    password_hash: v.optional(v.string()),
    password_salt: v.optional(v.string()),
    email: v.optional(v.string()),
    role: v.optional(v.string()),
    balance: v.number(),
    created_at: v.string(),
  }).index("by_phone", ["phone"]).index("by_email", ["email"]),

  sessions: defineTable({
    userId: v.id("users"),
    token: v.string(),
    expiresAt: v.number(),
    created_at: v.string(),
  }).index("by_token", ["token"]).index("by_user", ["userId"]),

  live_orders: defineTable({
    full_name: v.string(),
    avatar: v.string(),
    name: v.string(),
    amount: v.number(),
    status: v.string(),
    created_at: v.string(),
  }),

  sms_payments: defineTable({
    gateway: v.string(), // "bkash" | "nagad" | "rocket" | "upay" | "other"
    trx_id: v.string(),
    amount: v.number(),
    sender_number: v.string(),
    raw_message: v.string(),
    status: v.string(), // "unclaimed" | "claimed"
    matched_type: v.optional(v.string()), // "deposit" | "order" | "manual"
    matched_id: v.optional(v.string()),
    matched_phone: v.optional(v.string()),
    created_at: v.string(),
    claimed_at: v.optional(v.string()),
  }).index("by_trx_id", ["trx_id"]).index("by_status", ["status"]),

  raw_sms_logs: defineTable({
    sender: v.string(),
    message: v.string(),
    gateway: v.string(),
    is_payment: v.boolean(),
    trx_id: v.optional(v.string()),
    amount: v.optional(v.number()),
    sim_slot: v.optional(v.string()),
    device_id: v.optional(v.string()),
    received_at: v.optional(v.string()),
    created_at: v.string(),
  }).index("by_created_at", ["created_at"]),
});

