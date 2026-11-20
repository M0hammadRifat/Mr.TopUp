import { query, mutation } from "./_generated/server";
import { v } from "convex/values";

// Query packages for a product
export const listByProduct = query({
  args: { product_id: v.number() },
  handler: async (ctx, args) => {
    return await ctx.db
      .query("packages")
      .withIndex("by_product", (q) => q.eq("product_id", args.product_id))
      .collect();
  },
});

// Query all packages (Admin)
export const listAll = query({
  args: {},
  handler: async (ctx) => {
    return await ctx.db.query("packages").collect();
  },
});

// Mutation: Add new package (Admin)
export const add = mutation({
  args: {
    product_id: v.number(),
    name: v.string(),
    price: v.number(),
    tag: v.optional(v.string()),
    in_stock: v.optional(v.number()),
  },
  handler: async (ctx, args) => {
    const id = Date.now();
    const docId = await ctx.db.insert("packages", {
      id: id,
      product_id: args.product_id,
      name: args.name,
      price: args.price,
      tag: args.tag || "",
      in_stock: args.in_stock ?? 1,
    });
    return { success: true, id: docId };
  },
});

// Mutation: Update existing package (Admin)
export const update = mutation({
  args: {
    id: v.id("packages"),
    name: v.optional(v.string()),
    price: v.optional(v.number()),
    tag: v.optional(v.string()),
    in_stock: v.optional(v.number()),
  },
  handler: async (ctx, args) => {
    const patchData = {};
    if (args.name !== undefined) patchData.name = args.name;
    if (args.price !== undefined) patchData.price = args.price;
    if (args.tag !== undefined) patchData.tag = args.tag;
    if (args.in_stock !== undefined) patchData.in_stock = args.in_stock;

    await ctx.db.patch(args.id, patchData);
    return { success: true };
  },
});

// Mutation: Delete package (Admin)
export const remove = mutation({
  args: {
    id: v.id("packages"),
  },
  handler: async (ctx, args) => {
    await ctx.db.delete(args.id);
    return { success: true };
  },
});

// Mutation: seed packages
export const seedPackages = mutation({
  args: {
    items: v.array(
      v.object({
        id: v.number(),
        product_id: v.number(),
        name: v.string(),
        price: v.number(),
        tag: v.optional(v.string()),
        in_stock: v.optional(v.number()),
      })
    ),
  },
  handler: async (ctx, args) => {
    let count = 0;
    for (const item of args.items) {
      await ctx.db.insert("packages", item);
      count++;
    }
    return { inserted: count };
  },
});

// Mutation: Update stock status alias
export const updateStock = mutation({
  args: {
    id: v.id("packages"),
    in_stock: v.number(),
  },
  handler: async (ctx, args) => {
    await ctx.db.patch(args.id, { in_stock: args.in_stock });
    return { success: true };
  },
});
