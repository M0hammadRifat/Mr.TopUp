# Complete RRR Topup Clone Generator
import json

with open('/storage/emulated/0/Codex/freefire-topup/app_data.json', encoding='utf-8') as f:
    app_data = json.load(f)

products = app_data['products']
packages_21 = app_data['packages_21']
public_orders = app_data['orders']

categories = [
    {
        'id': 'cat-ff',
        'cat_id': 1,
        'title': 'GAME TOPUP',
        'tag': '🔖',
        'gradient': 'from-[#67E8F9] to-[#38BDF8]',
        'color': '#06B6D4',
        'icon': '<i class="fa-solid fa-gamepad text-[#06B6D4] text-lg sm:text-2xl"></i>'
    },
    {
        'id': 'cat-others',
        'cat_id': 8,
        'title': 'Others Game Topup',
        'tag': '⚽',
        'gradient': 'from-[#34D399] to-[#10B981]',
        'color': '#10B981',
        'icon': '<i class="fa-solid fa-futbol text-[#10B981] text-lg sm:text-2xl"></i>'
    },
    {
        'id': 'cat-pubg',
        'cat_id': 4,
        'title': 'PUBG TOPUP',
        'tag': '🔖',
        'gradient': 'from-[#FBBF24] to-[#F59E0B]',
        'color': '#F59E0B',
        'icon': '<i class="fa-solid fa-crosshairs text-[#F59E0B] text-lg sm:text-2xl"></i>'
    },
    {
        'id': 'cat-sub',
        'cat_id': 2,
        'title': 'APP SUBSCRIPTION',
        'tag': '🔖',
        'gradient': 'from-[#A78BFA] to-[#8B5CF6]',
        'color': '#8B5CF6',
        'icon': '<i class="fa-solid fa-circle-play text-[#8B5CF6] text-lg sm:text-2xl"></i>'
    },
    {
        'id': 'cat-smm',
        'cat_id': 6,
        'title': 'SMM PANEL SERVICE',
        'tag': '🔖',
        'gradient': 'from-[#F43F5E] to-[#E11D48]',
        'color': '#E11D48',
        'icon': '<i class="fa-solid fa-bell text-[#E11D48] text-lg sm:text-2xl"></i>'
    }
]

# Generate product cards HTML by category
category_sections_html = ''
for cat in categories:
    cid = cat['cat_id']
    cat_prods = [p for p in products if p.get('category_id') == cid]
    if not cat_prods:
        continue
    
    cards_html = ''
    for p in cat_prods:
        pid = p['id']
        pname = p['name']
        logo = p.get('logo', '')
        local_img = 'images/products/' + logo
        remote_img = 'https://apis.rrrtopup.com/images/' + logo
        
        cards_html += f'''
        <div class="product-item block h-full w-full focus:outline-none focus:ring-0 cursor-pointer" data-id="{pid}" data-name="{pname.lower()}" onclick="openProduct({pid})">
            <div class="group w-full overflow-hidden rounded-[16px] border border-theme-subtle bg-surface-main shadow-[0_8px_22px_rgba(0,0,0,0.35)] transition-all duration-[250ms] ease-out hover:-translate-y-1 hover:border-theme-hover hover:shadow-[0_10px_35px_rgba(45,97,204,0.2)]">
                <div class="relative aspect-square w-full overflow-hidden bg-surface-main">
                    <img alt="{pname}" loading="lazy" class="object-cover object-center w-full h-full transition-transform duration-[250ms] ease-out will-change-transform group-hover:scale-[1.04]"
                         src="{local_img}" onerror="this.onerror=null; this.src='{remote_img}';"/>
                    <div class="absolute top-2 right-2 bg-primary-500/90 text-[10px] font-bold text-white px-1.5 py-0.5 rounded shadow">INSTANT</div>
                </div>
                <div class="flex min-h-[44px] items-center justify-center border-t border-theme-subtle bg-surface/95 px-2 py-2 backdrop-blur-sm">
                    <span class="text-center text-[11px] font-semibold leading-tight text-[#F8FAFC] sm:text-[13px] line-clamp-1">{pname}</span>
                </div>
            </div>
        </div>
        '''
    
    category_sections_html += f'''
    <section id="{cat['id']}" class="container mx-auto px-3 sm:px-4 max-w-7xl mt-4 category-section">
        <div class="flex flex-col items-center py-4 md:py-6">
            <h3 class="flex flex-wrap items-center justify-center gap-2 text-center text-xl font-bold uppercase tracking-wide text-white md:text-3xl">
                {cat['icon']}
                <span>{cat['title'].split()[0]}</span>
                <span class="bg-gradient-to-r {cat['gradient']} bg-clip-text text-transparent drop-shadow-[0_0_10px_rgba(6,182,212,0.35)]">
                    {' '.join(cat['title'].split()[1:])} {cat['tag']}
                </span>
            </h3>
            <span class="mt-2 h-0.5 w-14 rounded-full bg-[{cat['color']}] shadow-[0_0_12px_{cat['color']}] md:w-16"></span>
        </div>
        <div class="grid grid-cols-3 gap-2.5 sm:grid-cols-3 lg:grid-cols-6 md:gap-4 md:py-3">
            {cards_html}
        </div>
    </section>
    '''

