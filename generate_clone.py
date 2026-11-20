import json
import os

with open('/storage/emulated/0/Codex/rrrtopup_data.json', encoding='utf-8') as f:
    site_data = json.load(f)

with open('/storage/emulated/0/Codex/product_21_data.json', encoding='utf-8') as f:
    prod_21_data = json.load(f)

products = site_data['props']['pageProps']['topup_products']
banners = site_data['props']['pageProps']['banners']
public_orders = site_data['props']['pageProps']['publicOrders']['orders']
settings = site_data['props']['pageProps']['siteSettings']
packages_21 = prod_21_data['productData']['packages']

# Prepare package dictionary for products
product_packages = {
    21: packages_21,
    49: [
        {"id": 491, "name": "1x Weekly + 1x Monthly", "price": 925, "tag": "Popular", "image": "diamond_package.webp"},
        {"id": 492, "name": "2x Weekly + 2x Monthly", "price": 1850, "tag": "Best Value", "image": "diamond_package.webp"},
        {"id": 493, "name": "3x Weekly + 3x Monthly", "price": 2775, "tag": "", "image": "diamond_package.webp"},
        {"id": 494, "name": "4x Weekly + 1x Monthly", "price": 1390, "tag": "", "image": "diamond_package.webp"},
        {"id": 495, "name": "Weekly Lite Combo", "price": 195, "tag": "", "image": "diamond_package.webp"},
    ],
    26: [
        {"id": 261, "name": "Weekly Lite 1x", "price": 35, "tag": "", "image": "diamond_package.webp"},
        {"id": 262, "name": "Weekly Lite 2x", "price": 70, "tag": "", "image": "diamond_package.webp"},
        {"id": 263, "name": "Weekly Lite 3x", "price": 105, "tag": "", "image": "diamond_package.webp"},
        {"id": 264, "name": "Weekly Lite 5x", "price": 175, "tag": "", "image": "diamond_package.webp"},
    ],
    38: [
        {"id": 381, "name": "Level Up - Lv 10", "price": 35, "tag": "Lv 10", "image": "diamond_package.webp"},
        {"id": 382, "name": "Level Up - Lv 15", "price": 50, "tag": "Lv 15", "image": "diamond_package.webp"},
        {"id": 383, "name": "Level Up - Lv 20", "price": 70, "tag": "Lv 20", "image": "diamond_package.webp"},
        {"id": 384, "name": "Level Up - Lv 25", "price": 70, "tag": "Lv 25", "image": "diamond_package.webp"},
        {"id": 385, "name": "Level Up - Lv 30", "price": 100, "tag": "Lv 30", "image": "diamond_package.webp"},
    ],
    31: [
        {"id": 311, "name": "60 UC", "price": 95, "tag": "Instant", "image": "diamond_package.webp"},
        {"id": 312, "name": "325 UC", "price": 450, "tag": "Popular", "image": "diamond_package.webp"},
        {"id": 313, "name": "660 UC", "price": 890, "tag": "Bonus", "image": "diamond_package.webp"},
        {"id": 314, "name": "1800 UC", "price": 2350, "tag": "", "image": "diamond_package.webp"},
        {"id": 315, "name": "3850 UC", "price": 4650, "tag": "VIP", "image": "diamond_package.webp"},
    ],
    34: [
        {"id": 341, "name": "60 UC Redeem Code", "price": 92, "tag": "", "image": "diamond_package.webp"},
        {"id": 342, "name": "325 UC Redeem Code", "price": 445, "tag": "", "image": "diamond_package.webp"},
        {"id": 343, "name": "660 UC Redeem Code", "price": 880, "tag": "", "image": "diamond_package.webp"},
    ],
    45: [
        {"id": 451, "name": "1 Month CapCut Pro", "price": 150, "tag": "Shared", "image": "diamond_package.webp"},
        {"id": 452, "name": "3 Months CapCut Pro", "price": 380, "tag": "Personal", "image": "diamond_package.webp"},
        {"id": 453, "name": "1 Year CapCut Pro", "price": 999, "tag": "Best", "image": "diamond_package.webp"},
    ],
    44: [
        {"id": 441, "name": "Canva Pro (1 Month)", "price": 40, "tag": "Edu", "image": "diamond_package.webp"},
        {"id": 442, "name": "Canva Pro (1 Year)", "price": 120, "tag": "Invite", "image": "diamond_package.webp"},
        {"id": 443, "name": "Canva Pro Brand Kit (1 Year)", "price": 250, "tag": "Admin", "image": "diamond_package.webp"},
    ],
    43: [
        {"id": 431, "name": "ChatGPT Plus (1 Month)", "price": 450, "tag": "Shared", "image": "diamond_package.webp"},
        {"id": 432, "name": "ChatGPT Plus (Personal Mail)", "price": 2400, "tag": "Private", "image": "diamond_package.webp"},
    ],
    29: [
        {"id": 291, "name": "Netflix 1 Screen 4K (1 Month)", "price": 250, "tag": "UHD", "image": "diamond_package.webp"},
        {"id": 292, "name": "Netflix 1 Profile 4K (3 Months)", "price": 690, "tag": "UHD", "image": "diamond_package.webp"},
    ]
}

