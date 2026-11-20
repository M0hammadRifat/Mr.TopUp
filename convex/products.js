import { query, mutation } from "./_generated/server";
import { v } from "convex/values";

// Query: list all products
export const list = query({
  args: {},
  handler: async (ctx) => {
    return await ctx.db.query("products").collect();
  },
});

// Query: get product by ID
export const getById = query({
  args: { id: v.number() },
  handler: async (ctx, args) => {
    const product = await ctx.db
      .query("products")
      .withIndex("by_pid", (q) => q.eq("id", args.id))
      .first();

    const pkgs = await ctx.db
      .query("packages")
      .withIndex("by_product", (q) => q.eq("product_id", args.id))
      .collect();

    return { product, packages: pkgs };
  },
});

// Mutation: seed products into Convex
export const seedProducts = mutation({
  args: {
    items: v.array(
      v.object({
        id: v.number(),
        name: v.string(),
        logo: v.string(),
        category_id: v.number(),
        sort_order: v.number(),
        topup_type: v.string(),
        brand: v.optional(v.any()),
      })
    ),
  },
  handler: async (ctx, args) => {
    let count = 0;
    for (const item of args.items) {
      const existing = await ctx.db
        .query("products")
        .withIndex("by_pid", (q) => q.eq("id", item.id))
        .first();

      if (!existing) {
        await ctx.db.insert("products", item);
        count++;
      }
    }
    return { inserted: count };
  },
});