# Generate recent orders HTML
orders_html = ''
for o in public_orders:
    name = o.get('full_name', 'Customer')
    avatar = o.get('avatar', 'https://apis.rrrtopup.com/uploads/images/1776251457859-1776068722862-RRR_Fov_2.png')
    pkg_name = o.get('name', 'Diamond Topup')
    amount = o.get('amount', '0')
    status = o.get('status', 'completed')
    time_str = 'just now'
    
    status_badge = '<span class="inline-flex items-center gap-1 rounded-full px-2 py-1 text-[10px] font-bold capitalize sm:px-3 sm:py-1.5 sm:text-xs bg-gradient-to-r from-[#22C55E] to-[#16A34A] text-white shadow-[0_0_14px_rgba(34,197,94,0.35)]"><i class="fa-solid fa-check text-[10px]"></i> completed</span>'
    if status != 'completed':
        status_badge = f'<span class="inline-flex items-center gap-1 rounded-full px-2 py-1 text-[10px] font-bold capitalize sm:px-3 sm:py-1.5 sm:text-xs bg-amber-500/90 text-white">{status}</span>'
        
    orders_html += f'''
    <article class="theme-order-card group animate-card-glow mb-2.5">
        <div class="relative z-10 flex items-center gap-2.5 px-3 py-2.5 sm:gap-4 sm:px-4 sm:py-3.5 md:gap-6">
            <div class="relative h-10 w-10 shrink-0 sm:h-12 sm:w-12 md:h-14 md:w-14">
                <img src="{avatar}" alt="{name}" class="h-full w-full rounded-full object-cover ring-2 ring-primary-300/45 transition-all duration-300 group-hover:ring-[3px]" onerror="this.src=\'https://lh3.googleusercontent.com/a/default-user=s96-c\';"/>
            </div>
            <div class="min-w-0 flex-1">
                <div class="flex items-center gap-1.5">
                    <h2 class="truncate text-[13px] font-semibold text-white sm:text-[16px] md:text-[18px]">{name}</h2>
                </div>
                <p class="mt-0.5 flex items-center gap-1.5 text-[11px] text-[#94A3B8] sm:text-[13px] md:text-[14px]">
                    <i class="fa-solid fa-gem text-primary-300 text-xs shrink-0"></i>
                    <span class="truncate">{pkg_name}</span>
                </p>
            </div>
            <div class="hidden shrink-0 text-right sm:block">
                <p class="text-[18px] font-bold leading-none text-[#34D399] md:text-[22px]">{amount} ৳</p>
                <p class="mt-1 flex items-center justify-end gap-1 text-[11px] text-primary-300/80 md:text-xs">
                    <i class="fa-regular fa-clock"></i> {time_str}
                </p>
            </div>
            <div class="flex shrink-0 flex-col items-end gap-1">
                <p class="text-[14px] font-bold text-[#34D399] sm:hidden">{amount} ৳</p>
                {status_badge}
            </div>
        </div>
        <div class="pointer-events-none absolute inset-0 z-20 overflow-hidden rounded-[18px] sm:rounded-[22px]">
            <div class="absolute left-0 top-0 h-full w-16 animate-card-slice bg-gradient-to-r from-transparent via-primary-300/55 to-transparent sm:w-24"></div>
        </div>
    </article>
    '''

with open('/storage/emulated/0/Codex/category_sections.html', 'w', encoding='utf-8') as f:
    f.write(category_sections_html)

with open('/storage/emulated/0/Codex/orders_snippet.html', 'w', encoding='utf-8') as f:
    f.write(orders_html)

print('Category and orders snippets written!')