# Group products into real categories
categories_map = [
    {
        "id": "cat-ff",
        "cat_id": 1,
        "title": "GAME TOPUP",
        "tag": "🔖",
        "gradient": "from-[#67E8F9] to-[#38BDF8]",
        "icon": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="h-5 w-5 shrink-0 text-[#06B6D4] drop-shadow-[0_0_8px_rgba(6,182,212,0.55)] md:h-8 md:w-8"><line x1="6" x2="10" y1="11" y2="11"></line><line x1="8" x2="8" y1="9" y2="13"></line><line x1="15" x2="15.01" y1="12" y2="12"></line><line x1="18" x2="18.01" y1="10" y2="10"></line><path d="M17.32 5H6.68a4 4 0 0 0-3.978 3.59c-.006.052-.01.101-.017.152C2.604 9.416 2 14.456 2 16a3 3 0 0 0 3 3c1 0 1.5-.5 2-1l1.414-1.414A2 2 0 0 1 9.828 16h4.344a2 2 0 0 1 1.414.586L17 18c.5.5 1 1 2 1a3 3 0 0 0 3-3c0-1.545-.604-6.584-.685-7.258-.007-.05-.011-.1-.017-.151A4 4 0 0 0 17.32 5z"></path></svg>',
        "color": "#06B6D4"
    },
    {
        "id": "cat-others",
        "cat_id": 8,
        "title": "Others Game Topup",
        "tag": "⚽",
        "gradient": "from-[#34D399] to-[#10B981]",
        "icon": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="h-5 w-5 shrink-0 text-[#10B981] drop-shadow-[0_0_8px_rgba(16,185,129,0.55)] md:h-8 md:w-8"><circle cx="12" cy="12" r="10"></circle><path d="m4.93 4.93 4.24 4.24"></path><path d="m14.83 9.17 4.24-4.24"></path><path d="m14.83 14.83 4.24 4.24"></path><path d="m9.17 14.83-4.24 4.24"></path><circle cx="12" cy="12" r="4"></circle></svg>',
        "color": "#10B981"
    },
    {
        "id": "cat-pubg",
        "cat_id": 4,
        "title": "PUBG TOPUP",
        "tag": "🔖",
        "gradient": "from-[#FBBF24] to-[#F59E0B]",
        "icon": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="h-5 w-5 shrink-0 text-[#F59E0B] drop-shadow-[0_0_8px_rgba(245,158,11,0.55)] md:h-8 md:w-8"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>',
        "color": "#F59E0B"
    },
    {
        "id": "cat-sub",
        "cat_id": 2,
        "title": "APP SUBSCRIPTION",
        "tag": "🔖",
        "gradient": "from-[#A78BFA] to-[#8B5CF6]",
        "icon": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="h-5 w-5 shrink-0 text-[#8B5CF6] drop-shadow-[0_0_8px_rgba(139,92,246,0.55)] md:h-8 md:w-8"><rect width="20" height="14" x="2" y="5" rx="2"></rect><line x1="2" x2="22" y1="10" y2="10"></line></svg>',
        "color": "#8B5CF6"
    },
    {
        "id": "cat-smm",
        "cat_id": 6,
        "title": "SMM PANEL SERVICE",
        "tag": "🔖",
        "gradient": "from-[#F43F5E] to-[#E11D48]",
        "icon": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="h-5 w-5 shrink-0 text-[#E11D48] drop-shadow-[0_0_8px_rgba(225,29,72,0.55)] md:h-8 md:w-8"><path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"></path><path d="M13.73 21a2 2 0 0 1-3.46 0"></path></svg>',
        "color": "#E11D48"
    }
]

print("Script template ready.")
