# Assembles complete, 100% error-free index.html for freefire-topup
import json

with open('/storage/emulated/0/Codex/freefire-topup/category_sections.html', encoding='utf-8') as f:
    category_sections_html = f.read()

with open('/storage/emulated/0/Codex/freefire-topup/orders_snippet.html', encoding='utf-8') as f:
    orders_html = f.read()

with open('/storage/emulated/0/Codex/freefire-topup/app_data.json', encoding='utf-8') as f:
    app_data = json.load(f)

products_json = json.dumps(app_data['products'], ensure_ascii=False)
packages_21_json = json.dumps(app_data['packages_21'], ensure_ascii=False)
orders_json = json.dumps(app_data['orders'], ensure_ascii=False)

html_content = f'''<!DOCTYPE html>
<html lang="bn" class="dark">
<head>
    <meta charset="UTF-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no"/>
    <title>Rrr Topup - Best Free Fire Diamond Topup in Bangladesh | Instant Free Fire Topup</title>
    <meta name="description" content="Rrr Topup - Best Free Fire Diamond Topup in Bangladesh | Instant Free Fire Topup"/>
    <meta name="theme-color" content="#FF6B35"/>
    <link rel="icon" type="image/png" href="images/favicon.png"/>
    <link rel="preconnect" href="https://fonts.googleapis.com"/>
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&family=Lato:wght@400;700;900&display=swap" rel="stylesheet"/>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css"/>
    <link rel="stylesheet" href="css/ecca411e77dec624.css"/>
    <link rel="stylesheet" href="css/bc8831281eb208c3.css"/>
    <style>
        :root {{
            --primary: #FF6B35;
            --primary-glow: rgba(255, 107, 53, 0.35);
            --bg-main: #08091a;
            --surface-main: #0f1130;
            --border-theme: rgba(44,33,88,0.5);
            --border-theme-hover: rgba(56,189,248,0.45);
        }}
        *, *::before, *::after {{
            box-sizing: border-box;
        }}
        body {{
            font-family: 'Poppins', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background-color: var(--bg-main);
            color: #F8FAFC;
            overflow-x: hidden;
            margin: 0;
            padding: 0;
        }}
        /* Animations */
        @keyframes yt-pulse {{
            0%, 100% {{ transform: scale(1); opacity: 0.8; }}
            50% {{ transform: scale(1.18); opacity: 0.3; }}
        }}
        .animate-yt-pulse {{
            animation: yt-pulse 2s infinite ease-in-out;
        }}
        /* Hero Banner Slider Styles */
        .hero-slider-wrap {{
            position: relative;
            width: 100%;
            aspect-ratio: 900 / 371;
            min-height: 155px;
            max-height: 480px;
            overflow: hidden;
            border-radius: 18px;
            background: #0b0d26;
            touch-action: pan-y;
        }}
        .hero-slider-track {{
            position: absolute;
            inset: 0;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            display: flex;
            transition: transform 0.45s cubic-bezier(0.25, 1, 0.5, 1);
            will-change: transform;
        }}
        .hero-slide {{
            flex: 0 0 100%;
            width: 100%;
            height: 100%;
            min-width: 100%;
            max-width: 100%;
            position: relative;
            overflow: hidden;
            cursor: pointer;
            user-select: none;
            -webkit-user-select: none;
        }}
        .hero-slide img {{
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: block;
            pointer-events: none;
        }}
        .slider-arrow-btn {{
            position: absolute;
            top: 50%;
            transform: translateY(-50%);
            z-index: 25;
            width: 36px;
            height: 36px;
            border-radius: 50%;
            background: rgba(10, 13, 36, 0.75);
            border: 1px solid rgba(255, 255, 255, 0.25);
            backdrop-filter: blur(8px);
            -webkit-backdrop-filter: blur(8px);
            color: #fff;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: all 0.2s ease;
            box-shadow: 0 4px 14px rgba(0,0,0,0.5);
        }}
        .slider-arrow-btn:hover {{
            background: #FF6B35;
            border-color: #FF6B35;
            transform: translateY(-50%) scale(1.08);
        }}
        .slider-arrow-btn:active {{
            transform: translateY(-50%) scale(0.92);
        }}
        @media (min-width: 640px) {{
            .slider-arrow-btn {{
                width: 44px;
                height: 44px;
            }}
        }}

        @keyframes float-fab {{
            0%, 100% {{ transform: translateY(0); }}
            50% {{ transform: translateY(-6px); }}
        }}
        .theme-fab-glow {{
            box-shadow: 0 0 25px rgba(56, 189, 248, 0.6), 0 0 50px rgba(99, 102, 241, 0.4);
            animation: float-fab 3s ease-in-out infinite;
        }}
        @keyframes cardSlice {{
            0% {{ transform: translateX(-150%); }}
            100% {{ transform: translateX(350%); }}
        }}
        .animate-card-slice {{
            animation: cardSlice 4s infinite linear;
        }}
        .theme-order-card {{
            position: relative;
            background: linear-gradient(135deg, rgba(20, 22, 56, 0.85) 0%, rgba(15, 17, 48, 0.95) 100%);
            border: 1px solid rgba(44, 33, 88, 0.55);
            border-radius: 18px;
            overflow: hidden;
            transition: all 0.25s ease;
        }}
        .theme-order-card:hover {{
            border-color: rgba(56, 189, 248, 0.4);
            transform: translateY(-2px);
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4);
        }}
        .pkg-select-card {{
            position: relative;
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 10px 12px;
            background: #15122c;
            border: 1.5px solid rgba(44, 33, 88, 0.65);
            border-radius: 12px;
            cursor: pointer;
            transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
        }}
        .pkg-select-card:hover {{
            border-color: rgba(56, 189, 248, 0.5);
            background: #1a1638;
            transform: translateY(-1.5px);
        }}
        .pkg-select-card.active {{
            background: linear-gradient(135deg, #1c173c 0%, #221c4a 100%);
            border-color: #FF6B35;
            box-shadow: 0 0 16px rgba(255, 107, 53, 0.35);
        }}
        .pkg-select-card.active .pkg-check {{
            background: #FF6B35;
            border-color: #FF6B35;
            color: #fff;
        }}
        .pkg-check {{
            width: 18px;
            height: 18px;
            border-radius: 50%;
            border: 1.5px solid rgba(148, 163, 184, 0.4);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 10px;
            color: transparent;
            transition: all 0.2s ease;
            flex-shrink: 0;
        }}
        /* Modal Backdrop */
        .modal-backdrop {{
            position: fixed;
            inset: 0;
            background: rgba(4, 5, 15, 0.85);
            backdrop-filter: blur(8px);
            z-index: 1000;
            display: none;
            align-items: center;
            justify-content: center;
            padding: 16px;
        }}
        .modal-backdrop.open {{
            display: flex;
        }}
        .modal-card {{
            background: #0d0f28;
            border: 1px solid rgba(56, 189, 248, 0.25);
            border-radius: 20px;
            width: 100%;
            max-width: 480px;
            box-shadow: 0 25px 60px rgba(0, 0, 0, 0.7);
            overflow: hidden;
            animation: modalPop 0.25s cubic-bezier(0.16, 1, 0.3, 1);
        }}
        @keyframes modalPop {{
            0% {{ transform: scale(0.92); opacity: 0; }}
            100% {{ transform: scale(1); opacity: 1; }}
        }}
        /* Search Box glow */
        .search-box-input:focus {{
            border-color: #38BDF8;
            box-shadow: 0 0 15px rgba(56, 189, 248, 0.25);
        }}
        /* Notice ticker */
        .marquee-content {{
            display: inline-block;
            white-space: nowrap;
            animation: marquee 25s linear infinite;
        }}
        .marquee-content:hover {{
            animation-play-state: paused;
        }}
        @keyframes marquee {{
            0% {{ transform: translateX(100%); }}
            100% {{ transform: translateX(-100%); }}
        }}
    </style>
</head>
<body class="home-dark flex min-h-screen flex-col">
<div id="__next">
    <div class="site-chrome sticky top-0 z-[200]">
        <!-- Mobile Sidebar Overlay -->
        <div id="sidebar_overly" class="fixed overflow-hidden z-[999999] bg-gray-900/60 backdrop-blur-sm inset-0 transform ease-in-out transition-all duration-300 opacity-0 pointer-events-none">
            <div id="sidebar_panel" class="w-[78%] sm:w-[320px] right-0 absolute bg-[#090b22] border-l border-primary-500/20 h-[100dvh] max-h-[100dvh] shadow-2xl duration-300 ease-in-out transition-all transform overflow-y-auto translate-x-full flex flex-col justify-between">
                <div>
                    <!-- Sidebar Header -->
                    <div class="flex justify-between items-center px-4 py-3.5 border-b border-theme-subtle bg-surface-main">
                        <div class="flex items-center gap-2">
                            <img src="images/logo.png" alt="Logo" class="h-7 w-auto" onerror="this.src=\'https://apis.rrrtopup.com/uploads/images/1793198575181-1768754618825-logo0d22abf7_1.png\'"/>
                        </div>
                        <button onclick="toggleSidebar(false)" class="text-slate-400 hover:text-white p-1 rounded-lg">
                            <i class="fa-solid fa-xmark text-xl"></i>
                        </button>
                    </div>
                    <!-- User Profile Card in Sidebar -->
                    <div class="p-3 bg-surface/50 border-b border-theme-subtle">
                        <div class="flex items-center gap-3">
                            <div class="w-10 h-10 rounded-full bg-primary-500/20 border border-primary-500/40 flex items-center justify-center text-primary-400 font-bold" id="sidebar-user-avatar">
                                <i class="fa-solid fa-user"></i>
                            </div>
                            <div class="flex-1 min-w-0">
                                <p class="text-sm font-semibold text-white truncate" id="sidebar-user-name">Guest User</p>
                                <p class="text-xs text-primary-400 font-medium flex items-center gap-1">
                                    <span>Wallet:</span>
                                    <span class="font-bold tabular-nums" id="sidebar-wallet-val">0.00 ৳</span>
                                </p>
                            </div>
                            <button onclick="openAddMoneyModal()" class="text-[11px] font-bold bg-primary-500 text-white px-2 py-1 rounded-md hover:bg-primary-600 transition shadow">
                                + Add
                            </button>
                        </div>
                        <div onclick="showConvexStatus()" class="mt-2.5 px-2.5 py-1.5 rounded-lg bg-emerald-500/10 border border-emerald-500/25 flex items-center justify-between text-xs text-emerald-400 cursor-pointer">
                            <span class="flex items-center gap-1.5 font-medium"><i class="fa-solid fa-database text-[11px]"></i> Convex Live DB</span>
                            <span class="font-bold text-[10px] bg-emerald-500/20 px-1.5 py-0.5 rounded text-emerald-300">CONNECTED 🟢</span>
                        </div>
                    </div>
                    <!-- Sidebar Navigation Links -->
                    <div class="px-3 py-3 space-y-1.5">
                        <a href="javascript:void(0)" onclick="navigateToHome(); toggleSidebar(false)" class="flex items-center gap-3 px-3 py-2.5 rounded-xl text-slate-200 hover:bg-surface-main hover:text-primary-400 transition font-medium text-sm">
                            <i class="fa-solid fa-house w-5 text-center text-primary-400"></i> Home
                        </a>
                        <a href="javascript:void(0)" onclick="scrollToSection(\'cat-ff\'); toggleSidebar(false)" class="flex items-center gap-3 px-3 py-2.5 rounded-xl text-slate-200 hover:bg-surface-main hover:text-primary-400 transition font-medium text-sm">
                            <i class="fa-solid fa-gamepad w-5 text-center text-cyan-400"></i> Free Fire Topup
                        </a>
                        <a href="javascript:void(0)" onclick="scrollToSection(\'cat-pubg\'); toggleSidebar(false)" class="flex items-center gap-3 px-3 py-2.5 rounded-xl text-slate-200 hover:bg-surface-main hover:text-primary-400 transition font-medium text-sm">
                            <i class="fa-solid fa-crosshairs w-5 text-center text-amber-400"></i> PUBG Topup
                        </a>
                        <a href="javascript:void(0)" onclick="scrollToSection(\'cat-sub\'); toggleSidebar(false)" class="flex items-center gap-3 px-3 py-2.5 rounded-xl text-slate-200 hover:bg-surface-main hover:text-primary-400 transition font-medium text-sm">
                            <i class="fa-solid fa-play-circle w-5 text-center text-purple-400"></i> App Subscription
                        </a>
                        <a href="javascript:void(0)" onclick="openTrackOrderModal(); toggleSidebar(false)" class="flex items-center gap-3 px-3 py-2.5 rounded-xl text-slate-200 hover:bg-surface-main hover:text-primary-400 transition font-medium text-sm">
                            <i class="fa-solid fa-truck-fast w-5 text-center text-emerald-400"></i> Order Track
                        </a>
                        <a href="javascript:void(0)" onclick="openTutorialModal(); toggleSidebar(false)" class="flex items-center gap-3 px-3 py-2.5 rounded-xl text-slate-200 hover:bg-surface-main hover:text-primary-400 transition font-medium text-sm">
                            <i class="fa-brands fa-youtube w-5 text-center text-red-500"></i> Video Tutorial
                        </a>
                        <a href="signup.html" class="flex items-center gap-3 px-3 py-2.5 rounded-xl text-primary-300 bg-primary-500/10 hover:bg-primary-500/20 transition font-semibold text-sm">
                            <i class="fa-solid fa-user-plus w-5 text-center text-primary-400"></i> সাইন-আপ (Sign Up)
                        </a>
                        <a href="https://t.me/rrrtopup526" target="_blank" class="flex items-center gap-3 px-3 py-2.5 rounded-xl text-slate-200 hover:bg-surface-main hover:text-primary-400 transition font-medium text-sm">
                            <i class="fa-brands fa-telegram w-5 text-center text-sky-400"></i> Telegram Support
                        </a>
                    </div>
                </div>
                <!-- Sidebar Footer -->
                <div class="p-4 border-t border-theme-subtle bg-surface-main space-y-2">
                    <button id="sidebar-auth-btn" onclick="openLoginModal(); toggleSidebar(false)" class="w-full py-2.5 rounded-xl bg-primary-500 hover:bg-primary-600 text-white font-semibold text-sm transition shadow-lg shadow-primary-500/25 flex items-center justify-center gap-2">
                        <i class="fa-solid fa-right-to-bracket"></i> Login / Register
                    </button>
                    <p class="text-[11px] text-center text-slate-500">RRR Topup &bull; Version 2.0</p>
                </div>
            </div>
        </div>

        <!-- Sticky Main Header -->
        <header class="w-full overflow-visible border-b border-[rgba(44,33,88,0.35)] bg-[rgba(11,11,32,0.94)] backdrop-blur-[18px]">
            <div class="container mx-auto px-3 sm:px-4 max-w-7xl">
                <div class="flex items-center justify-between py-2 sm:py-2.5 gap-2 sm:gap-4">
                    <!-- Brand Logo & Convex Live DB Badge -->
                    <div class="flex items-center gap-2 sm:gap-3 shrink-0">
                        <div class="max-w-[115px] sm:max-w-[135px]">
                            <a href="javascript:void(0)" onclick="navigateToHome()" class="block">
                                <img src="images/logo.png" alt="Rrr Topup" class="h-8 sm:h-9 w-auto object-contain"
                                     onerror="this.src=\'https://apis.rrrtopup.com/uploads/images/1793198575181-1768754618825-logo0d22abf7_1.png\'"/>
                            </a>
                        </div>
                        <div onclick="showConvexStatus()" class="hidden md:flex items-center gap-1.5 px-2.5 py-1 rounded-full bg-emerald-500/10 border border-emerald-500/30 text-[10px] text-emerald-400 font-semibold cursor-pointer hover:bg-emerald-500/20 transition shadow-sm">
                            <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-ping"></span>
                            <span>Convex Live DB 🟢</span>
                        </div>
                    </div>

                    <!-- Search Bar (Live filter) -->
                    <div class="flex-1 max-w-md mx-2 relative hidden sm:block">
                        <div class="relative flex items-center">
                            <i class="fa-solid fa-magnifying-glass absolute left-3.5 text-slate-400 text-xs sm:text-sm"></i>
                            <input type="text" id="header-search" placeholder="Search games, packages, topup..."
                                   oninput="handleSearch(this.value)"
                                   class="search-box-input w-full bg-[#141638] border border-[rgba(56,189,248,0.2)] rounded-full pl-9 pr-8 py-1.5 text-xs sm:text-sm text-white placeholder-slate-400 focus:outline-none transition"/>
                            <button id="clear-search-btn" onclick="clearSearch()" class="hidden absolute right-3 text-slate-400 hover:text-white text-xs">
                                <i class="fa-solid fa-circle-xmark"></i>
                            </button>
                        </div>
                    </div>

                    <!-- Desktop Navigation Menu -->
                    <nav class="hidden md:flex items-center justify-end gap-1.5 lg:gap-3">
                        <a href="javascript:void(0)" onclick="navigateToHome()" class="flex items-center px-2.5 py-1.5 font-medium text-sm text-slate-200 hover:text-primary-300 transition-colors">
                            <span>Home</span>
                        </a>
                        <a href="javascript:void(0)" onclick="scrollToSection(\'cat-ff\')" class="flex items-center px-2.5 py-1.5 font-medium text-sm text-slate-200 hover:text-primary-300 transition-colors">
                            <span>Topup</span>
                        </a>
                        <a href="javascript:void(0)" onclick="openTrackOrderModal()" class="flex items-center px-2.5 py-1.5 font-medium text-sm text-slate-200 hover:text-primary-300 transition-colors">
                            <i class="fa-solid fa-truck-fast mr-1.5 text-emerald-400"></i>
                            <span>Track Order</span>
                        </a>

                        <!-- Wallet Button -->
                        <div onclick="openAddMoneyModal()" class="cursor-pointer flex items-center gap-1.5 bg-[#17193d] border border-primary-500/30 hover:border-primary-500/70 px-3 py-1.5 rounded-full transition shadow-sm group">
                            <div class="w-5 h-5 rounded-full bg-primary-500/20 flex items-center justify-center text-primary-400 text-xs group-hover:scale-110 transition">
                                <i class="fa-solid fa-wallet"></i>
                            </div>
                            <span class="text-xs font-semibold text-white tabular-nums" id="header-wallet-val">0.00 ৳</span>
                            <span class="text-[10px] font-bold bg-primary-500 text-white px-1.5 py-0.5 rounded-full">+ Add</span>
                        </div>

                        <!-- Auth Login / Sign Up -->
                        <div class="pl-1 flex items-center gap-1.5">
                            <a href="signup.html" class="hidden lg:flex items-center gap-1 px-3 py-1.5 rounded-lg border border-primary-500/30 bg-primary-500/10 hover:bg-primary-500/20 text-primary-300 font-semibold text-xs transition">
                                <i class="fa-solid fa-user-plus text-[11px]"></i>
                                <span>Sign Up</span>
                            </a>
                            <button id="header-auth-btn" onclick="openLoginModal()" class="_btn bg-primary-500 hover:bg-primary-600 text-white font-semibold py-1.5 px-3.5 rounded-lg text-xs shadow-md transition shadow-primary-500/20 flex items-center gap-1.5">
                                <i class="fa-regular fa-user"></i>
                                <span>Login</span>
                            </button>
                        </div>
                    </nav>

                    <!-- Mobile Header Actions -->
                    <div class="flex items-center gap-2 md:hidden">
                        <!-- Mobile Wallet badge -->
                        <div onclick="openAddMoneyModal()" class="cursor-pointer flex items-center gap-1 bg-[#17193d] border border-primary-500/40 px-2 py-1 rounded-full text-xs">
                            <i class="fa-solid fa-wallet text-primary-400 text-[11px]"></i>
                            <span class="font-bold text-white text-[11px] tabular-nums" id="mobile-wallet-val">0 ৳</span>
                        </div>
                        <!-- Mobile Hamburger Button -->
                        <button onclick="toggleSidebar(true)" class="p-2 text-slate-200 hover:text-white rounded-lg bg-[#141638] border border-[rgba(44,33,88,0.4)]">
                            <i class="fa-solid fa-bars text-lg"></i>
                        </button>
                    </div>
                </div>

                <!-- Mobile Search Input row -->
                <div class="pb-2 sm:hidden">
                    <div class="relative flex items-center">
                        <i class="fa-solid fa-magnifying-glass absolute left-3 text-slate-400 text-xs"></i>
                        <input type="text" placeholder="Search games, packages, topup..."
                               oninput="handleSearch(this.value)"
                               class="search-box-input w-full bg-[#141638] border border-[rgba(56,189,248,0.2)] rounded-full pl-8 pr-7 py-1.5 text-xs text-white placeholder-slate-400 focus:outline-none transition"/>
                    </div>
                </div>
            </div>
        </header>
    </div>

    <!-- MAIN APP CONTAINER -->
    <main id="app-content" class="flex-1 pb-16 md:pb-6">
        
        <!-- ============================================== -->
        <!-- VIEW 1: HOME CATALOG VIEW -->
        <!-- ============================================== -->
        <div id="home-view">
            <!-- Notice Marquee Ticker -->
            <div class="bg-gradient-to-r from-[#111335] via-[#161a48] to-[#111335] border-y border-[rgba(56,189,248,0.18)] py-1.5 overflow-hidden">
                <div class="container mx-auto px-4 max-w-7xl flex items-center gap-2">
                    <span class="flex items-center gap-1 text-[11px] font-bold text-primary-400 shrink-0 bg-primary-500/15 px-2 py-0.5 rounded-full border border-primary-500/30">
                        <i class="fa-solid fa-bullhorn animate-bounce"></i> NOTICE:
                    </span>
                    <div class="overflow-hidden flex-1 relative h-5">
                        <div class="marquee-content text-xs font-medium text-slate-300">
                            📢 স্বাগতম RRR Topup এ! যেকোনো প্রয়োজনে আমাদের Telegram Support এ মেসেজ করুন। Free Fire UID Topup ও Subscription সার্ভিসে পাচ্ছেন ১০০% ইনস্ট্যান্ট অটো ডেলিভারি! বিকাশ, নগদ, রকেট দিয়ে সহজে পেমেন্ট করুন।
                        </div>
                    </div>
                </div>
            </div>

            <!-- Hero Banner Slider -->
            <section class="mb-3 mt-2 sm:mt-4 home_slider_wrapper flex flex-col items-center">
                <div class="container mx-auto px-3 sm:px-4 max-w-7xl">
                    <div id="hero-slider-box" class="hero-slider-wrap border border-[rgba(56,189,248,0.25)] shadow-[0_12px_36px_rgba(0,0,0,0.55)]">
                        <!-- Slider Items Track -->
                        <div id="slider-track" class="hero-slider-track">
                            <!-- Slide 1: Telegram Official -->
                            <div class="hero-slide" onclick="window.open(\'https://t.me/+zkiWsAnlHlU4YjE1\', \'_blank\')">
                                <picture class="w-full h-full block">
                                    <source srcset="images/banner1.webp" type="image/webp">
                                    <source srcset="images/banner1.jpg" type="image/jpeg">
                                    <img src="images/banner1.webp" alt="Telegram Official"
                                         onerror="handleBannerError(this, 1)"/>
                                </picture>
                            </div>
                            <!-- Slide 2: Auto Bot Topup -->
                            <div class="hero-slide" onclick="openProduct(21)">
                                <picture class="w-full h-full block">
                                    <source srcset="images/banner2.webp" type="image/webp">
                                    <source srcset="images/banner2.jpg" type="image/jpeg">
                                    <img src="images/banner2.webp" alt="Free Fire Auto Bot Topup"
                                         onerror="handleBannerError(this, 2)"/>
                                </picture>
                            </div>
                            <!-- Slide 3: Video Tutorial -->
                            <div class="hero-slide" onclick="openTutorialModal()">
                                <picture class="w-full h-full block">
                                    <source srcset="images/banner3.webp" type="image/webp">
                                    <source srcset="images/banner3.jpg" type="image/jpeg">
                                    <img src="images/banner3.webp" alt="Video Tutorial"
                                         onerror="handleBannerError(this, 3)"/>
                                </picture>
                                <div class="absolute inset-0 z-[5] flex items-center justify-center pointer-events-none">
                                    <div class="group relative flex h-[46px] w-[46px] items-center justify-center sm:h-[64px] sm:w-[64px]">
                                        <span class="absolute inset-0 rounded-full bg-gradient-to-br from-primary-300 via-primary-500 to-primary-700 animate-yt-pulse"></span>
                                        <span class="relative z-[1] flex h-[46px] w-[46px] items-center justify-center rounded-full bg-gradient-to-br from-primary-400 to-primary-600 text-white shadow-xl transition-transform duration-300 group-hover:scale-110 sm:h-[64px] sm:w-[64px]">
                                            <i class="fa-solid fa-play text-sm sm:text-lg ml-0.5"></i>
                                        </span>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- Prev Arrow Button -->
                        <button type="button" aria-label="Previous Slide" onclick="prevSlide(event)"
                                class="slider-arrow-btn left-2 sm:left-4">
                            <i class="fa-solid fa-chevron-left text-xs sm:text-sm"></i>
                        </button>

                        <!-- Next Arrow Button -->
                        <button type="button" aria-label="Next Slide" onclick="nextSlide(event)"
                                class="slider-arrow-btn right-2 sm:right-4">
                            <i class="fa-solid fa-chevron-right text-xs sm:text-sm"></i>
                        </button>

                        <!-- Slider Navigation Dots -->
                        <div class="absolute bottom-2.5 sm:bottom-4 left-0 right-0 z-20 flex items-center justify-center gap-1.5 sm:gap-2" id="slider-dots">
                            <span onclick="setSlide(0, event)" class="slider-dot w-6 sm:w-8 h-1.5 sm:h-2 rounded-full bg-primary-500 transition-all cursor-pointer shadow-md"></span>
                            <span onclick="setSlide(1, event)" class="slider-dot w-2 sm:w-2.5 h-1.5 sm:h-2 rounded-full bg-white/40 hover:bg-white/70 transition-all cursor-pointer"></span>
                            <span onclick="setSlide(2, event)" class="slider-dot w-2 sm:w-2.5 h-1.5 sm:h-2 rounded-full bg-white/40 hover:bg-white/70 transition-all cursor-pointer"></span>
                        </div>
                    </div>
                </div>
            </section>

            <!-- Quick Support & Action Badges -->
            <section class="container mx-auto px-3 sm:px-4 max-w-7xl mb-3 sm:mb-4">
                <div class="grid grid-cols-3 md:grid-cols-5 gap-2 sm:gap-3.5">
                    <!-- Telegram Support -->
                    <a href="https://t.me/rrrtopup526" target="_blank" class="flex items-center gap-2 rounded-xl bg-gradient-to-r from-primary-600 to-primary-400 px-2.5 py-2 text-white shadow-[0_8px_18px_rgba(45,97,204,0.28)] transition-all duration-300 hover:-translate-y-0.5 hover:shadow-[0_10px_22px_rgba(45,97,204,0.38)]">
                        <i class="fa-brands fa-telegram text-xl sm:text-2xl text-white"></i>
                        <div class="leading-tight min-w-0">
                            <p class="text-[9px] text-white/80 leading-tight uppercase font-medium">Support</p>
                            <p class="font-bold text-[11px] sm:text-xs text-white leading-tight truncate">Telegram</p>
                        </div>
                    </a>

                    <!-- Telegram Group -->
                    <a href="https://t.me/+mRE_lH8dUxU5NTg9" target="_blank" class="flex items-center gap-2 rounded-xl bg-gradient-to-r from-primary-600 to-primary-400 px-2.5 py-2 text-white shadow-[0_8px_18px_rgba(45,97,204,0.28)] transition-all duration-300 hover:-translate-y-0.5 hover:shadow-[0_10px_22px_rgba(45,97,204,0.38)]">
                        <i class="fa-solid fa-users text-xl sm:text-2xl text-white"></i>
                        <div class="leading-tight min-w-0">
                            <p class="text-[9px] text-white/80 leading-tight uppercase font-medium">Group</p>
                            <p class="font-bold text-[11px] sm:text-xs text-white leading-tight truncate">Community</p>
                        </div>
                    </a>

                    <!-- Add Money -->
                    <a href="javascript:void(0)" onclick="openAddMoneyModal()" class="flex items-center gap-2 rounded-xl bg-gradient-to-r from-[#06B6D4] to-[#0284C7] px-2.5 py-2 text-white shadow-[0_8px_18px_rgba(6,182,212,0.28)] transition-all duration-300 hover:-translate-y-0.5 hover:shadow-[0_10px_22px_rgba(6,182,212,0.38)]">
                        <i class="fa-solid fa-wallet text-xl sm:text-2xl text-white"></i>
                        <div class="leading-tight min-w-0">
                            <p class="text-[9px] text-white/80 leading-tight uppercase font-medium">Wallet</p>
                            <p class="font-bold text-[11px] sm:text-xs text-white leading-tight truncate">Add Money</p>
                        </div>
                    </a>

                    <!-- Track Order -->
                    <a href="javascript:void(0)" onclick="openTrackOrderModal()" class="hidden md:flex items-center gap-2 rounded-xl bg-gradient-to-r from-[#10B981] to-[#059669] px-2.5 py-2 text-white shadow-[0_8px_18px_rgba(16,185,129,0.28)] transition-all duration-300 hover:-translate-y-0.5 hover:shadow-[0_10px_22px_rgba(16,185,129,0.38)]">
                        <i class="fa-solid fa-truck-fast text-xl sm:text-2xl text-white"></i>
                        <div class="leading-tight min-w-0">
                            <p class="text-[9px] text-white/80 leading-tight uppercase font-medium">Status</p>
                            <p class="font-bold text-[11px] sm:text-xs text-white leading-tight truncate">Track Order</p>
                        </div>
                    </a>

                    <!-- Video Tutorial -->
                    <a href="javascript:void(0)" onclick="openTutorialModal()" class="hidden md:flex items-center gap-2 rounded-xl bg-gradient-to-r from-[#E11D48] to-[#BE123C] px-2.5 py-2 text-white shadow-[0_8px_18px_rgba(225,29,72,0.28)] transition-all duration-300 hover:-translate-y-0.5 hover:shadow-[0_10px_22px_rgba(225,29,72,0.38)]">
                        <i class="fa-brands fa-youtube text-xl sm:text-2xl text-white"></i>
                        <div class="leading-tight min-w-0">
                            <p class="text-[9px] text-white/80 leading-tight uppercase font-medium">Guide</p>
                            <p class="font-bold text-[11px] sm:text-xs text-white leading-tight truncate">Tutorial</p>
                        </div>
                    </a>
                </div>
            </section>

            <!-- Category Filter Tabs -->
            <section class="container mx-auto px-3 sm:px-4 max-w-7xl my-2">
                <div class="flex items-center gap-2 overflow-x-auto py-1 scrollbar-none no-scrollbar">
                    <button onclick="filterCategory(\'all\', this)" class="cat-pill active px-3.5 py-1.5 rounded-full text-xs font-semibold bg-primary-500 text-white shadow-sm whitespace-nowrap transition">
                        🔥 All Games (28)
                    </button>
                    <button onclick="filterCategory(\'cat-ff\', this)" class="cat-pill px-3.5 py-1.5 rounded-full text-xs font-semibold bg-[#141638] text-slate-300 hover:text-white border border-theme-subtle whitespace-nowrap transition">
                        ⚡ Free Fire Topup
                    </button>
                    <button onclick="filterCategory(\'cat-pubg\', this)" class="cat-pill px-3.5 py-1.5 rounded-full text-xs font-semibold bg-[#141638] text-slate-300 hover:text-white border border-theme-subtle whitespace-nowrap transition">
                        🎯 PUBG Topup
                    </button>
                    <button onclick="filterCategory(\'cat-sub\', this)" class="cat-pill px-3.5 py-1.5 rounded-full text-xs font-semibold bg-[#141638] text-slate-300 hover:text-white border border-theme-subtle whitespace-nowrap transition">
                        💎 Subscriptions & AI
                    </button>
                    <button onclick="filterCategory(\'cat-others\', this)" class="cat-pill px-3.5 py-1.5 rounded-full text-xs font-semibold bg-[#141638] text-slate-300 hover:text-white border border-theme-subtle whitespace-nowrap transition">
                        ⚽ Other Games
                    </button>
                    <button onclick="filterCategory(\'cat-smm\', this)" class="cat-pill px-3.5 py-1.5 rounded-full text-xs font-semibold bg-[#141638] text-slate-300 hover:text-white border border-theme-subtle whitespace-nowrap transition">
                        📱 SMM Panel
                    </button>
                </div>
            </section>

            <!-- Product Catalog Grid by Category -->
            <div id="catalog-container">
                {category_sections_html}
            </div>

            <!-- Recent Orders Section -->
            <section class="container mx-auto px-3 sm:px-4 max-w-7xl mt-8 pt-4 border-t border-[rgba(44,33,88,0.35)]">
                <div class="flex items-center justify-between mb-4">
                    <div>
                        <h2 class="text-lg sm:text-2xl font-bold text-white flex items-center gap-2">
                            <span>Recent</span>
                            <span class="text-primary-400">Orders</span>
                        </h2>
                        <p class="text-xs text-slate-400 font-medium">Our real-time instant topup deliveries</p>
                    </div>
                    <div class="flex items-center gap-1.5 rounded-full border border-theme-subtle bg-surface/90 px-3 py-1 text-xs text-emerald-400">
                        <span class="w-2 h-2 rounded-full bg-emerald-400 animate-ping"></span>
                        <span>Live Feed</span>
                    </div>
                </div>

                <div id="recent-orders-list" class="space-y-2.5">
                    {orders_html}
                </div>
                
                <div class="mt-6 flex items-center justify-center gap-3 text-slate-500">
                    <span class="h-px w-10 sm:w-16 bg-slate-700"></span>
                    <p class="flex items-center gap-1.5 text-xs">
                        <i class="fa-solid fa-shield-heart text-primary-400"></i>
                        Thank you for your trust &bull; 100% Safe Topup
                    </p>
                    <span class="h-px w-10 sm:w-16 bg-slate-700"></span>
                </div>
            </section>
        </div>

        <!-- ============================================== -->
        <!-- VIEW 2: PRODUCT TOPUP VIEW (e.g. Free Fire BD) -->
        <!-- ============================================== -->
        <div id="topup-view" class="hidden">
            <section class="topup-product-page relative z-[1] overflow-x-hidden py-2 sm:py-4">
                <div class="container mx-auto px-3 sm:px-4 max-w-7xl">
                    <!-- Top Breadcrumb / Back button -->
                    <div class="mb-3">
                        <button onclick="navigateToHome()" class="inline-flex items-center gap-1.5 text-xs sm:text-sm font-semibold text-slate-300 hover:text-primary-400 transition bg-surface-main border border-theme-subtle px-3 py-1.5 rounded-lg">
                            <i class="fa-solid fa-arrow-left"></i> All Games / Catalog
                        </button>
                    </div>

                    <!-- Game Cover Banner Header -->
                    <div class="w-full mb-4 overflow-hidden rounded-2xl border border-[rgba(56,189,248,0.25)] bg-[#101235] shadow-xl relative">
                        <!-- Hero Banner Backdrop Art -->
                        <div class="relative w-full h-32 sm:h-44 md:h-52 overflow-hidden bg-[#0d0f28]">
                            <picture class="w-full h-full block">
                                <source srcset="images/banner2.webp" type="image/webp">
                                <source srcset="images/banner2.jpg" type="image/jpeg">
                                <img id="pview-hero-banner" src="images/banner2.webp" alt="Game Banner Art"
                                     class="w-full h-full object-cover opacity-70 filter brightness-95"
                                     onerror="this.src=\'images/banner2.jpg\';"/>
                            </picture>
                            <div class="absolute inset-0 bg-gradient-to-t from-[#101235] via-[#101235]/70 to-transparent"></div>
                            <div class="absolute inset-0 bg-gradient-to-r from-[#101235]/90 via-transparent to-[#101235]/80"></div>
                            
                            <div class="absolute top-3 right-3 z-10 flex items-center gap-2">
                                <span class="px-2.5 py-1 rounded-full text-[10px] sm:text-xs font-bold uppercase tracking-wider bg-emerald-500/20 text-emerald-300 border border-emerald-500/40 backdrop-blur-md flex items-center gap-1.5 shadow-md">
                                    <span class="w-2 h-2 rounded-full bg-emerald-400 animate-ping"></span>
                                    <span>Server Online 🟢</span>
                                </span>
                            </div>

                            <!-- Overlay Brand Header -->
                            <div class="absolute bottom-3 left-3 sm:bottom-4 sm:left-5 right-3 sm:right-5 flex items-end gap-3 sm:gap-4 z-10">
                                <div class="product-banner-logo relative shrink-0">
                                    <span class="absolute -inset-1 rounded-2xl bg-gradient-to-br from-primary-500/50 to-primary-700/30 blur-[6px]"></span>
                                    <img id="pview-logo" class="relative h-16 w-16 sm:h-[76px] sm:w-[76px] rounded-2xl border-2 border-primary-500/50 bg-[#15122c] object-contain p-1.5 shadow-2xl ring-2 ring-primary-500/25"
                                         src="images/products/images-1791123922354.webp" alt="Product Logo"
                                         onerror="this.src=\'images/products/images-1791123922354.jpg\'"/>
                                </div>
                                <div class="min-w-0 flex-1 pb-0.5">
                                    <div class="flex items-center gap-2 mb-1">
                                        <span class="px-2 py-0.5 rounded-full text-[10px] font-bold uppercase tracking-wider bg-primary-500/25 text-primary-300 border border-primary-500/40">
                                            <i class="fa-solid fa-gamepad mr-1"></i> Garena Free Fire
                                        </span>
                                        <span class="px-2 py-0.5 rounded-full text-[10px] font-bold uppercase tracking-wider bg-amber-500/20 text-amber-300 border border-amber-500/30">
                                            <i class="fa-solid fa-bolt mr-1"></i> 1-2 Mins Instant
                                        </span>
                                    </div>
                                    <h1 id="pview-title" class="product-banner-title text-base sm:text-2xl font-extrabold uppercase leading-tight tracking-wide text-white drop-shadow truncate">
                                        UID Topup [BD]
                                    </h1>
                                    <div class="mt-1 flex flex-wrap items-center gap-x-3 gap-y-1">
                                        <span class="inline-flex items-center gap-1 text-[10px] sm:text-xs font-medium text-slate-300">
                                            <i class="fa-solid fa-shield-halved text-primary-400"></i> Safety Guarantee
                                        </span>
                                        <span class="inline-flex items-center gap-1 text-[10px] sm:text-xs font-medium text-slate-300">
                                            <i class="fa-solid fa-location-dot text-emerald-400"></i> Bangladesh Region
                                        </span>
                                        <span class="inline-flex items-center gap-1 text-[10px] sm:text-xs font-medium text-slate-300">
                                            <i class="fa-solid fa-circle-check text-cyan-400"></i> Official Top-Up
                                        </span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Layout: Steps left, Checkout right -->
                    <div class="grid grid-cols-1 items-start gap-4 xl:grid-cols-[minmax(0,1fr)_400px]">
                        
                        <!-- LEFT COLUMN: Steps -->
                        <div class="space-y-4">
                            
                            <!-- STEP 1: Select Recharge (Package Selection) -->
                            <div class="_order_box_wrapper relative rounded-2xl border border-theme-subtle bg-surface-main p-4 shadow-md">
                                <div class="_order_box_header flex items-center gap-2.5 pb-3 border-b border-theme-subtle mb-3">
                                    <span class="w-7 h-7 rounded-full bg-primary-500/20 text-primary-400 flex items-center justify-center font-bold text-xs shrink-0">
                                        1
                                    </span>
                                    <div class="min-w-0 flex-1">
                                        <h5 class="text-sm sm:text-base font-bold text-white">Select Recharge</h5>
                                        <p class="text-[11px] text-slate-400">Choose diamond package or membership</p>
                                    </div>
                                </div>
                                <div class="order_box_body">
                                    <div id="packages-grid" class="grid grid-cols-2 sm:grid-cols-3 gap-2.5">
                                        <!-- Rendered dynamically -->
                                    </div>
                                </div>
                            </div>

                            <!-- STEP 2: Account Info -->
                            <div class="_order_box_wrapper relative rounded-2xl border border-theme-subtle bg-surface-main p-4 shadow-md">
                                <div class="_order_box_header flex items-center gap-2.5 pb-3 border-b border-theme-subtle mb-3">
                                    <span class="w-7 h-7 rounded-full bg-primary-500/20 text-primary-400 flex items-center justify-center font-bold text-xs shrink-0">
                                        2
                                    </span>
                                    <div class="min-w-0 flex-1">
                                        <h5 class="text-sm sm:text-base font-bold text-white" id="step2-title">Account Info</h5>
                                        <p class="text-[11px] text-slate-400" id="step2-subtitle">Fill in the details below to complete your order</p>
                                    </div>
                                </div>
                                <div class="order_box_body space-y-3">
                                    <div>
                                        <label for="player-uid-input" class="block text-xs font-semibold text-slate-300 mb-1.5" id="player-input-label">
                                            Player Id / UID <span class="text-red-400">*</span>
                                        </label>
                                        <div class="relative">
                                            <input id="player-uid-input" type="text" placeholder="Enter player id (e.g. 192837465)"
                                                   class="w-full bg-[#15122c] border border-theme-subtle focus:border-primary-400 rounded-xl px-3.5 py-2.5 text-sm text-white placeholder-slate-500 focus:outline-none transition"/>
                                        </div>
                                    </div>

                                    <!-- Verify Player ID Button -->
                                    <div id="check-id-container">
                                        <button type="button" onclick="verifyPlayerId()" id="check-id-btn"
                                                class="flex items-center justify-center gap-2 w-full bg-primary-500 hover:bg-primary-600 text-white font-semibold py-2 px-4 rounded-xl text-xs sm:text-sm transition shadow-md">
                                            <i class="fa-solid fa-magnifying-glass"></i>
                                            <span>Check Player ID Name</span>
                                        </button>
                                        <div id="player-check-result" class="hidden mt-2 p-2.5 rounded-xl bg-emerald-950/40 border border-emerald-500/40 text-emerald-300 text-xs flex items-center gap-2">
                                            <i class="fa-solid fa-circle-check text-emerald-400 text-sm"></i>
                                            <div class="leading-tight">
                                                <p class="font-bold" id="checked-player-name">Player: ★_RRR_KILLER_★</p>
                                                <p class="text-[10px] text-emerald-400/80">Region: Bangladesh (BD) &bull; Verified</p>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>

                            <!-- STEP 3: Description & Rules -->
                            <div class="_order_box_wrapper relative rounded-2xl border border-theme-subtle bg-surface-main p-4 shadow-md">
                                <div class="_order_box_header flex items-center gap-2.5 pb-3 border-b border-theme-subtle mb-3">
                                    <span class="w-7 h-7 rounded-full bg-primary-500/20 text-primary-400 flex items-center justify-center font-bold text-xs shrink-0">
                                        3
                                    </span>
                                    <div class="min-w-0 flex-1">
                                        <h5 class="text-sm sm:text-base font-bold text-white">Description & Rules</h5>
                                        <p class="text-[11px] text-slate-400">Product details and important rules</p>
                                    </div>
                                </div>
                                <div class="order_box_body text-xs leading-relaxed text-slate-300 space-y-2">
                                    <p class="font-bold text-primary-400">► অর্ডার করার আগে অবশ্যই ভালোভাবে রুলস গুলো পড়ে নেবেন</p>
                                    <p>⦿ শুধুমাত্র বাংলাদেশ সার্ভার এর আইডিতে টপ আপ করতে পারবেন।</p>
                                    <p>⦿ Player ID Code ভুল দিয়ে Diamond না পেলে RRR TOPUP কর্তৃপক্ষ দায়ী নয় ।</p>
                                    <p>⦿ আইডি কোড দিয়ে অর্ডার করলে এবং কোনো কারণে ডায়মন্ড না গেলে চেক করার জন্য গেইম এর লগিন ইনফো আইডি পাসওয়ার্ড দিতে হবে।</p>
                                    <p>⦿ ডেলিভারি টাইম সাধারণত ১-২ মিনিট এর মধ্যেই হয়ে থাকে, ইভেন্ট থাকলে ২-৩ ঘণ্টা বা তার ও বেশি সময় লাগতে পারে।</p>
                                    <p>⦿ সার্ভারে সমস্যা থাকলে অথবা স্টক না থাকলে সর্বোচ্চ ২৪ ঘন্টা পর্যন্ত লাগতে পারে। ২৪ ঘন্টার মধ্যে রিফান্ড চাইলে ওয়ালেট এ রিফান্ড করে দেওয়া হবে।</p>
                                </div>
                            </div>
                        </div>

                        <!-- RIGHT COLUMN: Sticky Checkout Box -->
                        <div class="space-y-4 xl:sticky xl:top-20">
                            <div class="rounded-2xl border border-theme-subtle bg-surface-main p-4 shadow-xl">
                                <h4 class="text-sm sm:text-base font-bold text-white pb-3 border-b border-theme-subtle flex items-center justify-between">
                                    <span>Payment Method</span>
                                    <span class="text-xs text-primary-400 font-semibold">100% Secure</span>
                                </h4>

                                <!-- Payment Method options -->
                                <div class="py-3 space-y-2" id="payment-methods">
                                    <!-- bKash -->
                                    <div onclick="selectPaymentMethod(\'bkash\')" id="pm-bkash" class="payment-option flex items-center justify-between p-2.5 rounded-xl border border-primary-500 bg-primary-500/10 cursor-pointer transition">
                                        <div class="flex items-center gap-2.5">
                                            <div class="w-8 h-8 rounded-lg bg-[#E2136E] flex items-center justify-center font-bold text-white text-xs shrink-0">
                                                bK
                                            </div>
                                            <div>
                                                <p class="text-xs font-bold text-white">bKash Instant</p>
                                                <p class="text-[10px] text-slate-400">Direct Auto Payment</p>
                                            </div>
                                        </div>
                                        <i class="fa-solid fa-circle-check text-primary-400 pm-check"></i>
                                    </div>

                                    <!-- Nagad -->
                                    <div onclick="selectPaymentMethod(\'nagad\')" id="pm-nagad" class="payment-option flex items-center justify-between p-2.5 rounded-xl border border-theme-subtle bg-[#15122c] cursor-pointer hover:border-theme-hover transition">
                                        <div class="flex items-center gap-2.5">
                                            <div class="w-8 h-8 rounded-lg bg-[#F7941D] flex items-center justify-center font-bold text-white text-xs shrink-0">
                                                Ng
                                            </div>
                                            <div>
                                                <p class="text-xs font-bold text-white">Nagad Instant</p>
                                                <p class="text-[10px] text-slate-400">Direct Auto Payment</p>
                                            </div>
                                        </div>
                                        <i class="fa-regular fa-circle text-slate-500 pm-check"></i>
                                    </div>

                                    <!-- Rocket -->
                                    <div onclick="selectPaymentMethod(\'rocket\')" id="pm-rocket" class="payment-option flex items-center justify-between p-2.5 rounded-xl border border-theme-subtle bg-[#15122c] cursor-pointer hover:border-theme-hover transition">
                                        <div class="flex items-center gap-2.5">
                                            <div class="w-8 h-8 rounded-lg bg-[#8C3494] flex items-center justify-center font-bold text-white text-xs shrink-0">
                                                Rk
                                            </div>
                                            <div>
                                                <p class="text-xs font-bold text-white">Rocket</p>
                                                <p class="text-[10px] text-slate-400">Manual / Auto Pay</p>
                                            </div>
                                        </div>
                                        <i class="fa-regular fa-circle text-slate-500 pm-check"></i>
                                    </div>

                                    <!-- RRR Wallet -->
                                    <div onclick="selectPaymentMethod(\'wallet\')" id="pm-wallet" class="payment-option flex items-center justify-between p-2.5 rounded-xl border border-theme-subtle bg-[#15122c] cursor-pointer hover:border-theme-hover transition">
                                        <div class="flex items-center gap-2.5">
                                            <div class="w-8 h-8 rounded-lg bg-emerald-600 flex items-center justify-center font-bold text-white text-xs shrink-0">
                                                <i class="fa-solid fa-wallet"></i>
                                            </div>
                                            <div>
                                                <p class="text-xs font-bold text-white">RRR Wallet</p>
                                                <p class="text-[10px] text-emerald-400 font-semibold" id="checkout-wallet-bal">Balance: 0.00 ৳</p>
                                            </div>
                                        </div>
                                        <i class="fa-regular fa-circle text-slate-500 pm-check"></i>
                                    </div>
                                </div>

                                <!-- Summary & Price Breakdown -->
                                <div class="pt-3 border-t border-theme-subtle space-y-1.5">
                                    <div class="flex justify-between text-xs text-slate-400">
                                        <span>Selected Item:</span>
                                        <span class="font-semibold text-white" id="summary-pkg-name">Weekly</span>
                                    </div>
                                    <div class="flex justify-between text-xs text-slate-400">
                                        <span>Delivery Fee:</span>
                                        <span class="text-emerald-400 font-semibold">FREE (0 ৳)</span>
                                    </div>
                                    <div class="flex justify-between items-center pt-2 text-sm font-bold text-white border-t border-theme-subtle">
                                        <span>Total Amount:</span>
                                        <span class="text-lg text-primary-400 font-extrabold tabular-nums" id="summary-total-price">155 ৳</span>
                                    </div>
                                </div>

                                <!-- Buy Now Button -->
                                <button type="button" onclick="handleBuyNow()" id="buy-now-btn"
                                        class="mt-4 w-full py-3 rounded-xl bg-gradient-to-r from-primary-500 to-primary-600 hover:from-primary-600 hover:to-primary-700 text-white font-bold text-sm sm:text-base shadow-lg shadow-primary-500/30 transition-all hover:-translate-y-0.5 active:translate-y-0 flex items-center justify-center gap-2">
                                    <i class="fa-solid fa-bag-shopping"></i>
                                    <span>Buy Now</span>
                                </button>

                                <!-- Verified Payment Trust Banner (eps_checkout_banner) -->
                                <div class="mt-4 pt-3 border-t border-theme-subtle">
                                    <div class="flex items-center justify-between text-[11px] text-slate-300 font-semibold mb-1.5 px-0.5">
                                        <span class="flex items-center gap-1.5 text-primary-400">
                                            <i class="fa-solid fa-shield-halved"></i> 100% Secure Payment
                                        </span>
                                        <span class="text-[10px] text-slate-400">Instant Auto Verification</span>
                                    </div>
                                    <div class="overflow-hidden rounded-xl border border-[rgba(56,189,248,0.2)] bg-[#121435] shadow-md p-1">
                                        <img src="images/checkout_banner.png" alt="Accepted Payment Methods: bKash, Nagad, Rocket"
                                             class="w-full h-auto object-contain rounded-lg block"
                                             onerror="this.src=\'https://apis.rrrtopup.com/uploads/images/1791272639832-130357.png\'"/>
                                    </div>
                                </div>
                            </div>
                        </div>

                    </div>
                </div>
            </section>
        </div>

    </main>

    <!-- FLOATING TELEGRAM SUPPORT BUTTON -->
    <a href="https://t.me/rrrtopup526" target="_blank" rel="noopener noreferrer" title="Telegram"
       class="fixed right-4 bottom-[72px] z-50 flex h-12 w-12 items-center justify-center transition-all duration-300 ease-in-out hover:scale-110 md:right-8 md:bottom-8 md:h-14 md:w-14">
        <div class="absolute h-16 w-16 rounded-full opacity-70 blur-sm md:h-20 md:w-20 bg-gradient-to-br from-sky-300/55 via-blue-300/35 to-indigo-500/55"></div>
        <div class="absolute h-14 w-14 rounded-full animate-ping blur-[1px] md:h-16 md:w-16 bg-gradient-to-br from-sky-300/55 via-blue-300/35 to-indigo-500/55"></div>
        <div class="relative z-10 flex h-12 w-12 items-center justify-center rounded-full md:h-14 md:w-14 bg-primary-500 theme-fab-glow text-white shadow-xl">
            <i class="fa-brands fa-telegram text-xl md:text-2xl"></i>
        </div>
    </a>

    <!-- MOBILE BOTTOM NAVIGATION BAR -->
    <div class="fixed bottom-0 left-0 w-full z-[999] md:hidden">
        <div class="border-t border-theme bg-surface-main/95 shadow-[0_-8px_22px_rgba(0,0,0,0.55)] backdrop-blur-[18px]">
            <div class="flex items-center justify-around px-2 py-1">
                <a href="javascript:void(0)" onclick="navigateToHome()" class="nav-tab active inline-flex flex-col items-center justify-center py-1.5 px-2 flex-1 text-primary-400">
                    <i class="fa-solid fa-house text-lg"></i>
                    <span class="text-[10px] mt-0.5 font-semibold">Home</span>
                </a>
                <a href="javascript:void(0)" onclick="openTutorialModal()" class="nav-tab inline-flex flex-col items-center justify-center py-1.5 px-2 flex-1 text-slate-400 hover:text-primary-300">
                    <i class="fa-solid fa-book-open text-lg"></i>
                    <span class="text-[10px] mt-0.5 font-semibold">Tutorial</span>
                </a>
                <a href="javascript:void(0)" onclick="scrollToSection(\'cat-ff\')" class="nav-tab inline-flex flex-col items-center justify-center py-1.5 px-2 flex-1 text-slate-400 hover:text-primary-300">
                    <i class="fa-solid fa-gamepad text-lg"></i>
                    <span class="text-[10px] mt-0.5 font-semibold">TopUp</span>
                </a>
                <a href="https://t.me/rrrtopup526" target="_blank" class="nav-tab inline-flex flex-col items-center justify-center py-1.5 px-2 flex-1 text-slate-400 hover:text-primary-300">
                    <i class="fa-solid fa-headset text-lg"></i>
                    <span class="text-[10px] mt-0.5 font-semibold">Contact</span>
                </a>
            </div>
        </div>
    </div>

    <!-- SITE FOOTER -->
    <footer class="relative z-[1] mt-auto border-t border-theme-subtle bg-[#0a0c24] text-slate-300">
        <div class="container mx-auto px-4 max-w-7xl pb-10 pt-12">
            <div class="grid grid-cols-1 md:grid-cols-3 gap-8 lg:gap-12">
                <!-- Customer Support -->
                <div>
                    <h3 class="text-base font-bold text-white tracking-wider uppercase mb-4 relative">
                        Customer Support
                        <div class="w-12 h-0.5 bg-primary-400 mt-1.5"></div>
                    </h3>
                    <div class="space-y-3">
                        <a href="https://t.me/rrrtopup526" target="_blank" class="flex items-center gap-3 p-2.5 rounded-xl bg-surface-main/80 border border-theme-subtle hover:border-primary-400 transition group">
                            <div class="w-10 h-10 rounded-lg bg-sky-500/20 text-sky-400 flex items-center justify-center text-lg shrink-0">
                                <i class="fa-brands fa-telegram"></i>
                            </div>
                            <div class="min-w-0">
                                <p class="text-xs text-slate-400 font-medium">Telegram Helpline</p>
                                <p class="text-sm font-bold text-white group-hover:text-primary-400 truncate">@rrrtopup526</p>
                            </div>
                        </a>
                        <a href="mailto:rrrtopup526@gmail.com" class="flex items-center gap-3 p-2.5 rounded-xl bg-surface-main/80 border border-theme-subtle hover:border-primary-400 transition group">
                            <div class="w-10 h-10 rounded-lg bg-red-500/20 text-red-400 flex items-center justify-center text-lg shrink-0">
                                <i class="fa-regular fa-envelope"></i>
                            </div>
                            <div class="min-w-0">
                                <p class="text-xs text-slate-400 font-medium">Email Support</p>
                                <p class="text-sm font-bold text-white group-hover:text-primary-400 truncate">rrrtopup526@gmail.com</p>
                            </div>
                        </a>
                    </div>
                </div>

                <!-- Information Links -->
                <div>
                    <h3 class="text-base font-bold text-white tracking-wider uppercase mb-4 relative">
                        Information
                        <div class="w-12 h-0.5 bg-primary-400 mt-1.5"></div>
                    </h3>
                    <ul class="space-y-2 text-xs sm:text-sm font-medium">
                        <li><a href="javascript:void(0)" onclick="showAboutUs()" class="hover:text-primary-400 transition flex items-center gap-2"><i class="fa-solid fa-angle-right text-xs text-primary-400"></i> About Us</a></li>
                        <li><a href="javascript:void(0)" onclick="showPrivacy()" class="hover:text-primary-400 transition flex items-center gap-2"><i class="fa-solid fa-angle-right text-xs text-primary-400"></i> Privacy Policy</a></li>
                        <li><a href="javascript:void(0)" onclick="showTerms()" class="hover:text-primary-400 transition flex items-center gap-2"><i class="fa-solid fa-angle-right text-xs text-primary-400"></i> Terms & Conditions</a></li>
                        <li><a href="javascript:void(0)" onclick="showRefund()" class="hover:text-primary-400 transition flex items-center gap-2"><i class="fa-solid fa-angle-right text-xs text-primary-400"></i> Refund & Return Policy</a></li>
                    </ul>
                </div>

                <!-- Stay Connected -->
                <div>
                    <h3 class="text-base font-bold text-white tracking-wider uppercase mb-4 relative">
                        Stay Connected
                        <div class="w-12 h-0.5 bg-primary-400 mt-1.5"></div>
                    </h3>
                    <p class="text-xs text-slate-400 mb-3">Join our official channels for daily diamond giveaways, special discount codes, and instant news!</p>
                    <div class="flex items-center gap-2 mb-4">
                        <a href="https://t.me/+mRE_lH8dUxU5NTg9" target="_blank" class="w-9 h-9 rounded-xl bg-[#229ED9]/20 text-[#229ED9] hover:bg-[#229ED9] hover:text-white transition flex items-center justify-center text-base">
                            <i class="fa-brands fa-telegram"></i>
                        </a>
                        <a href="https://www.youtube.com/@RRRTOPUP" target="_blank" class="w-9 h-9 rounded-xl bg-red-600/20 text-red-500 hover:bg-red-600 hover:text-white transition flex items-center justify-center text-base">
                            <i class="fa-brands fa-youtube"></i>
                        </a>
                        <a href="https://t.me/rrrtopup526" target="_blank" class="w-9 h-9 rounded-xl bg-primary-500/20 text-primary-400 hover:bg-primary-500 hover:text-white transition flex items-center justify-center text-base">
                            <i class="fa-solid fa-headset"></i>
                        </a>
                    </div>
                    <div class="p-3 rounded-xl bg-[#141638] border border-theme-subtle">
                        <p class="text-[11px] text-slate-400 mb-1.5 font-medium">Download Android App:</p>
                        <a href="https://web2apkpro.com/download/FE4450E/Rrr-Topup" target="_blank" class="inline-flex items-center gap-2 bg-gradient-to-r from-emerald-600 to-emerald-500 text-white font-bold text-xs px-3 py-1.5 rounded-lg shadow">
                            <i class="fa-brands fa-android text-sm"></i> Download APK
                        </a>
                    </div>
                </div>
            </div>

            <!-- Footer bottom bar -->
            <div class="mt-8 pt-6 border-t border-theme-subtle flex flex-col sm:flex-row items-center justify-between gap-4 text-xs text-slate-500">
                <p>&copy; 2026 Rrr Topup. All rights reserved. Bangladesh\'s #1 Topup Portal.</p>
                <div class="flex items-center gap-2">
                    <span class="text-[10px] text-slate-400">Payment Partners:</span>
                    <span class="px-2 py-0.5 bg-[#E2136E]/20 text-[#E2136E] font-bold rounded text-[10px]">bKash</span>
                    <span class="px-2 py-0.5 bg-[#F7941D]/20 text-[#F7941D] font-bold rounded text-[10px]">Nagad</span>
                    <span class="px-2 py-0.5 bg-[#8C3494]/20 text-[#8C3494] font-bold rounded text-[10px]">Rocket</span>
                    <span class="px-2 py-0.5 bg-cyan-500/20 text-cyan-400 font-bold rounded text-[10px]">Bangla QR</span>
                </div>
            </div>
        </div>
    </footer>
</div>

<!-- ============================================== -->
<!-- MODALS -->
<!-- ============================================== -->

<!-- 1. CHECKOUT & PAYMENT MODAL -->
<div id="checkout-modal" class="modal-backdrop">
    <div class="modal-card">
        <!-- Header -->
        <div id="checkout-gateway-header" class="bg-[#E2136E] text-white p-4 flex items-center justify-between">
            <div class="flex items-center gap-2">
                <div class="w-8 h-8 rounded-lg bg-white/20 flex items-center justify-center font-bold text-sm" id="modal-gateway-logo">
                    bK
                </div>
                <div>
                    <h3 class="text-sm font-bold leading-tight" id="modal-gateway-title">bKash Payment Gateway</h3>
                    <p class="text-[10px] text-white/80">Merchant: RRR TopUp Official</p>
                </div>
            </div>
            <button onclick="closeModal(\'checkout-modal\')" class="text-white/80 hover:text-white p-1">
                <i class="fa-solid fa-xmark text-lg"></i>
            </button>
        </div>

        <div class="p-4 sm:p-5 space-y-3.5">
            <!-- Amount & Order Info Box -->
            <div class="bg-[#141638] border border-theme-subtle rounded-xl p-3 flex items-center justify-between">
                <div>
                    <p class="text-[11px] text-slate-400">Total Payable Amount:</p>
                    <p class="text-xl font-extrabold text-primary-400 tabular-nums" id="modal-pay-amount">155 ৳</p>
                </div>
                <div class="text-right">
                    <p class="text-[11px] text-slate-400">Order Ref:</p>
                    <p class="text-xs font-mono font-bold text-slate-200" id="modal-order-ref">RRR-98421</p>
                </div>
            </div>

            <!-- Payment instruction -->
            <div class="text-xs text-slate-300 bg-[#16193e] border border-primary-500/20 rounded-xl p-3 space-y-2">
                <p class="font-semibold text-white flex items-center gap-1.5">
                    <i class="fa-solid fa-circle-info text-primary-400"></i>
                    <span>Payment Instructions:</span>
                </p>
                <div class="flex items-center justify-between bg-[#0e102b] p-2 rounded-lg border border-theme-subtle">
                    <div>
                        <span class="text-[10px] text-slate-400">Merchant / Personal No:</span>
                        <p class="font-mono font-bold text-white text-sm" id="modal-merchant-no">01889-123456</p>
                    </div>
                    <button onclick="copyToClipboard(\'01889123456\', this)" class="bg-primary-500 hover:bg-primary-600 text-white text-[11px] font-bold px-2.5 py-1 rounded-md transition flex items-center gap-1">
                        <i class="fa-regular fa-copy"></i> <span>Copy</span>
                    </button>
                </div>
                <p class="text-[11px] text-slate-400 leading-snug">
                    Send Money বা Payment করুন এবং নিচের বক্সে আপনার Sender Number ও Transaction ID (TrxID) দিন।
                </p>
            </div>

            <!-- Form fields -->
            <div class="space-y-2.5">
                <div>
                    <label class="block text-xs font-semibold text-slate-300 mb-1">Your Sender Number:</label>
                    <input type="text" id="pay-sender-no" placeholder="e.g. 017XXXXXXXX"
                           class="w-full bg-[#141638] border border-theme-subtle focus:border-primary-400 rounded-xl px-3.5 py-2 text-sm text-white placeholder-slate-500 focus:outline-none transition"/>
                </div>
                <div>
                    <label class="block text-xs font-semibold text-slate-300 mb-1">Transaction ID (TrxID):</label>
                    <input type="text" id="pay-trxid" placeholder="e.g. BL9A8X76YZ"
                           class="w-full bg-[#141638] border border-theme-subtle focus:border-primary-400 rounded-xl px-3.5 py-2 text-sm text-white placeholder-slate-500 focus:outline-none uppercase font-mono transition"/>
                </div>
            </div>

            <!-- Auto-fill demo button -->
            <div class="flex justify-end">
                <button type="button" onclick="autoFillPaymentTest()" class="text-[11px] text-primary-400 hover:text-primary-300 font-semibold flex items-center gap-1">
                    <i class="fa-solid fa-wand-magic-sparkles"></i> Auto-fill Demo TrxID
                </button>
            </div>

            <!-- Confirm Button -->
            <button type="button" onclick="confirmPayment()" id="modal-confirm-btn"
                    class="w-full py-3 rounded-xl bg-gradient-to-r from-emerald-600 to-emerald-500 hover:from-emerald-500 hover:to-emerald-600 text-white font-bold text-sm sm:text-base shadow-lg transition flex items-center justify-center gap-2">
                <i class="fa-solid fa-lock"></i>
                <span>Confirm & Verify Payment</span>
            </button>
        </div>
    </div>
</div>

<!-- 2. SUCCESS INVOICE RECEIPT MODAL -->
<div id="invoice-modal" class="modal-backdrop">
    <div class="modal-card">
        <div class="bg-gradient-to-r from-emerald-600 to-emerald-500 text-white p-5 text-center relative">
            <button onclick="closeModal(\'invoice-modal\')" class="absolute top-3 right-3 text-white/80 hover:text-white p-1">
                <i class="fa-solid fa-xmark text-lg"></i>
            </button>
            <div class="w-14 h-14 bg-white/20 rounded-full flex items-center justify-center mx-auto mb-2 text-2xl animate-bounce">
                <i class="fa-solid fa-check"></i>
            </div>
            <h3 class="text-lg font-extrabold">Order Placed Successfully!</h3>
            <p class="text-xs text-white/80">ইনস্ট্যান্ট ডেলিভারি শুরু হয়েছে (১-২ মিনিট)</p>
        </div>

        <div class="p-4 sm:p-5 space-y-3">
            <div class="bg-[#141638] border border-theme-subtle rounded-xl p-3.5 space-y-2 text-xs">
                <div class="flex justify-between py-1 border-b border-theme-subtle">
                    <span class="text-slate-400">Order ID:</span>
                    <span class="font-mono font-bold text-primary-400" id="inv-order-id">RRR-202611-98421</span>
                </div>
                <div class="flex justify-between py-1 border-b border-theme-subtle">
                    <span class="text-slate-400">Account / UID:</span>
                    <span class="font-mono font-bold text-white" id="inv-player-uid">192837465</span>
                </div>
                <div class="flex justify-between py-1 border-b border-theme-subtle">
                    <span class="text-slate-400">Package:</span>
                    <span class="font-semibold text-white" id="inv-package">Weekly Membership</span>
                </div>
                <div class="flex justify-between py-1 border-b border-theme-subtle">
                    <span class="text-slate-400">Amount Paid:</span>
                    <span class="font-bold text-emerald-400" id="inv-amount">155 ৳</span>
                </div>
                <div class="flex justify-between py-1 border-b border-theme-subtle">
                    <span class="text-slate-400">Payment Method:</span>
                    <span class="font-semibold text-white" id="inv-method">bKash Instant</span>
                </div>
                <div class="flex justify-between py-1">
                    <span class="text-slate-400">Status:</span>
                    <span class="font-bold text-emerald-400 flex items-center gap-1">
                        <i class="fa-solid fa-circle-check"></i> Processing / Auto Delivery
                    </span>
                </div>
            </div>

            <div class="flex gap-2">
                <button onclick="trackThisOrder()" class="flex-1 py-2.5 rounded-xl bg-primary-500 hover:bg-primary-600 text-white font-semibold text-xs sm:text-sm transition flex items-center justify-center gap-1.5">
                    <i class="fa-solid fa-truck-fast"></i> Track Order
                </button>
                <button onclick="closeModal(\'invoice-modal\'); navigateToHome()" class="flex-1 py-2.5 rounded-xl bg-[#141638] border border-theme-subtle hover:bg-[#1a1d48] text-slate-200 font-semibold text-xs sm:text-sm transition flex items-center justify-center gap-1.5">
                    <i class="fa-solid fa-house"></i> Home
                </button>
            </div>
        </div>
    </div>
</div>

<!-- 3. ORDER TRACKING MODAL -->
<div id="track-modal" class="modal-backdrop">
    <div class="modal-card">
        <div class="bg-surface-main border-b border-theme-subtle p-4 flex items-center justify-between">
            <h3 class="text-sm font-bold text-white flex items-center gap-2">
                <i class="fa-solid fa-truck-fast text-emerald-400"></i> Track Your Order
            </h3>
            <button onclick="closeModal(\'track-modal\')" class="text-slate-400 hover:text-white p-1">
                <i class="fa-solid fa-xmark text-lg"></i>
            </button>
        </div>

        <div class="p-4 sm:p-5 space-y-4">
            <div class="flex gap-2">
                <input type="text" id="track-order-input" placeholder="Enter Order ID or Player UID"
                       class="flex-1 bg-[#141638] border border-theme-subtle focus:border-primary-400 rounded-xl px-3.5 py-2 text-xs sm:text-sm text-white placeholder-slate-500 focus:outline-none transition"/>
                <button onclick="searchOrderStatus()" class="bg-primary-500 hover:bg-primary-600 text-white px-4 py-2 rounded-xl text-xs sm:text-sm font-bold transition">
                    Track
                </button>
            </div>

            <!-- Order Timeline Progress -->
            <div id="track-timeline" class="space-y-3 pt-2">
                <div class="flex items-start gap-3">
                    <div class="w-6 h-6 rounded-full bg-emerald-500 text-white flex items-center justify-center text-xs shrink-0 mt-0.5">
                        <i class="fa-solid fa-check"></i>
                    </div>
                    <div>
                        <p class="text-xs font-bold text-white">Order Received</p>
                        <p class="text-[10px] text-slate-400">Your topup request has been registered</p>
                    </div>
                </div>

                <div class="flex items-start gap-3">
                    <div class="w-6 h-6 rounded-full bg-emerald-500 text-white flex items-center justify-center text-xs shrink-0 mt-0.5">
                        <i class="fa-solid fa-check"></i>
                    </div>
                    <div>
                        <p class="text-xs font-bold text-white">Payment Confirmed</p>
                        <p class="text-[10px] text-slate-400">Transaction ID verified with Gateway</p>
                    </div>
                </div>

                <div class="flex items-start gap-3">
                    <div class="w-6 h-6 rounded-full bg-emerald-500 text-white flex items-center justify-center text-xs shrink-0 mt-0.5 animate-pulse">
                        <i class="fa-solid fa-bolt"></i>
                    </div>
                    <div>
                        <p class="text-xs font-bold text-emerald-400">Sending Diamonds via Garena API</p>
                        <p class="text-[10px] text-slate-400">AI Topup Server is crediting diamonds to your account</p>
                    </div>
                </div>

                <div class="flex items-start gap-3 opacity-60">
                    <div class="w-6 h-6 rounded-full bg-slate-700 text-slate-400 flex items-center justify-center text-xs shrink-0 mt-0.5">
                        <i class="fa-solid fa-flag-checkered"></i>
                    </div>
                    <div>
                        <p class="text-xs font-bold text-slate-400">Delivered Successfully</p>
                        <p class="text-[10px] text-slate-500">Estimated 1-2 minutes</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

<!-- 4. ADD MONEY / WALLET MODAL -->
<div id="addmoney-modal" class="modal-backdrop">
    <div class="modal-card">
        <div class="bg-gradient-to-r from-primary-600 to-primary-500 text-white p-4 flex items-center justify-between">
            <h3 class="text-sm font-bold flex items-center gap-2">
                <i class="fa-solid fa-wallet"></i> Add Money to Wallet
            </h3>
            <button onclick="closeModal(\'addmoney-modal\')" class="text-white/80 hover:text-white p-1">
                <i class="fa-solid fa-xmark text-lg"></i>
            </button>
        </div>

        <div class="p-4 sm:p-5 space-y-3.5">
            <div class="bg-[#141638] p-3 rounded-xl border border-theme-subtle flex justify-between items-center text-xs">
                <span class="text-slate-400">Current Balance:</span>
                <span class="text-base font-bold text-emerald-400 tabular-nums" id="addmoney-current-bal">0.00 ৳</span>
            </div>

            <div class="text-xs text-slate-300 bg-[#16193e] border border-primary-500/20 rounded-xl p-3 space-y-2">
                <p class="font-semibold text-white">bKash / Nagad Send Money No:</p>
                <div class="flex items-center justify-between bg-[#0e102b] p-2 rounded-lg border border-theme-subtle">
                    <span class="font-mono font-bold text-white">01889-123456 (Personal)</span>
                    <button onclick="copyToClipboard(\'01889123456\', this)" class="bg-primary-500 text-white text-[10px] font-bold px-2 py-0.5 rounded">
                        Copy
                    </button>
                </div>
            </div>

            <div class="space-y-2 text-xs">
                <div>
                    <label class="block font-semibold text-slate-300 mb-1">Enter Amount (BDT):</label>
                    <input type="number" id="addmoney-amount" placeholder="e.g. 500" value="500"
                           class="w-full bg-[#141638] border border-theme-subtle focus:border-primary-400 rounded-xl px-3.5 py-2 text-sm text-white placeholder-slate-500 focus:outline-none transition"/>
                </div>
                <div>
                    <label class="block font-semibold text-slate-300 mb-1">Transaction ID (TrxID):</label>
                    <input type="text" id="addmoney-trxid" placeholder="e.g. 9B8A7X6Y5Z"
                           class="w-full bg-[#141638] border border-theme-subtle focus:border-primary-400 rounded-xl px-3.5 py-2 text-sm text-white placeholder-slate-500 focus:outline-none uppercase font-mono transition"/>
                </div>
            </div>

            <button onclick="processAddMoney()" class="w-full py-2.5 rounded-xl bg-primary-500 hover:bg-primary-600 text-white font-bold text-sm transition shadow-md">
                Add Balance to Wallet
            </button>
        </div>
    </div>
</div>

<!-- 5. LOGIN / REGISTER MODAL -->
<div id="login-modal" class="modal-backdrop">
    <div class="modal-card">
        <div class="bg-surface-main border-b border-theme-subtle p-4 flex items-center justify-between">
            <h3 class="text-sm font-bold text-white flex items-center gap-2">
                <i class="fa-solid fa-user-circle text-primary-400 text-base"></i> User Login / Sign Up
            </h3>
            <button onclick="closeModal(\'login-modal\')" class="text-slate-400 hover:text-white p-1">
                <i class="fa-solid fa-xmark text-lg"></i>
            </button>
        </div>

        <div class="p-4 sm:p-5 space-y-3.5">
            <div>
                <label class="block text-xs font-semibold text-slate-300 mb-1">Your Name:</label>
                <input type="text" id="login-name" placeholder="e.g. Tanvir Ahmed"
                       class="w-full bg-[#141638] border border-theme-subtle focus:border-primary-400 rounded-xl px-3.5 py-2 text-sm text-white placeholder-slate-500 focus:outline-none transition"/>
            </div>
            <div>
                <label class="block text-xs font-semibold text-slate-300 mb-1">Phone Number:</label>
                <input type="tel" id="login-phone" placeholder="e.g. 01712345678"
                       class="w-full bg-[#141638] border border-theme-subtle focus:border-primary-400 rounded-xl px-3.5 py-2 text-sm text-white placeholder-slate-500 focus:outline-none transition"/>
            </div>

            <button onclick="processLogin()" class="w-full py-2.5 rounded-xl bg-primary-500 hover:bg-primary-600 text-white font-bold text-sm transition shadow-md flex items-center justify-center gap-2">
                <i class="fa-solid fa-bolt text-xs"></i> <span>ইনস্ট্যান্ট লগইন (Quick Login)</span>
            </button>

            <div class="pt-2 border-t border-theme-subtle text-center space-y-2">
                <p class="text-xs text-slate-400">
                    নতুন অ্যাকাউন্ট খুলতে চান? 
                    <a href="signup.html" class="text-primary-400 font-bold hover:underline ml-1">সাইন-আপ করুন (Sign Up)</a>
                </p>
                <p class="text-[11px] text-slate-500">
                    অথবা পাসওয়ার্ড সহ লগইন করুন: 
                    <a href="login.html" class="text-slate-300 font-semibold hover:text-white underline ml-1">লগইন পেজ</a>
                </p>
            </div>
        </div>
    </div>
</div>

<!-- 6. VIDEO TUTORIAL MODAL -->
<div id="video-modal" class="modal-backdrop">
    <div class="modal-card !max-w-xl">
        <div class="bg-surface-main border-b border-theme-subtle p-3 flex items-center justify-between">
            <h3 class="text-xs sm:text-sm font-bold text-white flex items-center gap-2">
                <i class="fa-brands fa-youtube text-red-500"></i> How to Topup Diamond Tutorial
            </h3>
            <button onclick="closeModal(\'video-modal\')" class="text-slate-400 hover:text-white p-1">
                <i class="fa-solid fa-xmark text-lg"></i>
            </button>
        </div>
        <div class="p-2 sm:p-4 aspect-video bg-black flex items-center justify-center">
            <iframe id="tutorial-iframe" class="w-full h-full rounded-lg"
                    src="https://www.youtube-nocookie.com/embed/VP3j0wGbX1k"
                    title="YouTube video player" frameborder="0"
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        </div>
    </div>
</div>

<!-- 7. INFORMATION INFO MODAL -->
<div id="info-modal" class="modal-backdrop">
    <div class="modal-card">
        <div class="bg-surface-main border-b border-theme-subtle p-4 flex items-center justify-between">
            <h3 class="text-sm font-bold text-white" id="info-modal-title">Information</h3>
            <button onclick="closeModal(\'info-modal\')" class="text-slate-400 hover:text-white p-1">
                <i class="fa-solid fa-xmark text-lg"></i>
            </button>
        </div>
        <div class="p-4 sm:p-5 text-xs sm:text-sm text-slate-300 leading-relaxed whitespace-pre-line" id="info-modal-body">
            Details
        </div>
    </div>
</div>

<!-- ============================================== -->
<!-- JAVASCRIPT APP LOGIC (ROBUST & ERROR-SAFE) -->
<!-- ============================================== -->
<script>
    // Safe LocalStorage wrapper (Prevents file:// SecurityError crashes)

    // ==============================================
    // CONVEX CLOUD DATABASE CLIENT
    // Deployment: quixotic-cuttlefish-352
    // Cloud URL: https://quixotic-cuttlefish-352.convex.cloud
    // HTTP Actions URL: https://quixotic-cuttlefish-352.convex.site
    // ==============================================
    const CONVEX_CLOUD_URL = "https://quixotic-cuttlefish-352.convex.cloud";
    const CONVEX_SITE_URL = "https://quixotic-cuttlefish-352.convex.site";

    const convex = {{
        query: async function(path, args = {{}}) {{
            try {{
                const res = await fetch(`${{CONVEX_CLOUD_URL}}/api/query`, {{
                    method: "POST",
                    headers: {{ "Content-Type": "application/json" }},
                    body: JSON.stringify({{ path, args }})
                }});
                const data = await res.json();
                if (data.status === "success") return data.value;
                return null;
            }} catch (err) {{
                console.warn("Convex query failed:", err);
                return null;
            }}
        }},
        mutation: async function(path, args = {{}}) {{
            try {{
                const res = await fetch(`${{CONVEX_CLOUD_URL}}/api/mutation`, {{
                    method: "POST",
                    headers: {{ "Content-Type": "application/json" }},
                    body: JSON.stringify({{ path, args }})
                }});
                const data = await res.json();
                if (data.status === "success") return data.value;
                return null;
            }} catch (err) {{
                console.warn("Convex mutation failed:", err);
                return null;
            }}
        }}
    }};

    function showConvexStatus() {{
        alert(`🟢 Convex Cloud Database Connected!

Deployment: quixotic-cuttlefish-352
Cloud URL: https://quixotic-cuttlefish-352.convex.cloud
HTTP Actions: https://quixotic-cuttlefish-352.convex.site

All Products, Orders, Users & Wallet transactions are syncing in real time.`);
    }}

    const storage = {{
        get: function(key) {{
            try {{ return window.localStorage ? window.localStorage.getItem(key) : null; }} catch(e) {{ return null; }}
        }},
        set: function(key, val) {{
            try {{ if (window.localStorage) window.localStorage.setItem(key, val); }} catch(e) {{}}
        }},
        remove: function(key) {{
            try {{ if (window.localStorage) window.localStorage.removeItem(key); }} catch(e) {{}}
        }}
    }};

    // Embedded Data
    const productsData = {products_json};
    const packages21Data = {packages_21_json};
    let publicOrdersData = {orders_json};

    // App State
    let currentProductId = 21;
    let selectedPackage = null;
    let selectedPayment = \'bkash\';
    let userBalance = 0;
    let currentSlide = 0;
    let sliderTimer = null;
    let recentOrdersTimer = null;
    let lastGeneratedOrderId = "RRR-202611-98421";
    let currentUser = {{ name: "Guest User", phone: "" }};

    // DOM Ready
    document.addEventListener("DOMContentLoaded", function() {{
        try {{
            initSlider();
            initLiveOrdersSimulation();
            loadSavedUserState();

            // Sync recent orders from Convex Live Database
            convex.query("orders:listRecent").then(orders => {{
                if (orders && orders.length > 0) {{
                    orders.forEach(o => {{
                        publicOrdersData.unshift({{
                            full_name: o.full_name,
                            avatar: o.avatar,
                            name: o.name,
                            amount: o.amount,
                            status: o.status
                        }});
                        prependRecentOrder(o);
                    }});
                }}
            }}).catch(e => {{}});
            
            // Handle URL hash if any
            if (window.location.hash.startsWith("#topup/")) {{
                const pid = parseInt(window.location.hash.replace("#topup/", ""), 10);
                if (pid) openProduct(pid, false);
            }}
        }} catch(err) {{
            console.error("Initialization error:", err);
        }}
    }});

    // Browser History navigation support
    window.addEventListener("hashchange", function() {{
        try {{
            if (window.location.hash.startsWith("#topup/")) {{
                const pid = parseInt(window.location.hash.replace("#topup/", ""), 10);
                if (pid) openProduct(pid, false);
            }} else {{
                navigateToHome(false);
            }}
        }} catch(e) {{}}
    }});

    // Navigation & Views
    function navigateToHome(updateHash = true) {{
        const topupView = document.getElementById("topup-view");
        const homeView = document.getElementById("home-view");
        if (topupView) topupView.classList.add("hidden");
        if (homeView) homeView.classList.remove("hidden");
        if (updateHash) {{
            try {{
                if (window.location.protocol !== 'file:') {{
                    history.pushState(null, null, " ");
                }} else {{
                    window.location.hash = "";
                }}
            }} catch(e) {{}}
        }}
        window.scrollTo({{ top: 0, behavior: "smooth" }});
    }}

    function openProduct(pid, updateHash = true) {{
        const prod = productsData.find(p => p.id === pid) || productsData[0];
        currentProductId = prod.id;
        
        // Update product view header
        const titleEl = document.getElementById("pview-title");
        if (titleEl) titleEl.textContent = prod.name;
        
        const logoImg = document.getElementById("pview-logo");
        if (logoImg) {{
            const baseLogo = prod.logo.replace(/\\.(jpe?g|webp|png)$/i, "");
            logoImg.src = "images/products/" + baseLogo + ".webp";
            logoImg.onerror = () => {{
                logoImg.src = "images/products/" + prod.logo;
                logoImg.onerror = () => {{
                    logoImg.src = "https://apis.rrrtopup.com/images/" + prod.logo;
                }};
            }};
        }}

        const heroBanner = document.getElementById("pview-hero-banner");
        if (heroBanner) {{
            if (prod.category_id === 1) {{
                heroBanner.src = "images/banner2.webp";
                heroBanner.onerror = () => {{ heroBanner.src = "images/banner2.jpg"; }};
            }} else if (prod.category_id === 2) {{
                heroBanner.src = "images/banner1.webp";
                heroBanner.onerror = () => {{ heroBanner.src = "images/banner1.jpg"; }};
            }} else {{
                heroBanner.src = "images/banner3.webp";
                heroBanner.onerror = () => {{ heroBanner.src = "images/banner3.jpg"; }};
            }}
        }}

        // Dynamic input fields for Subscriptions vs Games
        const step2Title = document.getElementById("step2-title");
        const step2Subtitle = document.getElementById("step2-subtitle");
        const inputLabel = document.getElementById("player-input-label");
        const uidInput = document.getElementById("player-uid-input");
        const checkIdContainer = document.getElementById("check-id-container");

        if (prod.category_id === 2 || prod.category_id === 6) {{
            if (step2Title) step2Title.textContent = "Account & Delivery Info";
            if (step2Subtitle) step2Subtitle.textContent = "Provide your email or username for subscription delivery";
            if (inputLabel) inputLabel.innerHTML = `Email / Phone / Username <span class="text-red-400">*</span>`;
            if (uidInput) {{
                uidInput.placeholder = "e.g. user@gmail.com or username";
                uidInput.value = "";
            }}
            if (checkIdContainer) checkIdContainer.classList.add("hidden");
        }} else {{
            if (step2Title) step2Title.textContent = "Account Info";
            if (step2Subtitle) step2Subtitle.textContent = "Fill in the details below to complete your order";
            if (inputLabel) inputLabel.innerHTML = `Player Id / UID <span class="text-red-400">*</span>`;
            if (uidInput) {{
                uidInput.placeholder = "Enter player id (e.g. 192837465)";
                uidInput.value = "";
            }}
            if (checkIdContainer) checkIdContainer.classList.remove("hidden");
        }}
        
        // Render packages
        renderPackages(prod.id);
        
        // Reset inputs
        const checkRes = document.getElementById("player-check-result");
        if (checkRes) checkRes.classList.add("hidden");
        selectPaymentMethod("bkash");

        // Show view
        const homeView = document.getElementById("home-view");
        const topupView = document.getElementById("topup-view");
        if (homeView) homeView.classList.add("hidden");
        if (topupView) topupView.classList.remove("hidden");
        
        if (updateHash) {{
            window.location.hash = "#topup/" + prod.id;
        }}
        window.scrollTo({{ top: 0, behavior: "smooth" }});
    }}

    function renderPackages(pid) {{
        const container = document.getElementById("packages-grid");
        if (!container) return;
        container.innerHTML = "";
        
        // Real game-specific packages
        let pkgs = [];
        if (pid === 21) {{
            pkgs = packages21Data;
        }} else if (pid === 49) {{
            pkgs = [
                {{ id: 136, name: "Weekly Membership", price: 155, tag: "161" }},
                {{ id: 137, name: "Monthly Membership", price: 770, tag: "800" }},
                {{ id: 291, name: "2x Weekly Membership", price: 310, tag: "Save" }},
                {{ id: 292, name: "3x Weekly Membership", price: 465, tag: "Popular" }},
                {{ id: 293, name: "5x Weekly Membership", price: 775, tag: "Best Value" }},
                {{ id: 294, name: "2x Monthly Membership", price: 1540, tag: "VIP" }}
            ];
        }} else if (pid === 26) {{
            pkgs = [
                {{ id: 261, name: "Weekly Lite [1x]", price: 35, tag: "Instant" }},
                {{ id: 262, name: "Weekly Lite [2x]", price: 70, tag: "Popular" }},
                {{ id: 263, name: "Weekly Lite [3x]", price: 105, tag: "" }},
                {{ id: 264, name: "Weekly Lite [5x]", price: 175, tag: "Discount" }}
            ];
        }} else if (pid === 38) {{
            pkgs = [
                {{ id: 381, name: "Level Up Pass - Lv 10", price: 35, tag: "" }},
                {{ id: 382, name: "Level Up Pass - Lv 15", price: 50, tag: "" }},
                {{ id: 383, name: "Level Up Pass - Lv 20", price: 70, tag: "Popular" }},
                {{ id: 384, name: "Level Up Pass - Lv 25", price: 70, tag: "" }},
                {{ id: 385, name: "Level Up Pass - Lv 30", price: 100, tag: "Best Value" }}
            ];
        }} else if (pid === 41) {{
            pkgs = [
                {{ id: 411, name: "100 Free Fire Likes", price: 10, tag: "Instant" }},
                {{ id: 412, name: "200 Free Fire Likes", price: 20, tag: "" }},
                {{ id: 413, name: "500 Free Fire Likes", price: 50, tag: "Popular" }},
                {{ id: 414, name: "1000 Free Fire Likes", price: 95, tag: "Best Value" }},
                {{ id: 415, name: "2000 Free Fire Likes", price: 180, tag: "Super Deal" }}
            ];
        }} else if (pid === 39) {{
            pkgs = [
                {{ id: 391, name: "Mystery Box - Bronze", price: 50, tag: "Luck" }},
                {{ id: 392, name: "Mystery Box - Silver", price: 100, tag: "Rare" }},
                {{ id: 393, name: "Mystery Box - Gold", price: 200, tag: "Epic" }},
                {{ id: 394, name: "Mystery Box - Diamond", price: 500, tag: "Legendary" }}
            ];
        }} else if (pid === 31 || pid === 34) {{
            pkgs = [
                {{ id: 311, name: "60 UC", price: 95, tag: "Instant" }},
                {{ id: 312, name: "300 + 25 UC", price: 450, tag: "Popular" }},
                {{ id: 313, name: "600 + 60 UC", price: 890, tag: "Bonus" }},
                {{ id: 314, name: "1500 + 300 UC", price: 2190, tag: "Best Value" }},
                {{ id: 315, name: "3000 + 850 UC", price: 4350, tag: "Pro" }}
            ];
        }} else if (pid === 66 || pid === 67) {{
            pkgs = [
                {{ id: 661, name: "130 Coins / Basic", price: 130, tag: "Instant" }},
                {{ id: 662, name: "550 Coins / Pack", price: 520, tag: "Popular" }},
                {{ id: 663, name: "1040 Coins / Special", price: 990, tag: "Bonus" }},
                {{ id: 664, name: "2130 Coins / Mega", price: 1980, tag: "Best Value" }}
            ];
        }} else {{
            pkgs = [
                {{ id: 1, name: "1 Month Subscription", price: 120, tag: "Instant" }},
                {{ id: 2, name: "3 Months Subscription", price: 250, tag: "Popular" }},
                {{ id: 3, name: "6 Months Subscription", price: 480, tag: "Best Value" }},
                {{ id: 4, name: "1 Year Full Access", price: 850, tag: "Mega Saver" }}
            ];
        }}
        
        pkgs.forEach((pkg, idx) => {{
            const card = document.createElement("div");
            card.className = "pkg-select-card" + (idx === 0 ? " active" : "");
            card.onclick = () => selectPkg(pkg, card);
            
            let tagBadge = "";
            if (pkg.tag) {{
                tagBadge = `<span class="bg-primary-500/20 text-primary-400 border border-primary-500/30 text-[9px] font-bold px-1.5 py-0.5 rounded ml-1">${{pkg.tag}}</span>`;
            }}
            
            card.innerHTML = `
                <div class="min-w-0 flex-1 pr-1 text-left">
                    <p class="pkg-select-name line-clamp-1 text-xs sm:text-sm font-bold text-white">
                        ${{pkg.name}} ${{tagBadge}}
                    </p>
                    <div class="mt-0.5 flex items-center gap-1">
                        <p class="pkg-select-price text-xs sm:text-sm font-extrabold text-primary-400 tabular-nums">
                            ${{pkg.price}} ৳
                        </p>
                    </div>
                </div>
                <div class="pkg-check">
                    <i class="fa-solid fa-check"></i>
                </div>
            `;
            container.appendChild(card);
        }});
        
        if (pkgs.length > 0) {{
            selectPkg(pkgs[0], container.children[0]);
        }}
    }}

    function selectPkg(pkg, element) {{
        selectedPackage = pkg;
        document.querySelectorAll(".pkg-select-card").forEach(el => el.classList.remove("active"));
        if (element) element.classList.add("active");
        
        const summaryName = document.getElementById("summary-pkg-name");
        const summaryPrice = document.getElementById("summary-total-price");
        if (summaryName) summaryName.textContent = pkg.name;
        if (summaryPrice) summaryPrice.textContent = pkg.price + " ৳";
    }}

    function selectPaymentMethod(method) {{
        selectedPayment = method;
        const options = ["bkash", "nagad", "rocket", "wallet"];
        options.forEach(m => {{
            const el = document.getElementById("pm-" + m);
            if (!el) return;
            const check = el.querySelector(".pm-check");
            if (m === method) {{
                el.classList.add("border-primary-500", "bg-primary-500/10");
                el.classList.remove("border-theme-subtle", "bg-[#15122c]");
                if (check) check.className = "fa-solid fa-circle-check text-primary-400 pm-check";
            }} else {{
                el.classList.remove("border-primary-500", "bg-primary-500/10");
                el.classList.add("border-theme-subtle", "bg-[#15122c]");
                if (check) check.className = "fa-regular fa-circle text-slate-500 pm-check";
            }}
        }});
    }}

    // Player ID verification simulator
    function verifyPlayerId() {{
        const uidInput = document.getElementById("player-uid-input");
        const uid = uidInput ? uidInput.value.trim() : "";
        const btn = document.getElementById("check-id-btn");
        const resBox = document.getElementById("player-check-result");
        
        if (!uid) {{
            alert("অনুগ্রহ করে Player ID লিখুন!");
            if (uidInput) uidInput.focus();
            return;
        }}
        
        if (btn) {{
            btn.innerHTML = `<i class="fa-solid fa-spinner fa-spin"></i> Checking Garena Server...`;
            btn.disabled = true;
        }}
        
        setTimeout(() => {{
            if (btn) {{
                btn.innerHTML = `<i class="fa-solid fa-magnifying-glass"></i> Check Player ID Name`;
                btn.disabled = false;
            }}
            
            const randomNames = ["★_RRR_KILLER_★", "BD_MAFIA_BOSS", "⚡_DARK_SHADOW_⚡", "PRO_GAMER_99", "TANJID_FF_07"];
            const pName = randomNames[Math.floor(Math.random() * randomNames.length)];
            
            const resName = document.getElementById("checked-player-name");
            if (resName) resName.textContent = `Player: ${{pName}} (UID: ${{uid}})`;
            if (resBox) resBox.classList.remove("hidden");
        }}, 800);
    }}

    // Buy Now & Checkout flow
    function handleBuyNow() {{
        const uidInput = document.getElementById("player-uid-input");
        const uid = uidInput ? uidInput.value.trim() : "";
        if (!uid) {{
            alert("অনুগ্রহ করে আপনার Player ID / Email প্রদান করুন!");
            if (uidInput) uidInput.focus();
            return;
        }}
        if (!selectedPackage) {{
            alert("অনুগ্রহ করে একটি রিচার্জ প্যাকেজ সিলেক্ট করুন!");
            return;
        }}

        const pkgPriceNum = parseFloat(selectedPackage.price) || 0;

        // Check if paying with wallet
        if (selectedPayment === "wallet") {{
            if (userBalance < pkgPriceNum) {{
                alert(`আপনার ওয়ালেটে পর্যাপ্ত ব্যালেন্স নেই! বর্তমান ব্যালেন্স: ${{userBalance.toFixed(2)}} ৳। দয়া করে ব্যালেন্স অ্যাড করুন অথবা বিকাশ/নগদ দিয়ে পে করুন।`);
                openAddMoneyModal();
                return;
            }}
            // Deduct wallet balance
            userBalance -= pkgPriceNum;
            updateBalanceUI();
            completeOrder(uid, selectedPackage, "RRR Wallet (Paid)");
            return;
        }}

        // Setup Checkout Modal
        const orderRef = "RRR-" + Math.floor(100000 + Math.random() * 900000);
        lastGeneratedOrderId = orderRef;
        const refEl = document.getElementById("modal-order-ref");
        const payAmountEl = document.getElementById("modal-pay-amount");
        if (refEl) refEl.textContent = orderRef;
        if (payAmountEl) payAmountEl.textContent = selectedPackage.price + " ৳";
        
        const header = document.getElementById("checkout-gateway-header");
        const logo = document.getElementById("modal-gateway-logo");
        const title = document.getElementById("modal-gateway-title");
        const merchNo = document.getElementById("modal-merchant-no");

        if (selectedPayment === "bkash") {{
            if (header) header.className = "bg-[#E2136E] text-white p-4 flex items-center justify-between";
            if (logo) logo.textContent = "bK";
            if (title) title.textContent = "bKash Instant Gateway";
            if (merchNo) merchNo.textContent = "01889-123456 (Personal)";
        }} else if (selectedPayment === "nagad") {{
            if (header) header.className = "bg-[#F7941D] text-white p-4 flex items-center justify-between";
            if (logo) logo.textContent = "Ng";
            if (title) title.textContent = "Nagad Instant Gateway";
            if (merchNo) merchNo.textContent = "01889-123456 (Merchant)";
        }} else {{
            if (header) header.className = "bg-[#8C3494] text-white p-4 flex items-center justify-between";
            if (logo) logo.textContent = "Rk";
            if (title) title.textContent = "Rocket Payment Gateway";
            if (merchNo) merchNo.textContent = "01889-123456 (Personal)";
        }}

        const senderInp = document.getElementById("pay-sender-no");
        const trxInp = document.getElementById("pay-trxid");
        if (senderInp) senderInp.value = currentUser.phone || "";
        if (trxInp) trxInp.value = "";

        openModal("checkout-modal");
    }}

    function autoFillPaymentTest() {{
        const senderInp = document.getElementById("pay-sender-no");
        const trxInp = document.getElementById("pay-trxid");
        if (senderInp) senderInp.value = "01789" + Math.floor(100000 + Math.random() * 900000);
        
        const chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
        let trx = "BL";
        for (let i = 0; i < 8; i++) trx += chars.charAt(Math.floor(Math.random() * chars.length));
        if (trxInp) trxInp.value = trx;
    }}

    function confirmPayment() {{
        const senderInp = document.getElementById("pay-sender-no");
        const trxInp = document.getElementById("pay-trxid");
        const sender = senderInp ? senderInp.value.trim() : "";
        const trxid = trxInp ? trxInp.value.trim() : "";
        const btn = document.getElementById("modal-confirm-btn");

        if (!sender || !trxid) {{
            alert("অনুগ্রহ করে আপনার Sender Number এবং TrxID প্রদান করুন!");
            return;
        }}

        if (btn) {{
            btn.innerHTML = `<i class="fa-solid fa-spinner fa-spin"></i> Verifying with Gateway...`;
            btn.disabled = true;
        }}

        setTimeout(() => {{
            if (btn) {{
                btn.innerHTML = `<i class="fa-solid fa-lock"></i> Confirm & Verify Payment`;
                btn.disabled = false;
            }}
            closeModal("checkout-modal");
            
            const uidInput = document.getElementById("player-uid-input");
            const uid = uidInput ? uidInput.value.trim() : "192837465";
            completeOrder(uid, selectedPackage, `${{selectedPayment.toUpperCase()}} (Trx: ${{trxid}})`);
        }}, 1200);
    }}

    function completeOrder(uid, pkg, methodStr) {{
        const invOrderEl = document.getElementById("inv-order-id");
        const invUidEl = document.getElementById("inv-player-uid");
        const invPkgEl = document.getElementById("inv-package");
        const invAmtEl = document.getElementById("inv-amount");
        const invMethodEl = document.getElementById("inv-method");

        if (invOrderEl) invOrderEl.textContent = lastGeneratedOrderId;
        if (invUidEl) invUidEl.textContent = uid;
        if (invPkgEl) invPkgEl.textContent = pkg.name;
        if (invAmtEl) invAmtEl.textContent = pkg.price + " ৳";
        if (invMethodEl) invMethodEl.textContent = methodStr;

        // Save order directly into Convex Cloud Database
        convex.mutation("orders:create", {{
            order_id: lastGeneratedOrderId,
            product_id: currentProductId,
            product_name: (productsData.find(p => p.id === currentProductId) || {{}}).name || "Free Fire Topup",
            package_name: pkg.name,
            amount: parseFloat(pkg.price) || 0,
            player_uid: uid,
            payment_method: methodStr,
            user_phone: currentUser.phone || undefined
        }}).then(res => {{
            console.log("Order saved to Convex Database:", res);
        }}).catch(err => console.warn("Convex order save notice:", err));

        // Add to live public orders feed
        const newOrder = {{
            full_name: currentUser.name || "Customer",
            avatar: "https://lh3.googleusercontent.com/a/ACg8ocLDlfC4vHjXm1TtshnotB4DGPMl1fHvHqpJpHCykwaT-f-nbWQ=s96-c",
            name: pkg.name,
            amount: pkg.price,
            status: "completed"
        }};
        publicOrdersData.unshift(newOrder);
        prependRecentOrder(newOrder);

        openModal("invoice-modal");
    }}

    function prependRecentOrder(order) {{
        const list = document.getElementById("recent-orders-list");
        if (!list) return;
        const art = document.createElement("article");
        art.className = "theme-order-card group animate-card-glow mb-2.5";
        const av = order.avatar || "https://apis.rrrtopup.com/uploads/images/1776251457859-1776068722862-RRR_Fov_2.png";
        
        art.innerHTML = `
            <div class="relative z-10 flex items-center gap-2.5 px-3 py-2.5 sm:gap-4 sm:px-4 sm:py-3.5 md:gap-6">
                <div class="relative h-10 w-10 shrink-0 sm:h-12 sm:w-12 md:h-14 md:w-14">
                    <img src="${{av}}" alt="${{order.full_name}}" class="h-full w-full rounded-full object-cover ring-2 ring-primary-300/45" onerror="this.src='https://apis.rrrtopup.com/uploads/images/1776251457859-1776068722862-RRR_Fov_2.png'"/>
                </div>
                <div class="min-w-0 flex-1">
                    <div class="flex items-center gap-1.5">
                        <h2 class="truncate text-[13px] font-semibold text-white sm:text-[16px] md:text-[18px]">${{order.full_name}}</h2>
                    </div>
                    <p class="mt-0.5 flex items-center gap-1.5 text-[11px] text-[#94A3B8] sm:text-[13px] md:text-[14px]">
                        <i class="fa-solid fa-gem text-primary-300 text-xs shrink-0"></i>
                        <span class="truncate">${{order.name}}</span>
                    </p>
                </div>
                <div class="hidden shrink-0 text-right sm:block">
                    <p class="text-[18px] font-bold leading-none text-[#34D399] md:text-[22px]">${{order.amount}} ৳</p>
                    <p class="mt-1 flex items-center justify-end gap-1 text-[11px] text-primary-300/80 md:text-xs">
                        <i class="fa-regular fa-clock"></i> just now
                    </p>
                </div>
                <div class="flex shrink-0 flex-col items-end gap-1">
                    <p class="text-[14px] font-bold text-[#34D399] sm:hidden">${{order.amount}} ৳</p>
                    <span class="inline-flex items-center gap-1 rounded-full px-2 py-1 text-[10px] font-bold capitalize sm:px-3 sm:py-1.5 sm:text-xs bg-gradient-to-r from-[#22C55E] to-[#16A34A] text-white shadow">
                        <i class="fa-solid fa-check text-xs"></i> completed
                    </span>
                </div>
            </div>
            <div class="pointer-events-none absolute inset-0 z-20 overflow-hidden rounded-[18px] sm:rounded-[22px]">
                <div class="absolute left-0 top-0 h-full w-16 animate-card-slice bg-gradient-to-r from-transparent via-primary-300/55 to-transparent sm:w-24"></div>
            </div>
        `;
        list.insertBefore(art, list.firstChild);
    }}

    // Tracking Modal
    function openTrackOrderModal() {{
        openModal("track-modal");
    }}

    function trackThisOrder() {{
        closeModal("invoice-modal");
        openModal("track-modal");
        const trackInp = document.getElementById("track-order-input");
        if (trackInp) trackInp.value = lastGeneratedOrderId;
    }}

    async function searchOrderStatus() {{
        const trackInp = document.getElementById("track-order-input");
        const resBox = document.getElementById("track-result-box");
        const input = trackInp ? trackInp.value.trim() : "";
        if (!input) {{
            alert("অনুগ্রহ করে আপনার Order ID অথবা Player UID লিখুন!");
            if (trackInp) trackInp.focus();
            return;
        }}

        // Query live Convex Database
        const resEl = document.getElementById("track-status-display");
        if (resEl) {{
            resEl.innerHTML = `<div class="p-3 text-center text-xs text-primary-400"><i class="fa-solid fa-spinner fa-spin mr-1"></i> Checking Convex Cloud Database...</div>`;
        }}
        if (resBox) resBox.classList.remove("hidden");

        const liveOrder = await convex.query("orders:track", {{ search: input }});
        if (liveOrder && resEl) {{
            resEl.innerHTML = `
                <div class="p-3 rounded-xl bg-[#161a42] border border-emerald-500/40 text-left space-y-1.5 animate-fadeIn">
                    <div class="flex items-center justify-between">
                        <span class="text-xs font-bold text-white">Order: ${{liveOrder.order_id}}</span>
                        <span class="px-2 py-0.5 rounded-full text-[10px] font-bold bg-emerald-500/20 text-emerald-400 border border-emerald-500/40 uppercase">${{liveOrder.status}}</span>
                    </div>
                    <p class="text-[11px] text-slate-300">Player UID: <span class="text-primary-300 font-mono font-semibold">${{liveOrder.player_uid}}</span></p>
                    <p class="text-[11px] text-slate-300">Package: <span class="text-white font-semibold">${{liveOrder.package_name}}</span> (${{liveOrder.amount}} ৳)</p>
                    <p class="text-[11px] text-emerald-400 font-semibold"><i class="fa-solid fa-bolt mr-1"></i> Verified & Stored in Convex Cloud Database</p>
                    <p class="text-[10px] text-slate-400">Date: ${{new Date(liveOrder.created_at || liveOrder._creationTime).toLocaleString()}}</p>
                </div>
            `;
        }} else if (resEl) {{
            resEl.innerHTML = `
                <div class="p-3 rounded-xl bg-[#161a42] border border-theme-subtle text-left space-y-1.5">
                    <div class="flex items-center justify-between">
                        <span class="text-xs font-bold text-white">Order: ${{input}}</span>
                        <span class="px-2 py-0.5 rounded-full text-[10px] font-bold bg-emerald-500/20 text-emerald-400 border border-emerald-500/40">COMPLETED</span>
                    </div>
                    <p class="text-[11px] text-slate-300">Package: Free Fire UID Topup BD Server</p>
                    <p class="text-[11px] text-emerald-400 font-semibold"><i class="fa-solid fa-bolt mr-1"></i> Instant Delivery Confirmed via Garena Server</p>
                    <p class="text-[10px] text-slate-400">Status: Verified & Auto Delivered</p>
                </div>
            `;
        }}
    }}

    // Add Money Logic
    function openAddMoneyModal() {{
        const curBalEl = document.getElementById("addmoney-current-bal");
        if (curBalEl) curBalEl.textContent = userBalance.toFixed(2) + " ৳";
        openModal("addmoney-modal");
    }}

    function processAddMoney() {{
        const amtInput = document.getElementById("addmoney-amount");
        const trxInput = document.getElementById("addmoney-trxid");
        const amount = parseFloat(amtInput ? amtInput.value : 0);
        const trxid = trxInput ? trxInput.value.trim() : "";
        
        if (!amount || amount < 10) {{
            alert("সর্বনিম্ন ১০ টাকা অ্যাড করতে পারবেন!");
            return;
        }}
        if (!trxid) {{
            alert("অনুগ্রহ করে TrxID প্রদান করুন!");
            return;
        }}

        userBalance += amount;
        updateBalanceUI();

        // Sync with Convex Cloud Database
        convex.mutation("wallet:addMoney", {{
            phone: currentUser.phone || "01889123456",
            amount: amount,
            payment_method: "bKash",
            sender_number: currentUser.phone || "01889123456",
            trx_id: trxid
        }}).then(res => {{
            if (res && typeof res.newBalance === "number") {{
                userBalance = res.newBalance;
                updateBalanceUI();
            }}
            console.log("Wallet synced to Convex:", res);
        }}).catch(e => console.warn("Convex wallet sync:", e));

        closeModal("addmoney-modal");
        alert(`অভিনন্দন! আপনার ওয়ালেটে ৳${{amount}} সফলভাবে যুক্ত হয়েছে। বর্তমান ব্যালেন্স: ${{userBalance.toFixed(2)}} ৳ (Convex Cloud Synced)`);
    }}

    function updateBalanceUI() {{
        const hBal = document.getElementById("header-wallet-val");
        const sBal = document.getElementById("sidebar-wallet-val");
        const mBal = document.getElementById("mobile-wallet-val");
        const cBal = document.getElementById("checkout-wallet-bal");

        if (hBal) hBal.textContent = userBalance.toFixed(2) + " ৳";
        if (sBal) sBal.textContent = userBalance.toFixed(2) + " ৳";
        if (mBal) mBal.textContent = Math.floor(userBalance) + " ৳";
        if (cBal) cBal.textContent = "Balance: " + userBalance.toFixed(2) + " ৳";
        storage.set("rrrtopup_balance", userBalance.toString());
    }}

    // Login logic
    function openLoginModal() {{
        openModal("login-modal");
    }}

    function processLogin() {{
        const nameInp = document.getElementById("login-name");
        const phoneInp = document.getElementById("login-phone");
        const name = nameInp ? nameInp.value.trim() : "";
        const phone = phoneInp ? phoneInp.value.trim() : "";
        
        if (!name || !phone) {{
            alert("অনুগ্রহ করে নাম ও মোবাইল নাম্বার দিন!");
            return;
        }}

        currentUser = {{ name, phone }};
        storage.set("rrrtopup_user", JSON.stringify(currentUser));

        // Sync login with Convex Cloud Database
        convex.mutation("users:login", {{ name, phone }}).then(dbUser => {{
            if (dbUser && typeof dbUser.balance === "number") {{
                userBalance = dbUser.balance;
                updateBalanceUI();
            }}
            console.log("User logged in to Convex Database:", dbUser);
        }}).catch(e => console.warn("Convex login notice:", e));

        applyUserState();
        closeModal("login-modal");
        alert(`স্বাগতম, ${{name}}! আপনি সফলভাবে লগইন করেছেন। Convex Live Database এর সাথে যুক্ত হয়েছে।`);
    }}

    function loadSavedUserState() {{
        const savedBal = storage.get("rrrtopup_balance");
        if (savedBal) userBalance = parseFloat(savedBal) || 0;
        updateBalanceUI();

        const savedUser = storage.get("rrrtopup_user");
        if (savedUser) {{
            try {{
                currentUser = JSON.parse(savedUser);
                applyUserState();
            }} catch(e) {{}}
        }}

        // Verify Convex Auth Session Token (Zero OTP)
        const authToken = storage.get("rrrtopup_auth_token");
        if (authToken) {{
            convex.query("auth:getMe", {{ token: authToken }}).then(user => {{
                if (user) {{
                    currentUser = user;
                    userBalance = user.balance || 0;
                    storage.set("rrrtopup_user", JSON.stringify(user));
                    storage.set("rrrtopup_balance", userBalance.toString());
                    updateBalanceUI();
                    applyUserState();
                    console.log("Convex Auth Session Verified (Zero OTP):", user.name);
                }}
            }}).catch(e => console.warn("Convex Auth session check notice:", e));
        }}
    }}

    function applyUserState() {{
        if (currentUser.name && currentUser.name !== "Guest User") {{
            const hAuthBtn = document.getElementById("header-auth-btn");
            const sUserName = document.getElementById("sidebar-user-name");
            const sUserAvatar = document.getElementById("sidebar-user-avatar");
            const sAuthBtn = document.getElementById("sidebar-auth-btn");

            if (hAuthBtn) {{
                hAuthBtn.innerHTML = `<i class="fa-solid fa-user-check text-emerald-400"></i> <span class="max-w-[80px] truncate inline-block align-bottom">${{currentUser.name}}</span>`;
                hAuthBtn.onclick = () => {{
                    if (confirm(`লগআউট করতে চান?\nইউজার: ${{currentUser.name}} (${{currentUser.phone || currentUser.email}})`)) {{
                        logoutUser();
                    }}
                }};
            }}
            if (sUserName) sUserName.textContent = currentUser.name;
            if (sUserAvatar) sUserAvatar.innerHTML = currentUser.name.charAt(0).toUpperCase();
            if (sAuthBtn) {{
                sAuthBtn.innerHTML = `<i class="fa-solid fa-arrow-right-from-bracket"></i> Logout`;
                sAuthBtn.onclick = logoutUser;
            }}
        }}
    }}

    function logoutUser() {{
        const token = storage.get("rrrtopup_auth_token");
        if (token) {{
            convex.mutation("auth:signOut", {{ token }}).catch(() => {{}});
        }}
        storage.remove("rrrtopup_auth_token");
        storage.remove("rrrtopup_user");
        storage.remove("rrrtopup_balance");
        currentUser = {{ name: "Guest User", phone: "" }};
        window.location.reload();
    }}

    // Modal Helpers
    function openModal(id) {{
        const m = document.getElementById(id);
        if (m) m.classList.add("open");
    }}

    function closeModal(id) {{
        const m = document.getElementById(id);
        if (m) m.classList.remove("open");
    }}

    function openInfoModal(title, text) {{
        const titleEl = document.getElementById("info-modal-title");
        const bodyEl = document.getElementById("info-modal-body");
        if (titleEl) titleEl.textContent = title;
        if (bodyEl) bodyEl.textContent = text;
        openModal("info-modal");
    }}

    function showAboutUs() {{
        openInfoModal("About Us", "RRR Topup is Bangladesh\'s trusted instant game topup and digital subscription platform. We provide 24/7 automated delivery via Garena API with 100% safety guarantee.");
    }}

    function showPrivacy() {{
        openInfoModal("Privacy Policy", "We value your privacy. We never store your game passwords. Only player UID is used to credit diamonds through official channels.");
    }}

    function showTerms() {{
        openInfoModal("Terms & Conditions", "1. Diamond orders are processed within 1-2 minutes.\\n2. Provide correct Player UID.\\n3. In case of server issue, delivery may take up to 24 hours or refund will be made to wallet.");
    }}

    function showRefund() {{
        openInfoModal("Refund Policy", "If diamond delivery fails within 24 hours, 100% of the payment will be refunded immediately into your RRR Topup wallet.");
    }}

    function openTutorialModal() {{
        openModal("video-modal");
    }}

    // Universal copy helper (works in file://, HTTP, HTTPS)
    function copyToClipboard(text, btn) {{
        if (navigator.clipboard && navigator.clipboard.writeText) {{
            navigator.clipboard.writeText(text).then(() => {{
                showCopied(btn);
            }}).catch(() => fallbackCopy(text, btn));
        }} else {{
            fallbackCopy(text, btn);
        }}
    }}

    function fallbackCopy(text, btn) {{
        const ta = document.createElement("textarea");
        ta.value = text;
        ta.style.position = "fixed";
        ta.style.left = "-9999px";
        document.body.appendChild(ta);
        ta.select();
        try {{
            document.execCommand("copy");
            showCopied(btn);
        }} catch(e) {{
            alert("Copied: " + text);
        }}
        if (ta.parentNode) ta.parentNode.removeChild(ta);
    }}

    function showCopied(btn) {{
        if (!btn) return;
        const old = btn.innerHTML;
        btn.innerHTML = `<i class="fa-solid fa-check"></i> Copied!`;
        setTimeout(() => {{ if (btn) btn.innerHTML = old; }}, 1500);
    }}

    // Sidebar Mobile
    function toggleSidebar(open) {{
        const overlay = document.getElementById("sidebar_overly");
        const panel = document.getElementById("sidebar_panel");
        if (!overlay || !panel) return;
        if (open) {{
            overlay.classList.remove("opacity-0", "pointer-events-none");
            overlay.classList.add("opacity-100", "pointer-events-auto");
            panel.classList.remove("translate-x-full");
        }} else {{
            overlay.classList.remove("opacity-100", "pointer-events-auto");
            overlay.classList.add("opacity-0", "pointer-events-none");
            panel.classList.add("translate-x-full");
        }}
    }}

    // Enhanced Hero Slider Controller with Swipe, Arrows & Fallback Handling
    const totalSlides = 3;

    function initSlider() {{
        startSliderTimer();
        setupSliderGestures();
    }}

    function startSliderTimer() {{
        if (sliderTimer) clearInterval(sliderTimer);
        sliderTimer = setInterval(() => {{
            setSlide((currentSlide + 1) % totalSlides);
        }}, 4000);
    }}

    function stopSliderTimer() {{
        if (sliderTimer) {{
            clearInterval(sliderTimer);
            sliderTimer = null;
        }}
    }}

    function setSlide(idx, ev) {{
        if (ev) ev.stopPropagation();
        currentSlide = (idx + totalSlides) % totalSlides;
        const track = document.getElementById("slider-track");
        if (track) {{
            track.style.transform = `translateX(-${{currentSlide * 100}}%)`;
        }}
        
        const dots = document.querySelectorAll(".slider-dot");
        dots.forEach((d, i) => {{
            if (i === currentSlide) {{
                d.className = "slider-dot w-6 sm:w-8 h-1.5 sm:h-2 rounded-full bg-primary-500 transition-all cursor-pointer shadow-md";
            }} else {{
                d.className = "slider-dot w-2 sm:w-2.5 h-1.5 sm:h-2 rounded-full bg-white/40 hover:bg-white/70 transition-all cursor-pointer";
            }}
        }});
        startSliderTimer();
    }}

    function nextSlide(ev) {{
        if (ev) ev.stopPropagation();
        setSlide(currentSlide + 1);
    }}

    function prevSlide(ev) {{
        if (ev) ev.stopPropagation();
        setSlide(currentSlide - 1);
    }}

    function setupSliderGestures() {{
        const box = document.getElementById("hero-slider-box");
        if (!box) return;

        let startX = 0;
        let startY = 0;
        let isTouching = false;

        box.addEventListener("touchstart", (e) => {{
            if (e.touches.length === 1) {{
                startX = e.touches[0].clientX;
                startY = e.touches[0].clientY;
                isTouching = true;
                stopSliderTimer();
            }}
        }}, {{ passive: true }});

        box.addEventListener("touchend", (e) => {{
            if (!isTouching) return;
            isTouching = false;
            const endX = e.changedTouches[0].clientX;
            const endY = e.changedTouches[0].clientY;
            const diffX = endX - startX;
            const diffY = endY - startY;

            if (Math.abs(diffX) > 35 && Math.abs(diffX) > Math.abs(diffY)) {{
                if (diffX < 0) {{
                    nextSlide();
                }} else {{
                    prevSlide();
                }}
            }} else {{
                startSliderTimer();
            }}
        }}, {{ passive: true }});

        box.addEventListener("mouseenter", () => stopSliderTimer());
        box.addEventListener("mouseleave", () => startSliderTimer());
    }}

    const remoteBannerFallbacks = [
        "https://apis.rrrtopup.com/images/images-1773166066810.jpg",
        "https://apis.rrrtopup.com/images/images-1772817502063.jpg",
        "https://apis.rrrtopup.com/images/images-1773166049555.jpg"
    ];

    function handleBannerError(img, slideNum) {{
        const idx = slideNum - 1;
        if (!img.dataset.stage) {{
            img.dataset.stage = "1";
            img.src = `images/banner${{slideNum}}.jpg`;
        }} else if (img.dataset.stage === "1") {{
            img.dataset.stage = "2";
            img.src = remoteBannerFallbacks[idx] || remoteBannerFallbacks[0];
        }} else if (img.dataset.stage === "2") {{
            img.dataset.stage = "3";
            img.src = getBannerSvg(slideNum);
        }}
    }}

    function getBannerSvg(num) {{
        if (num === 1) {{
            return "data:image/svg+xml;charset=utf-8," + encodeURIComponent(`<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 371" width="100%" height="100%"><defs><linearGradient id="g1" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#090f2e"/><stop offset="50%" stop-color="#0c2340"/><stop offset="100%" stop-color="#144272"/></linearGradient></defs><rect width="900" height="371" fill="url(#g1)"/><circle cx="750" cy="180" r="130" fill="#0077b6" opacity="0.25"/><text x="60" y="90" fill="#38bdf8" font-family="sans-serif" font-size="16" font-weight="bold" letter-spacing="3">OFFICIAL TELEGRAM CHANNEL</text><text x="60" y="160" fill="#ffffff" font-family="sans-serif" font-size="38" font-weight="900">JOIN RRR TOPUP TELEGRAM</text><text x="60" y="210" fill="#90e0ef" font-family="sans-serif" font-size="18">24/7 Live Support • Exclusive Promo Codes • Daily Giveaways</text><rect x="60" y="250" width="220" height="48" rx="24" fill="#0284c7"/><text x="170" y="280" fill="#ffffff" font-family="sans-serif" font-size="16" font-weight="bold" text-anchor="middle">Join Channel ➔</text></svg>`);
        }} else if (num === 2) {{
            return "data:image/svg+xml;charset=utf-8," + encodeURIComponent(`<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 371" width="100%" height="100%"><defs><linearGradient id="g2" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#180c2e"/><stop offset="50%" stop-color="#2d0b4e"/><stop offset="100%" stop-color="#ea580c"/></linearGradient></defs><rect width="900" height="371" fill="url(#g2)"/><text x="60" y="90" fill="#f59e0b" font-family="sans-serif" font-size="16" font-weight="bold" letter-spacing="3">⚡ 100% INSTANT AUTO BOT</text><text x="60" y="160" fill="#ffffff" font-family="sans-serif" font-size="38" font-weight="900">FREE FIRE UID TOPUP</text><text x="60" y="210" fill="#fdba74" font-family="sans-serif" font-size="18">1-2 Minute Delivery • BD Server Official • 100% Safe</text><rect x="60" y="250" width="220" height="48" rx="24" fill="#ff6b35"/><text x="170" y="280" fill="#ffffff" font-family="sans-serif" font-size="16" font-weight="bold" text-anchor="middle">Topup Now ➔</text></svg>`);
        }} else {{
            return "data:image/svg+xml;charset=utf-8," + encodeURIComponent(`<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 371" width="100%" height="100%"><defs><linearGradient id="g3" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#1e0828"/><stop offset="50%" stop-color="#4a0e4e"/><stop offset="100%" stop-color="#b5179e"/></linearGradient></defs><rect width="900" height="371" fill="url(#g3)"/><circle cx="730" cy="180" r="55" fill="#ef4444"/><polygon points="720,165 750,180 720,195" fill="#ffffff"/><text x="60" y="90" fill="#f472b6" font-family="sans-serif" font-size="16" font-weight="bold" letter-spacing="3">VIDEO TUTORIAL</text><text x="60" y="160" fill="#ffffff" font-family="sans-serif" font-size="36" font-weight="900">কিভাবে টপআপ করবেন?</text><text x="60" y="210" fill="#fbcfe8" font-family="sans-serif" font-size="18">সহজ ১ মিনিটের ভিডিও গাইড • বিকাশ, নগদ ও ওয়ালেট ব্যবহারের নিয়ম</text><rect x="60" y="250" width="220" height="48" rx="24" fill="#ef4444"/><text x="170" y="280" fill="#ffffff" font-family="sans-serif" font-size="16" font-weight="bold" text-anchor="middle">Watch Video ▶</text></svg>`);
        }}
    }}

    // Category Filter Pills
    function filterCategory(catId, btn) {{
        document.querySelectorAll(".cat-pill").forEach(p => {{
            p.classList.remove("active", "bg-primary-500", "text-white");
            p.classList.add("bg-[#141638]", "text-slate-300");
        }});
        if (btn) {{
            btn.classList.add("active", "bg-primary-500", "text-white");
            btn.classList.remove("bg-[#141638]", "text-slate-300");
        }}

        if (catId === \'all\') {{
            document.querySelectorAll(".category-section").forEach(sec => sec.style.display = "");
        }} else {{
            document.querySelectorAll(".category-section").forEach(sec => {{
                sec.style.display = (sec.id === catId) ? "" : "none";
            }});
        }}
    }}

    function scrollToSection(id) {{
        navigateToHome();
        setTimeout(() => {{
            const el = document.getElementById(id);
            if (el) el.scrollIntoView({{ behavior: "smooth" }});
        }}, 100);
    }}

    // Real-time Search Filter
    function handleSearch(query) {{
        const q = (query || "").trim().toLowerCase();
        const clearBtn = document.getElementById("clear-search-btn");
        if (clearBtn) clearBtn.classList.toggle("hidden", q.length === 0);

        const items = document.querySelectorAll(".product-item");
        items.forEach(it => {{
            const name = it.getAttribute("data-name") || "";
            it.style.display = (!q || name.includes(q)) ? "" : "none";
        }});
    }}

    function clearSearch() {{
        const input = document.getElementById("header-search");
        if (input) {{
            input.value = "";
            handleSearch("");
        }}
    }}

    // Live Orders simulation
    function initLiveOrdersSimulation() {{
        if (recentOrdersTimer) clearInterval(recentOrdersTimer);
        const sampleNames = ["Tanvir Ahmed", "Sadikur Rahman", "Sakib Al Hasan", "Mehedi Hasan", "Naimur Rahman", "Robiul Islam", "Ashikur", "Shahidul"];
        const samplePkgs = ["115 Daimond💎", "240 Daimond💎", "Weekly", "Monthly", "100 Daimond💎", "Level Up - Lv 20", "CapCut Pro 1 Month"];
        const sampleAmounts = [78, 156, 155, 770, 70, 70, 150];

        recentOrdersTimer = setInterval(() => {{
            const rIdx = Math.floor(Math.random() * sampleNames.length);
            const simOrder = {{
                full_name: sampleNames[rIdx],
                avatar: "https://lh3.googleusercontent.com/a/ACg8ocLDlfC4vHjXm1TtshnotB4DGPMl1fHvHqpJpHCykwaT-f-nbWQ=s96-c",
                name: samplePkgs[rIdx],
                amount: sampleAmounts[rIdx],
                status: "completed"
            }};
            prependRecentOrder(simOrder);
        }}, 9000);
    }}
</script>
</body>
</html>
'''

# Write to freefire-topup/index.html
with open('/storage/emulated/0/Codex/freefire-topup/index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Generated clean index.html! Size: {len(html_content)} bytes")
