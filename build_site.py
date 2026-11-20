import json
import os

with open('/storage/emulated/0/Codex/rrrtopup_data.json') as f:
    site_data = json.load(f)

with open('/storage/emulated/0/Codex/product_21_data.json') as f:
    prod_21_data = json.load(f)

products = site_data['props']['pageProps']['topup_products']
banners = site_data['props']['pageProps']['banners']
orders = site_data['props']['pageProps']['publicOrders']['orders']
settings = site_data['props']['pageProps']['siteSettings']
packages_21 = prod_21_data['productData']['packages']

print(f"Loaded {len(products)} products, {len(banners)} banners, {len(orders)} orders, {len(packages_21)} packages.")
