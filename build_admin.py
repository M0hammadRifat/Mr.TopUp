# -*- coding: utf-8 -*-
"""
Generate the Updated, Feature-Packed Production Admin Panel for RRR Topup (admin.html)
Connected in real-time with Convex Cloud Database.
"""

admin_html_content = '''<!DOCTYPE html>
<html lang="bn">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>অ্যাডমিন কন্ট্রোল সেন্টার | RRR Topup Admin Panel</title>
    <link rel="icon" type="image/png" href="images/favicon.png">
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- FontAwesome 6 CDN -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Hind+Siliguri:wght@400;500;600;700&family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@400;600;700&display=swap" rel="stylesheet">

    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        primary: {
                            50: '#eef2ff',
                            100: '#e0e7ff',
                            200: '#c7d2fe',
                            300: '#a5b4fc',
                            400: '#818cf8',
                            500: '#6366f1',
                            600: '#4f46e5',
                            700: '#4338ca',
                            800: '#3730a3',
                            900: '#312e81',
                        },
                        dark: {
                            950: '#040612',
                            900: '#070a1a',
                            850: '#0b1028',
                            800: '#101738',
                            700: '#17204d',
                            600: '#202c69',
                            500: '#2c3c8c',
                        }
                    },
                    fontFamily: {
                        sans: ['"Inter"', '"Hind Siliguri"', 'sans-serif'],
                        mono: ['"JetBrains Mono"', 'monospace'],
                    }
                }
            }
        }
    </script>

    <style>
        body {
            font-family: 'Inter', 'Hind Siliguri', sans-serif;
            background-color: #050816;
            color: #f1f5f9;
            min-height: 100vh;
        }
        .admin-card {
            background: rgba(11, 16, 40, 0.85);
            backdrop-filter: blur(14px);
            border: 1px solid rgba(99, 102, 241, 0.2);
            box-shadow: 0 4px 25px -2px rgba(0, 0, 0, 0.5);
        }
        .admin-table th {
            background-color: #12193e;
            color: #94a3b8;
            font-size: 11px;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            padding: 12px 14px;
            font-weight: 700;
        }
        .admin-table td {
            padding: 12px 14px;
            border-bottom: 1px solid rgba(99, 102, 241, 0.1);
            font-size: 12px;
        }
        .admin-table tr:hover td {
            background-color: rgba(99, 102, 241, 0.06);
        }
        .tab-btn.active {
            background: linear-gradient(135deg, #2563eb 0%, #4f46e5 100%);
            color: #ffffff;
            font-weight: 700;
            box-shadow: 0 4px 15px rgba(37, 99, 235, 0.4);
            border-color: rgba(99, 102, 241, 0.6);
        }
        .custom-scrollbar::-webkit-scrollbar {
            width: 6px;
            height: 6px;
        }
        .custom-scrollbar::-webkit-scrollbar-track {
            background: #070a1a;
        }
        .custom-scrollbar::-webkit-scrollbar-thumb {
            background: #202c69;
            border-radius: 4px;
        }
        .toast-notify {
            animation: slideDown 0.3s ease-out forwards;
        }
        @keyframes slideDown {
            from { transform: translateY(-100%); opacity: 0; }
            to { transform: translateY(0); opacity: 1; }
        }
    </style>
</head>
<body class="flex flex-col min-h-screen">

    <!-- FLOATING TOAST NOTIFICATION -->
    <div id="toast-container" class="fixed top-4 right-4 z-50 flex flex-col gap-2 max-w-sm w-full pointer-events-none"></div>

    <!-- ============================================== -->
    <!-- ADMIN LOGIN LOCK OVERLAY (Security Shield)     -->
    <!-- ============================================== -->
    <div id="login-overlay" class="fixed inset-0 z-50 bg-[#040612]/95 backdrop-blur-md flex items-center justify-center p-4">
        <div class="max-w-md w-full admin-card rounded-3xl p-6 sm:p-8 border border-blue-500/40 text-center shadow-2xl relative">
            <div class="w-16 h-16 rounded-2xl bg-blue-500/10 border border-blue-500/30 mx-auto flex items-center justify-center text-blue-400 mb-4 shadow-inner">
                <i class="fa-solid fa-shield-halved text-2xl"></i>
            </div>
            <h2 class="text-xl sm:text-2xl font-black text-white tracking-wide">RRR Topup Admin Access</h2>
            <p class="text-xs text-slate-400 mt-1 mb-6">অ্যাডমিন কন্ট্রোল সেন্টারে প্রবেশ করতে ক্রেডেনশিয়াল দিন</p>

            <div id="login-error" class="hidden mb-4 p-3 rounded-xl bg-rose-500/20 text-rose-300 border border-rose-500/40 text-xs font-semibold text-left flex items-center gap-2">
                <i class="fa-solid fa-triangle-exclamation"></i>
                <span id="login-error-text">ভুল অ্যাডমিন ইমেইল বা পাসওয়ার্ড!</span>
            </div>

            <form onsubmit="handleAdminLogin(event)" class="space-y-4 text-left">
                <div>
                    <label class="block text-xs font-bold text-slate-300 mb-1.5">
                        <i class="fa-solid fa-envelope text-blue-400 mr-1.5"></i> অ্যাডমিন ইমেইল (Admin Email)
                    </label>
                    <input type="email" id="admin-email-input" required placeholder="admin@example.com"
                           class="w-full px-4 py-2.5 rounded-xl bg-dark-900 border border-slate-700 text-white text-sm focus:outline-none focus:border-blue-500 font-mono">
                </div>
                <div>
                    <label class="block text-xs font-bold text-slate-300 mb-1.5">
                        <i class="fa-solid fa-lock text-blue-400 mr-1.5"></i> অ্যাডমিন পাসওয়ার্ড (Admin Password)
                    </label>
                    <div class="relative">
                        <input type="password" id="admin-pass-input" placeholder="পাসওয়ার্ড লিখুন" required
                               class="w-full px-4 py-2.5 rounded-xl bg-dark-900 border border-slate-700 text-white text-sm focus:outline-none focus:border-blue-500 font-mono pr-10">
                        <button type="button" onclick="togglePassVisibility('admin-pass-input')" class="absolute right-3.5 top-1/2 -translate-y-1/2 text-slate-400 hover:text-white">
                            <i class="fa-solid fa-eye-slash text-xs"></i>
                        </button>
                    </div>
                </div>
                <button type="submit" id="btn-admin-login"
                        class="w-full py-3 rounded-xl bg-[#2563eb] hover:bg-[#1d4ed8] text-white font-bold text-sm transition shadow-lg shadow-blue-500/30 flex items-center justify-center gap-2 mt-2">
                    <i class="fa-solid fa-shield-halved"></i> <span>অ্যাডমিন প্যানেলে প্রবেশ করুন</span>
                </button>
            </form>
            <div class="mt-6 pt-4 border-t border-slate-800/80">
                <a href="index.html" class="text-xs text-slate-400 hover:text-white transition flex items-center justify-center gap-1.5">
                    <i class="fa-solid fa-arrow-left"></i> <span>গ্রাহক স্টোর পেজে ফিরে যান</span>
                </a>
            </div>
        </div>
    </div>

    <!-- ============================================== -->
    <!-- TOP NAVIGATION BAR                             -->
    <!-- ============================================== -->
    <header class="bg-[#070a1a]/95 border-b border-blue-500/20 sticky top-0 z-40 backdrop-blur-md">
        <div class="max-w-7xl mx-auto px-3 sm:px-6 h-16 flex items-center justify-between">
            <!-- Brand & Badges -->
            <div class="flex items-center gap-2 sm:gap-3">
                <a href="index.html" class="flex items-center gap-2">
                    <img src="images/logo.png" alt="RRR Topup" class="h-8 object-contain"
                         onerror="this.src='https://apis.rrrtopup.com/uploads/images/1793198575181-1768754618825-logo0d22abf7_1.png'">
                </a>
                <span class="px-2 py-0.5 rounded-md bg-amber-500/20 text-amber-300 border border-amber-500/40 text-[10px] font-black uppercase tracking-wider flex items-center gap-1">
                    <i class="fa-solid fa-crown text-[9px]"></i> Super Admin
                </span>
                <span class="hidden lg:inline text-xs text-slate-400 font-mono">
                    <i class="fa-solid fa-user-shield text-amber-400 mr-1"></i> admin@mrtopup.com
                </span>
            </div>

            <!-- Convex Cloud Live Status & Action Controls -->
            <div class="flex items-center gap-2 sm:gap-3">
                <!-- Live Cloud Badge -->
                <div class="hidden sm:flex items-center gap-1.5 px-3 py-1 rounded-full bg-emerald-500/10 border border-emerald-500/30 text-[11px] text-emerald-400 font-semibold">
                    <span class="w-2 h-2 rounded-full bg-emerald-400 animate-ping"></span>
                    <span>Convex Live 🟢</span>
                </div>

                <!-- Auto Refresh Toggle Button -->
                <button onclick="toggleAutoSync()" id="btn-auto-sync"
                        class="px-2.5 py-1.5 rounded-xl bg-dark-800 border border-slate-700 text-slate-300 hover:text-white text-xs font-semibold transition flex items-center gap-1.5"
                        title="স্বয়ংক্রিয় রিফ্রেশ অন/অফ">
                    <i class="fa-solid fa-clock-rotate-left text-blue-400"></i>
                    <span class="hidden md:inline" id="auto-sync-text">Auto Sync (10s)</span>
                </button>

                <!-- Manual Refresh Button -->
                <button onclick="fetchAllData(true)" title="ডাটাবেস এখনই রিফ্রেশ করুন"
                        class="p-2 sm:px-3 sm:py-1.5 rounded-xl bg-dark-800 border border-blue-500/30 text-blue-300 hover:text-white hover:bg-blue-600 transition text-xs font-semibold flex items-center gap-1.5">
                    <i id="refresh-icon" class="fa-solid fa-arrows-rotate"></i>
                    <span class="hidden sm:inline">রিফ্রেশ</span>
                </button>

                <!-- View Store Button -->
                <a href="index.html" target="_blank"
                   class="px-3 py-1.5 rounded-xl bg-blue-600/20 border border-blue-500/40 text-blue-300 hover:bg-blue-600 hover:text-white transition text-xs font-semibold flex items-center gap-1.5">
                    <i class="fa-solid fa-arrow-up-right-from-square"></i>
                    <span class="hidden sm:inline">স্টোর</span>
                </a>

                <!-- Logout Button -->
                <button onclick="handleAdminLogout()" title="অ্যাডমিন লগআউট"
                        class="p-2 px-2.5 rounded-xl bg-rose-500/10 border border-rose-500/30 text-rose-400 hover:bg-rose-500 hover:text-white transition text-xs">
                    <i class="fa-solid fa-right-from-bracket"></i>
                </button>
            </div>
        </div>
    </header>

    <!-- ============================================== -->
    <!-- MAIN CONTENT CONTAINER                         -->
    <!-- ============================================== -->
    <main class="max-w-7xl w-full mx-auto px-3 sm:px-6 py-5 flex-1 flex flex-col gap-5">

        <!-- EXECUTIVE STATISTICS CARDS (5 Responsive Cards) -->
        <section class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-5 gap-2.5 sm:gap-4">
            <!-- 1. Total Revenue -->
            <div class="admin-card rounded-2xl p-4 border border-emerald-500/30 relative overflow-hidden">
                <div class="flex items-center justify-between text-slate-400 text-xs mb-1 font-semibold">
                    <span>মোট সেলস</span>
                    <i class="fa-solid fa-sack-dollar text-emerald-400 text-sm"></i>
                </div>
                <div id="stat-revenue" class="text-lg sm:text-2xl font-black text-white font-mono">৳ 0.00</div>
                <div class="text-[10px] text-emerald-400 mt-1 font-bold flex items-center gap-1">
                    <i class="fa-solid fa-circle-check"></i> কমপ্লিট অর্ডার
                </div>
            </div>

            <!-- 2. Total Orders -->
            <div class="admin-card rounded-2xl p-4 border border-blue-500/30 relative overflow-hidden">
                <div class="flex items-center justify-between text-slate-400 text-xs mb-1 font-semibold">
                    <span>মোট অর্ডার</span>
                    <i class="fa-solid fa-cart-shopping text-blue-400 text-sm"></i>
                </div>
                <div id="stat-orders" class="text-lg sm:text-2xl font-black text-white font-mono">0</div>
                <div class="text-[10px] text-slate-400 mt-1 font-medium">সমস্ত সফল ও প্রক্রিয়াধীন</div>
            </div>

            <!-- 3. Pending Orders -->
            <div class="admin-card rounded-2xl p-4 border border-amber-500/40 relative overflow-hidden">
                <div class="flex items-center justify-between text-slate-400 text-xs mb-1 font-semibold">
                    <span>পেন্ডিং অর্ডার</span>
                    <i class="fa-solid fa-hourglass-half text-amber-400 text-sm"></i>
                </div>
                <div id="stat-pending" class="text-lg sm:text-2xl font-black text-amber-400 font-mono">0</div>
                <div class="text-[10px] text-amber-300 mt-1 font-bold flex items-center gap-1">
                    <span class="w-1.5 h-1.5 rounded-full bg-amber-400 animate-ping"></span> ডেলিভারি অপেক্ষা করছে
                </div>
            </div>

            <!-- 4. Deposit Requests -->
            <div class="admin-card rounded-2xl p-4 border border-purple-500/40 relative overflow-hidden">
                <div class="flex items-center justify-between text-slate-400 text-xs mb-1 font-semibold">
                    <span>ডিপোজিট রিকোয়েস্ট</span>
                    <i class="fa-solid fa-money-bill-transfer text-purple-400 text-sm"></i>
                </div>
                <div id="stat-deposits" class="text-lg sm:text-2xl font-black text-purple-300 font-mono">0</div>
                <div class="text-[10px] text-purple-400 mt-1 font-bold">অ্যাড মানি পেন্ডিং</div>
            </div>

            <!-- 5. Registered Users & Wallets -->
            <div class="col-span-2 sm:col-span-1 admin-card rounded-2xl p-4 border border-cyan-500/30 relative overflow-hidden">
                <div class="flex items-center justify-between text-slate-400 text-xs mb-1 font-semibold">
                    <span>ইউজার ও ওয়ালেট</span>
                    <i class="fa-solid fa-users text-cyan-400 text-sm"></i>
                </div>
                <div class="flex items-baseline gap-2">
                    <span id="stat-users" class="text-lg sm:text-2xl font-black text-white font-mono">0</span>
                    <span class="text-xs text-slate-400">গেমার</span>
                </div>
                <div class="text-[10px] text-cyan-300 font-mono font-bold mt-1">
                    মোট ওয়ালেট: <span id="stat-wallet">৳ 0.00</span>
                </div>
            </div>
        </section>

        <!-- NAVIGATION TABS (5 Main Control Tabs) -->
        <div class="flex items-center gap-2 overflow-x-auto pb-1 border-b border-slate-800/80 custom-scrollbar">
            <button onclick="switchTab('orders')" id="tab-btn-orders"
                    class="tab-btn active px-3.5 sm:px-4 py-2 rounded-xl text-xs font-bold transition flex items-center gap-2 border border-transparent shrink-0">
                <i class="fa-solid fa-boxes-stacked"></i> <span>অর্ডার সমূহ (Orders)</span>
                <span id="badge-orders-count" class="px-1.5 py-0.2 rounded-full bg-white/20 text-[10px]">0</span>
            </button>
            <button onclick="switchTab('deposits')" id="tab-btn-deposits"
                    class="tab-btn px-3.5 sm:px-4 py-2 rounded-xl bg-dark-800 text-slate-300 hover:text-white border border-slate-700/60 text-xs font-semibold transition flex items-center gap-2 shrink-0">
                <i class="fa-solid fa-wallet"></i> <span>ডিপোজিট অনুমোদন (Deposits)</span>
                <span id="badge-deposits-count" class="px-1.5 py-0.2 rounded-full bg-purple-500/30 text-purple-300 text-[10px]">0</span>
            </button>
            <button onclick="switchTab('packages')" id="tab-btn-packages"
                    class="tab-btn px-3.5 sm:px-4 py-2 rounded-xl bg-dark-800 text-slate-300 hover:text-white border border-slate-700/60 text-xs font-semibold transition flex items-center gap-2 shrink-0">
                <i class="fa-solid fa-gem"></i> <span>ডায়মন্ড প্যাকেজ (Packages)</span>
            </button>
            <button onclick="switchTab('users')" id="tab-btn-users"
                    class="tab-btn px-3.5 sm:px-4 py-2 rounded-xl bg-dark-800 text-slate-300 hover:text-white border border-slate-700/60 text-xs font-semibold transition flex items-center gap-2 shrink-0">
                <i class="fa-solid fa-users-gear"></i> <span>ইউজার ও ওয়ালেট (Users)</span>
            </button>
            <button onclick="switchTab('settings')" id="tab-btn-settings"
                    class="tab-btn px-3.5 sm:px-4 py-2 rounded-xl bg-dark-800 text-slate-300 hover:text-white border border-slate-700/60 text-xs font-semibold transition flex items-center gap-2 shrink-0">
                <i class="fa-solid fa-sliders"></i> <span>সাইট সেটিংস ও নোটিশ (Settings)</span>
            </button>
        </div>


        <!-- ============================================== -->
        <!-- TAB 1: ORDERS MANAGEMENT                       -->
        <!-- ============================================== -->
        <section id="tab-orders" class="space-y-4">
            <!-- Filter Bar & Search -->
            <div class="flex flex-col md:flex-row items-stretch md:items-center justify-between gap-3">
                <!-- Status Filter Pills -->
                <div class="flex items-center gap-1.5 overflow-x-auto py-1 custom-scrollbar">
                    <button onclick="filterOrders('all')" id="filter-all" class="px-3 py-1.5 rounded-xl text-xs font-bold bg-blue-600 text-white shrink-0">সব (All)</button>
                    <button onclick="filterOrders('pending')" id="filter-pending" class="px-3 py-1.5 rounded-xl text-xs font-medium bg-dark-800 text-slate-300 hover:text-white border border-slate-700/50 shrink-0">⏳ পেন্ডিং</button>
                    <button onclick="filterOrders('processing')" id="filter-processing" class="px-3 py-1.5 rounded-xl text-xs font-medium bg-dark-800 text-slate-300 hover:text-white border border-slate-700/50 shrink-0">🔄 প্রসেসিং</button>
                    <button onclick="filterOrders('completed')" id="filter-completed" class="px-3 py-1.5 rounded-xl text-xs font-medium bg-dark-800 text-slate-300 hover:text-white border border-slate-700/50 shrink-0">✅ কমপ্লিট</button>
                    <button onclick="filterOrders('cancelled')" id="filter-cancelled" class="px-3 py-1.5 rounded-xl text-xs font-medium bg-dark-800 text-slate-300 hover:text-white border border-slate-700/50 shrink-0">❌ বাতিল</button>
                </div>

                <!-- Search Input & Export -->
                <div class="flex items-center gap-2">
                    <div class="relative flex-1 sm:w-72">
                        <i class="fa-solid fa-magnifying-glass absolute left-3 top-1/2 -translate-y-1/2 text-slate-400 text-xs"></i>
                        <input type="text" id="order-search" oninput="renderOrdersTable()" placeholder="অর্ডার আইডি, UID বা ফোন..."
                               class="w-full pl-9 pr-3 py-2 rounded-xl bg-dark-900 border border-slate-700 text-xs text-white placeholder-slate-500 focus:outline-none focus:border-blue-500 font-mono">
                    </div>
                    <button onclick="exportOrdersToCSV()" title="CSV রিপোর্ট ডাউনলোড করুন"
                            class="p-2 sm:px-3 sm:py-2 rounded-xl bg-dark-800 border border-slate-700 text-slate-300 hover:text-white hover:border-emerald-500/40 text-xs font-semibold transition shrink-0 flex items-center gap-1.5">
                        <i class="fa-solid fa-file-excel text-emerald-400"></i>
                        <span class="hidden sm:inline">Export</span>
                    </button>
                </div>
            </div>

            <!-- Orders Table Container -->
            <div class="admin-card rounded-2xl overflow-hidden border border-blue-500/20">
                <div class="overflow-x-auto custom-scrollbar">
                    <table class="w-full admin-table text-left border-collapse">
                        <thead>
                            <tr>
                                <th>অর্ডার আইডি</th>
                                <th>প্লেয়ার UID</th>
                                <th>প্যাকেজ ও বিবরণ</th>
                                <th>মূল্য (৳ BDT)</th>
                                <th>পেমেন্ট মেথড ও TrxID</th>
                                <th>অর্ডার সময়</th>
                                <th>স্ট্যাটাস</th>
                                <th class="text-right">একশন</th>
                            </tr>
                        </thead>
                        <tbody id="orders-tbody">
                            <tr>
                                <td colspan="8" class="text-center py-8 text-slate-400 text-xs">
                                    <i class="fa-solid fa-spinner fa-spin mr-2"></i> ডাটাবেস থেকে অর্ডার লোড হচ্ছে...
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </section>


        <!-- ============================================== -->
        <!-- TAB 2: DEPOSITS & ADD MONEY APPROVAL           -->
        <!-- ============================================== -->
        <section id="tab-deposits" class="hidden space-y-4">
            <div class="flex flex-col sm:flex-row items-stretch sm:items-center justify-between gap-3">
                <div>
                    <h3 class="text-sm font-bold text-white flex items-center gap-2">
                        <i class="fa-solid fa-wallet text-purple-400"></i> গ্রাহকদের ডিপোজিট ও অ্যাড মানি রিকোয়েস্ট
                    </h3>
                    <p class="text-xs text-slate-400">TrxID যাচাই করে ওয়ালেটে স্বয়ংক্রিয়ভাবে ব্যালেন্স যোগ করুন</p>
                </div>
                <div class="flex items-center gap-2">
                    <button onclick="openManualDepositModal()"
                            class="px-3.5 py-2 rounded-xl bg-purple-600 hover:bg-purple-500 text-white font-bold text-xs transition flex items-center gap-1.5 shadow-lg shadow-purple-600/20">
                        <i class="fa-solid fa-plus"></i> <span>ম্যানুয়াল অ্যাড মানি</span>
                    </button>
                </div>
            </div>

            <!-- Deposit Search & Filter -->
            <div class="flex items-center justify-between gap-3">
                <div class="flex items-center gap-1.5 overflow-x-auto py-1">
                    <button onclick="filterDeposits('all')" id="dep-filter-all" class="px-3 py-1.5 rounded-xl text-xs font-bold bg-purple-600 text-white">সব (All)</button>
                    <button onclick="filterDeposits('pending')" id="dep-filter-pending" class="px-3 py-1.5 rounded-xl text-xs font-medium bg-dark-800 text-slate-300 hover:text-white border border-slate-700/50">⏳ পেন্ডিং</button>
                    <button onclick="filterDeposits('completed')" id="dep-filter-completed" class="px-3 py-1.5 rounded-xl text-xs font-medium bg-dark-800 text-slate-300 hover:text-white border border-slate-700/50">✅ অনুমোদিত</button>
                </div>
                <div class="relative w-64">
                    <i class="fa-solid fa-magnifying-glass absolute left-3 top-1/2 -translate-y-1/2 text-slate-400 text-xs"></i>
                    <input type="text" id="deposit-search" oninput="renderDepositsTable()" placeholder="TrxID বা মোবাইল নম্বর..."
                           class="w-full pl-9 pr-3 py-1.5 rounded-xl bg-dark-900 border border-slate-700 text-xs text-white placeholder-slate-500 focus:outline-none focus:border-purple-500 font-mono">
                </div>
            </div>

            <!-- Deposits Table -->
            <div class="admin-card rounded-2xl overflow-hidden border border-purple-500/20">
                <div class="overflow-x-auto custom-scrollbar">
                    <table class="w-full admin-table text-left border-collapse">
                        <thead>
                            <tr>
                                <th>TrxID (ট্রানজেকশন আইডি)</th>
                                <th>গ্রাহকের ফোন নম্বর</th>
                                <th>পেমেন্ট মেথড</th>
                                <th>টাকার পরিমাণ (৳)</th>
                                <th>রিকোয়েস্ট তারিখ</th>
                                <th>স্ট্যাটাস</th>
                                <th class="text-right">একশন</th>
                            </tr>
                        </thead>
                        <tbody id="deposits-tbody">
                            <tr>
                                <td colspan="7" class="text-center py-8 text-slate-400 text-xs">
                                    <i class="fa-solid fa-spinner fa-spin mr-2"></i> ডিপোজিট রিকোয়েস্ট লোড হচ্ছে...
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </section>


        <!-- ============================================== -->
        <!-- TAB 3: PACKAGES & RATES                        -->
        <!-- ============================================== -->
        <section id="tab-packages" class="hidden space-y-4">
            <div class="flex items-center justify-between">
                <div>
                    <h3 class="text-sm font-bold text-white flex items-center gap-2">
                        <i class="fa-solid fa-gem text-cyan-400"></i> Free Fire ডায়মন্ড ও মেম্বারশিপ প্যাকেজ
                    </h3>
                    <p class="text-xs text-slate-400">সরাসরি মূল্য ও স্টক স্ট্যাটাস আপডেট করুন</p>
                </div>
                <button onclick="openAddPackageModal()"
                        class="px-3.5 py-2 rounded-xl bg-[#2563eb] hover:bg-[#1d4ed8] text-white font-bold text-xs transition flex items-center gap-1.5 shadow-lg shadow-blue-500/20">
                    <i class="fa-solid fa-plus"></i> <span>নতুন প্যাকেজ যোগ করুন</span>
                </button>
            </div>

            <div class="admin-card rounded-2xl overflow-hidden border border-blue-500/20">
                <div class="overflow-x-auto custom-scrollbar">
                    <table class="w-full admin-table text-left border-collapse">
                        <thead>
                            <tr>
                                <th>প্যাকেজের নাম</th>
                                <th>ডায়মন্ড / ট্যাগ</th>
                                <th>মূল্য (৳ BDT)</th>
                                <th>স্টক স্ট্যাটাস</th>
                                <th class="text-right">একশন</th>
                            </tr>
                        </thead>
                        <tbody id="packages-tbody">
                            <tr>
                                <td colspan="5" class="text-center py-8 text-slate-400 text-xs">
                                    <i class="fa-solid fa-spinner fa-spin mr-2"></i> প্যাকেজ লোড হচ্ছে...
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </section>


        <!-- ============================================== -->
        <!-- TAB 4: USERS & WALLET MANAGEMENT               -->
        <!-- ============================================== -->
        <section id="tab-users" class="hidden space-y-4">
            <div class="flex flex-col sm:flex-row items-stretch sm:items-center justify-between gap-3">
                <div>
                    <h3 class="text-sm font-bold text-white flex items-center gap-2">
                        <i class="fa-solid fa-users text-cyan-400"></i> নিবন্ধিত ইউজার তালিকা ও ওয়ালেট ব্যালেন্স
                    </h3>
                    <p class="text-xs text-slate-400">গ্রাহকদের অ্যাকাউন্ট তথ্য ও ওয়ালেট নিয়ন্ত্রণ করুন</p>
                </div>
                <div class="relative w-full sm:w-64">
                    <i class="fa-solid fa-magnifying-glass absolute left-3 top-1/2 -translate-y-1/2 text-slate-400 text-xs"></i>
                    <input type="text" id="user-search" oninput="renderUsersTable()" placeholder="নাম বা মোবাইল নম্বর..."
                           class="w-full pl-9 pr-3 py-1.5 rounded-xl bg-dark-900 border border-slate-700 text-xs text-white placeholder-slate-500 focus:outline-none focus:border-blue-500 font-mono">
                </div>
            </div>

            <div class="admin-card rounded-2xl overflow-hidden border border-blue-500/20">
                <div class="overflow-x-auto custom-scrollbar">
                    <table class="w-full admin-table text-left border-collapse">
                        <thead>
                            <tr>
                                <th>ইউজার নাম</th>
                                <th>মোবাইল নম্বর</th>
                                <th>ইমেইল</th>
                                <th>বর্তমান ব্যালেন্স</th>
                                <th>নিবন্ধন তারিখ</th>
                                <th class="text-right">ওয়ালেট একশন</th>
                            </tr>
                        </thead>
                        <tbody id="users-tbody">
                            <tr>
                                <td colspan="6" class="text-center py-8 text-slate-400 text-xs">
                                    <i class="fa-solid fa-spinner fa-spin mr-2"></i> ইউজার লোড হচ্ছে...
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </section>


        <!-- ============================================== -->
        <!-- TAB 5: SYSTEM SETTINGS, NOTICES & SECURITY     -->
        <!-- ============================================== -->
        <section id="tab-settings" class="hidden space-y-4">
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">

                <!-- Site Notice & Announcements Manager -->
                <div class="admin-card rounded-2xl p-6 border border-blue-500/30 space-y-4">
                    <div class="flex items-center justify-between">
                        <h4 class="text-sm font-bold text-white flex items-center gap-2">
                            <i class="fa-solid fa-bullhorn text-cyan-400"></i> নোটিশ ব্যানার ও ঘোষণা
                        </h4>
                        <span class="px-2 py-0.5 rounded-full bg-cyan-500/20 text-cyan-300 border border-cyan-500/40 text-[10px] font-bold">LIVE MARQUEE</span>
                    </div>

                    <form onsubmit="handleSaveNotice(event)" class="space-y-3">
                        <div>
                            <label class="block text-xs font-semibold text-slate-300 mb-1">হোম পেজের নোটিশ টেক্সট</label>
                            <textarea id="setting-notice-text" rows="3" required
                                      class="w-full px-3.5 py-2.5 rounded-xl bg-dark-900 border border-slate-700 text-xs text-white focus:outline-none focus:border-blue-500 resize-none">ফ্রি ফায়ার ডায়মন্ড টপআপ করতে পারবেন, মাত্র ০৫ সেকেন্ডে রোবটের মাধ্যমে ইনস্ট্যান্ট ডেলিভারি দেওয়া হয়! যেকোনো প্রয়োজনে টেলিগ্রাম সাপোর্টে মেসেজ দিন।</textarea>
                        </div>
                        <button type="submit" class="w-full py-2.5 rounded-xl bg-[#2563eb] hover:bg-[#1d4ed8] text-white font-bold text-xs transition shadow-md">
                            নোটিশ আপডেট করুন
                        </button>
                    </form>
                </div>

                <!-- Payment Numbers Manager -->
                <div class="admin-card rounded-2xl p-6 border border-emerald-500/30 space-y-4">
                    <div class="flex items-center justify-between">
                        <h4 class="text-sm font-bold text-white flex items-center gap-2">
                            <i class="fa-solid fa-credit-card text-emerald-400"></i> পেমেন্ট মেথড নম্বর সেটিংস
                        </h4>
                        <span class="px-2 py-0.5 rounded-full bg-emerald-500/20 text-emerald-300 border border-emerald-500/40 text-[10px] font-bold">ACCOUNTS</span>
                    </div>

                    <form onsubmit="handleSavePaymentNumbers(event)" class="space-y-3">
                        <div>
                            <label class="block text-xs font-semibold text-slate-300 mb-1">বিকাশ পার্সোনাল নম্বর (Send Money)</label>
                            <input type="text" id="setting-bkash-no" value="01889123456" required
                                   class="w-full px-3.5 py-2 rounded-xl bg-dark-900 border border-slate-700 text-xs text-white font-mono focus:outline-none focus:border-emerald-500">
                        </div>
                        <div>
                            <label class="block text-xs font-semibold text-slate-300 mb-1">নগদ পার্সোনাল নম্বর (Send Money)</label>
                            <input type="text" id="setting-nagad-no" value="01889123456" required
                                   class="w-full px-3.5 py-2 rounded-xl bg-dark-900 border border-slate-700 text-xs text-white font-mono focus:outline-none focus:border-orange-500">
                        </div>
                        <button type="submit" class="w-full py-2.5 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs transition shadow-md">
                            পেমেন্ট নম্বর সেভ করুন
                        </button>
                    </form>
                </div>

                <!-- Admin Security & Password Change -->
                <div class="admin-card rounded-2xl p-6 border border-amber-500/30 space-y-4">
                    <div class="flex items-center justify-between">
                        <h4 class="text-sm font-bold text-white flex items-center gap-2">
                            <i class="fa-solid fa-key text-amber-400"></i> অ্যাডমিন পাসওয়ার্ড পরিবর্তন
                        </h4>
                        <span class="text-amber-400 font-bold uppercase text-[10px] bg-amber-500/20 px-2 py-0.5 rounded">Security</span>
                    </div>

                    <div class="p-3 rounded-xl bg-dark-900 border border-slate-800 space-y-1 text-xs">
                        <div class="flex items-center justify-between">
                            <span class="text-slate-400">অ্যাডমিন ইমেইল:</span>
                            <span class="font-mono text-emerald-400 font-bold">admin@mrtopup.com</span>
                        </div>
                    </div>

                    <form onsubmit="handleAdminPasswordChange(event)" class="space-y-3">
                        <div>
                            <label class="block text-xs font-semibold text-slate-300 mb-1">নতুন অ্যাডমিন পাসওয়ার্ড</label>
                            <input type="password" id="new-admin-pass" required placeholder="কমপক্ষে ৬ অক্ষরের পাসওয়ার্ড"
                                   class="w-full px-3.5 py-2 rounded-xl bg-dark-900 border border-slate-700 text-xs text-white focus:outline-none focus:border-amber-500">
                        </div>
                        <button type="submit" class="w-full py-2.5 rounded-xl bg-amber-600 hover:bg-amber-500 text-white font-bold text-xs transition shadow-md">
                            পাসওয়ার্ড আপডেট করুন
                        </button>
                    </form>
                </div>

                <!-- Convex Cloud Diagnostics & Latency -->
                <div class="admin-card rounded-2xl p-6 border border-blue-500/30 space-y-4">
                    <div class="flex items-center justify-between">
                        <h4 class="text-sm font-bold text-white flex items-center gap-2">
                            <i class="fa-solid fa-cloud text-blue-400"></i> Convex Cloud ডাটাবেস লিংক
                        </h4>
                        <span class="px-2 py-0.5 rounded-full bg-emerald-500/20 text-emerald-400 border border-emerald-500/40 text-[10px] font-bold">ACTIVE</span>
                    </div>

                    <div class="space-y-2 text-xs">
                        <div class="flex items-center justify-between p-2.5 rounded-xl bg-dark-900 border border-slate-800">
                            <span class="text-slate-400">Deployment:</span>
                            <span class="font-mono text-blue-300 font-bold">quixotic-cuttlefish-352</span>
                        </div>
                        <div class="flex items-center justify-between p-2.5 rounded-xl bg-dark-900 border border-slate-800">
                            <span class="text-slate-400">Latency:</span>
                            <span id="cloud-ping-val" class="font-mono text-emerald-400 font-bold">~45ms</span>
                        </div>
                    </div>

                    <div class="pt-2 flex items-center gap-2">
                        <a href="https://dashboard.convex.dev/t/mohammad-rifat/test/quixotic-cuttlefish-352/settings" target="_blank"
                           class="flex-1 py-2.5 rounded-xl bg-[#2563eb] hover:bg-[#1d4ed8] text-white font-bold text-xs text-center transition flex items-center justify-center gap-1.5 shadow-md">
                            <i class="fa-solid fa-arrow-up-right-from-square"></i> Convex Dashboard
                        </a>
                        <button onclick="pingCloudLatency()" class="py-2.5 px-3.5 rounded-xl bg-dark-800 hover:bg-dark-700 text-slate-300 text-xs font-semibold transition border border-slate-700">
                            <i class="fa-solid fa-bolt text-amber-400"></i> Ping
                        </button>
                    </div>
                </div>

            </div>
        </section>

    </main>

    <!-- ============================================== -->
    <!-- MODALS & POPUPS                                -->
    <!-- ============================================== -->

    <!-- MODAL 1: ADJUST USER WALLET -->
    <div id="modal-wallet" class="hidden fixed inset-0 z-50 bg-black/80 backdrop-blur-sm flex items-center justify-center p-4">
        <div class="max-w-sm w-full admin-card rounded-3xl p-6 border border-blue-500/40 shadow-2xl">
            <div class="flex items-center justify-between mb-4">
                <h4 class="text-sm font-bold text-white flex items-center gap-2">
                    <i class="fa-solid fa-coins text-purple-400"></i> ওয়ালেট ব্যালেন্স অ্যাডজাস্ট
                </h4>
                <button onclick="closeModal('modal-wallet')" class="text-slate-400 hover:text-white"><i class="fa-solid fa-xmark"></i></button>
            </div>
            <div class="space-y-3.5 text-xs">
                <div class="p-3 rounded-xl bg-dark-900 border border-slate-800 space-y-1">
                    <p class="text-slate-300">ইউজার: <span id="wallet-modal-user" class="font-bold text-white"></span></p>
                    <p class="text-slate-300">বর্তমান ব্যালেন্স: <span id="wallet-modal-curr" class="font-mono text-emerald-400 font-bold"></span></p>
                </div>
                
                <div>
                    <label class="block text-slate-300 font-semibold mb-1">একশন টাইপ</label>
                    <select id="wallet-action-type" class="w-full px-3.5 py-2.5 rounded-xl bg-dark-900 border border-slate-700 text-white font-medium focus:outline-none focus:border-blue-500">
                        <option value="add">টাকা যোগ করুন (+ Add)</option>
                        <option value="deduct">টাকা কর্তন করুন (- Deduct)</option>
                        <option value="set">নির্দিষ্ট পরিমাণ সেট করুন (= Set)</option>
                    </select>
                </div>

                <div>
                    <label class="block text-slate-300 font-semibold mb-1">টাকার পরিমাণ (৳ BDT)</label>
                    <input type="number" id="wallet-amount-input" min="1" placeholder="যেমন: 100"
                           class="w-full px-3.5 py-2.5 rounded-xl bg-dark-900 border border-slate-700 text-white font-mono focus:outline-none focus:border-blue-500">
                </div>

                <button onclick="submitWalletAdjustment()" class="w-full py-2.5 rounded-xl bg-[#2563eb] hover:bg-[#1d4ed8] text-white font-bold text-xs transition shadow-lg mt-2">
                    ব্যালেন্স সংরক্ষণ করুন
                </button>
            </div>
        </div>
    </div>

    <!-- MODAL 2: ADD NEW DIAMOND PACKAGE -->
    <div id="modal-package" class="hidden fixed inset-0 z-50 bg-black/80 backdrop-blur-sm flex items-center justify-center p-4">
        <div class="max-w-md w-full admin-card rounded-3xl p-6 border border-blue-500/40 shadow-2xl">
            <div class="flex items-center justify-between mb-4">
                <h4 class="text-sm font-bold text-white flex items-center gap-2">
                    <i class="fa-solid fa-gem text-blue-400"></i> নতুন ডায়মন্ড প্যাকেজ যোগ করুন
                </h4>
                <button onclick="closeModal('modal-package')" class="text-slate-400 hover:text-white"><i class="fa-solid fa-xmark"></i></button>
            </div>
            <form onsubmit="submitNewPackage(event)" class="space-y-3.5 text-xs">
                <div>
                    <label class="block text-slate-300 font-semibold mb-1">প্যাকেজের নাম</label>
                    <input type="text" id="pkg-name" required placeholder="যেমন: 115 Daimond💎 বা Monthly"
                           class="w-full px-3.5 py-2.5 rounded-xl bg-dark-900 border border-slate-700 text-white focus:outline-none focus:border-blue-500">
                </div>
                <div>
                    <label class="block text-slate-300 font-semibold mb-1">ট্যাগ / ডায়মন্ড সংখ্যা</label>
                    <input type="text" id="pkg-tag" placeholder="যেমন: 115 বা 30 Days"
                           class="w-full px-3.5 py-2.5 rounded-xl bg-dark-900 border border-slate-700 text-white focus:outline-none focus:border-blue-500">
                </div>
                <div>
                    <label class="block text-slate-300 font-semibold mb-1">মূল্য (৳ BDT)</label>
                    <input type="number" id="pkg-price" required min="1" placeholder="যেমন: 78"
                           class="w-full px-3.5 py-2.5 rounded-xl bg-dark-900 border border-slate-700 text-white font-mono focus:outline-none focus:border-blue-500">
                </div>
                <button type="submit" class="w-full py-2.5 rounded-xl bg-[#2563eb] hover:bg-[#1d4ed8] text-white font-bold text-xs transition shadow-lg mt-2">
                    প্যাকেজ সেভ করুন
                </button>
            </form>
        </div>
    </div>

    <!-- MODAL 3: MANUAL DEPOSIT ENTRY -->
    <div id="modal-manual-deposit" class="hidden fixed inset-0 z-50 bg-black/80 backdrop-blur-sm flex items-center justify-center p-4">
        <div class="max-w-md w-full admin-card rounded-3xl p-6 border border-purple-500/40 shadow-2xl">
            <div class="flex items-center justify-between mb-4">
                <h4 class="text-sm font-bold text-white flex items-center gap-2">
                    <i class="fa-solid fa-plus-circle text-purple-400"></i> ম্যানুয়াল ডিপোজিট এন্ট্রি
                </h4>
                <button onclick="closeModal('modal-manual-deposit')" class="text-slate-400 hover:text-white"><i class="fa-solid fa-xmark"></i></button>
            </div>
            <form onsubmit="submitManualDeposit(event)" class="space-y-3.5 text-xs">
                <div>
                    <label class="block text-slate-300 font-semibold mb-1">গ্রাহকের মোবাইল নম্বর</label>
                    <input type="tel" id="man-dep-phone" required placeholder="01XXXXXXXXX"
                           class="w-full px-3.5 py-2.5 rounded-xl bg-dark-900 border border-slate-700 text-white font-mono focus:outline-none focus:border-purple-500">
                </div>
                <div>
                    <label class="block text-slate-300 font-semibold mb-1">টাকার পরিমাণ (৳ BDT)</label>
                    <input type="number" id="man-dep-amount" required min="1" placeholder="যেমন: 500"
                           class="w-full px-3.5 py-2.5 rounded-xl bg-dark-900 border border-slate-700 text-white font-mono focus:outline-none focus:border-purple-500">
                </div>
                <div>
                    <label class="block text-slate-300 font-semibold mb-1">পেমেন্ট মেথড</label>
                    <select id="man-dep-method" class="w-full px-3.5 py-2.5 rounded-xl bg-dark-900 border border-slate-700 text-white focus:outline-none focus:border-purple-500">
                        <option value="bKash">bKash (Send Money)</option>
                        <option value="Nagad">Nagad (Send Money)</option>
                        <option value="Admin Manual">Admin Manual / Cash</option>
                    </select>
                </div>
                <div>
                    <label class="block text-slate-300 font-semibold mb-1">TrxID (ঐচ্ছিক)</label>
                    <input type="text" id="man-dep-trx" placeholder="যেমন: 9J87K2L1"
                           class="w-full px-3.5 py-2.5 rounded-xl bg-dark-900 border border-slate-700 text-white font-mono uppercase focus:outline-none focus:border-purple-500">
                </div>
                <button type="submit" class="w-full py-2.5 rounded-xl bg-purple-600 hover:bg-purple-500 text-white font-bold text-xs transition shadow-lg mt-2">
                    ডিপোজিট নিশ্চিত ও ওয়ালেটে জমা করুন
                </button>
            </form>
        </div>
    </div>


    <!-- ============================================== -->
    <!-- JAVASCRIPT LOGIC & CONVEX INTEGRATION          -->
    <!-- ============================================== -->
    <script>
        const CONVEX_CLOUD_URL = "https://quixotic-cuttlefish-352.convex.cloud";
        const CONVEX_SITE_URL = "https://quixotic-cuttlefish-352.convex.site";

        const convex = {
            query: async function(path, args = {}) {
                try {
                    const res = await fetch(`${CONVEX_CLOUD_URL}/api/query`, {
                        method: "POST",
                        headers: { "Content-Type": "application/json" },
                        body: JSON.stringify({ path, args })
                    });
                    const data = await res.json();
                    if (data.status === "success") return data.value;
                    return null;
                } catch(e) {
                    console.error("Convex query failed:", e);
                    return null;
                }
            },
            mutation: async function(path, args = {}) {
                try {
                    const res = await fetch(`${CONVEX_CLOUD_URL}/api/mutation`, {
                        method: "POST",
                        headers: { "Content-Type": "application/json" },
                        body: JSON.stringify({ path, args })
                    });
                    const data = await res.json();
                    if (data.status === "success") return data.value;
                    return null;
                } catch(e) {
                    console.error("Convex mutation failed:", e);
                    return null;
                }
            }
        };

        // Application State
        let allOrders = [];
        let allDeposits = [];
        let allPackages = [];
        let allUsers = [];
        let currentOrderFilter = 'all';
        let currentDepositFilter = 'all';
        let selectedUserId = null;
        let autoSyncTimer = null;
        let isAutoSyncActive = false;

        // Toast Notification System
        function showToast(message, type = "success") {
            const container = document.getElementById("toast-container");
            if (!container) return;
            const toast = document.createElement("div");
            toast.className = `p-3 rounded-2xl text-xs font-bold text-white shadow-2xl flex items-center gap-2 border pointer-events-auto toast-notify ${
                type === 'success' ? 'bg-emerald-600/90 border-emerald-400' :
                type === 'error' ? 'bg-rose-600/90 border-rose-400' : 'bg-blue-600/90 border-blue-400'
            }`;
            toast.innerHTML = `
                <i class="fa-solid ${type === 'success' ? 'fa-circle-check' : type === 'error' ? 'fa-triangle-exclamation' : 'fa-info-circle'} text-sm"></i>
                <span class="flex-1">${message}</span>
            `;
            container.appendChild(toast);
            setTimeout(() => {
                toast.style.opacity = '0';
                toast.style.transition = 'opacity 0.4s ease';
                setTimeout(() => toast.remove(), 400);
            }, 3000);
        }

        // Admin Security & Authentication
        function checkAdminAuth() {
            const isAuth = sessionStorage.getItem("rrrtopup_admin_auth");
            const overlay = document.getElementById("login-overlay");
            if (isAuth === "true") {
                if (overlay) overlay.classList.add("hidden");
                fetchAllData();
                startAutoSync();
            } else {
                if (overlay) overlay.classList.remove("hidden");
            }
        }

        async function handleAdminLogin(e) {
            e.preventDefault();
            const btn = document.getElementById("btn-admin-login");
            const email = (document.getElementById("admin-email-input").value || "").trim().toLowerCase();
            const pass = document.getElementById("admin-pass-input").value;
            const targetEmail = (localStorage.getItem("rrrtopup_admin_email") || "").toLowerCase();
            const targetPass = localStorage.getItem("rrrtopup_admin_password") || "";

            btn.disabled = true;
            btn.innerHTML = `<i class="fa-solid fa-spinner fa-spin"></i> <span>যাচাই করা হচ্ছে...</span>`;

            // Check Convex Auth mutation or local admin credentials
            let authenticated = (email === targetEmail && pass === targetPass);
            if (!authenticated) {
                try {
                    const res = await convex.mutation("auth:signIn", { identifier: email, password: pass });
                    if (res && res.success && res.user && res.user.role === "admin") {
                        authenticated = true;
                    }
                } catch(err) {}
            }

            if (authenticated) {
                sessionStorage.setItem("rrrtopup_admin_auth", "true");
                sessionStorage.setItem("rrrtopup_admin_email", email);
                document.getElementById("login-overlay").classList.add("hidden");
                showToast("স্বাগতম অ্যাডমিন! প্যানেলে সফলভাবে লগইন হয়েছে।");
                fetchAllData();
                startAutoSync();
            } else {
                const err = document.getElementById("login-error");
                document.getElementById("login-error-text").textContent = "ভুল অ্যাডমিন ইমেইল বা পাসওয়ার্ড! অনুগ্রহ করে সঠিক তথ্য দিন।";
                err.classList.remove("hidden");
                btn.disabled = false;
                btn.innerHTML = `<i class="fa-solid fa-shield-halved"></i> <span>অ্যাডমিন প্যানেলে প্রবেশ করুন</span>`;
            }
        }

        function handleAdminLogout() {
            if (confirm("আপনি কি নিশ্চিত অ্যাডমিন প্যানেল থেকে লগআউট করতে চান?")) {
                sessionStorage.removeItem("rrrtopup_admin_auth");
                window.location.reload();
            }
        }

        function togglePassVisibility(id) {
            const el = document.getElementById(id);
            if (el) el.type = el.type === "password" ? "text" : "password";
        }

        async function handleAdminPasswordChange(e) {
            e.preventDefault();
            const p = document.getElementById("new-admin-pass").value;
            if (p.length < 6) {
                alert("পাসওয়ার্ড কমপক্ষে ৬ অক্ষরের হতে হবে!");
                return;
            }
            localStorage.setItem("rrrtopup_admin_password", p);
            
            // Sync with Convex database
            try {
                await convex.mutation("users:setAdmin", { email: "admin@mrtopup.com", password: p });
            } catch(e) {}

            showToast("অ্যাডমিন পাসওয়ার্ড সফলভাবে আপডেট করা হয়েছে!");
            document.getElementById("new-admin-pass").value = "";
        }

        // Tab Switching
        function switchTab(tabId) {
            ['orders', 'deposits', 'packages', 'users', 'settings'].forEach(t => {
                const sec = document.getElementById(`tab-${t}`);
                const btn = document.getElementById(`tab-btn-${t}`);
                if (t === tabId) {
                    if (sec) sec.classList.remove("hidden");
                    if (btn) btn.className = "tab-btn active px-3.5 sm:px-4 py-2 rounded-xl text-xs font-bold transition flex items-center gap-2 border border-transparent shrink-0";
                } else {
                    if (sec) sec.classList.add("hidden");
                    if (btn) btn.className = "tab-btn px-3.5 sm:px-4 py-2 rounded-xl bg-dark-800 text-slate-300 hover:text-white border border-slate-700/60 text-xs font-semibold transition flex items-center gap-2 shrink-0";
                }
            });
        }

        // Auto Sync Logic
        function startAutoSync() {
            isAutoSyncActive = true;
            if (autoSyncTimer) clearInterval(autoSyncTimer);
            autoSyncTimer = setInterval(() => {
                fetchAllData(false);
            }, 10000);
            updateAutoSyncBtnUI();
        }

        function stopAutoSync() {
            isAutoSyncActive = false;
            if (autoSyncTimer) clearInterval(autoSyncTimer);
            updateAutoSyncBtnUI();
        }

        function toggleAutoSync() {
            if (isAutoSyncActive) {
                stopAutoSync();
                showToast("Auto-Sync বন্ধ করা হয়েছে।", "info");
            } else {
                startAutoSync();
                showToast("Auto-Sync (10s) চালু করা হয়েছে।", "success");
            }
        }

        function updateAutoSyncBtnUI() {
            const btn = document.getElementById("btn-auto-sync");
            const text = document.getElementById("auto-sync-text");
            if (!btn || !text) return;
            if (isAutoSyncActive) {
                btn.className = "px-2.5 py-1.5 rounded-xl bg-emerald-500/20 border border-emerald-500/50 text-emerald-300 text-xs font-semibold transition flex items-center gap-1.5";
                text.textContent = "Auto Sync: ON 🟢";
            } else {
                btn.className = "px-2.5 py-1.5 rounded-xl bg-dark-800 border border-slate-700 text-slate-300 hover:text-white text-xs font-semibold transition flex items-center gap-1.5";
                text.textContent = "Auto Sync: OFF";
            }
        }

        // Fetch All Data from Convex Cloud Database
        async function fetchAllData(showToastMsg = false) {
            const icon = document.getElementById("refresh-icon");
            if (icon) icon.classList.add("fa-spin");

            try {
                const [orders, deposits, pkgs, users] = await Promise.all([
                    convex.query("orders:listAll"),
                    convex.query("wallet:listAll"),
                    convex.query("packages:listAll"),
                    convex.query("users:listAll")
                ]);

                allOrders = orders || [];
                allDeposits = deposits || [];
                allPackages = pkgs || [];
                allUsers = users || [];

                updateStats();
                renderOrdersTable();
                renderDepositsTable();
                renderPackagesTable();
                renderUsersTable();

                if (showToastMsg) {
                    showToast("Convex Cloud Database থেকে সফলভাবে সমস্ত ডাটা সিঙ্ক হয়েছে!");
                }
            } catch(e) {
                console.error("Data fetch error:", e);
            } finally {
                if (icon) icon.classList.remove("fa-spin");
            }
        }

        // Update Executive Dashboard Metric Cards
        function updateStats() {
            // Revenue
            const completed = allOrders.filter(o => o.status === "completed");
            const rev = completed.reduce((sum, o) => sum + (parseFloat(o.amount) || 0), 0);
            document.getElementById("stat-revenue").textContent = "৳ " + rev.toFixed(2);

            // Orders count & pending
            document.getElementById("stat-orders").textContent = allOrders.length;
            const pendingOrders = allOrders.filter(o => o.status === "pending" || o.status === "processing").length;
            document.getElementById("stat-pending").textContent = pendingOrders;
            document.getElementById("badge-orders-count").textContent = pendingOrders > 0 ? `${pendingOrders} Pending` : allOrders.length;

            // Deposits count & pending
            const pendingDeposits = allDeposits.filter(d => d.status === "pending").length;
            document.getElementById("stat-deposits").textContent = pendingDeposits;
            document.getElementById("badge-deposits-count").textContent = pendingDeposits > 0 ? `${pendingDeposits} New` : allDeposits.length;

            // Users & Total Wallet
            document.getElementById("stat-users").textContent = allUsers.length;
            const totalWallet = allUsers.reduce((sum, u) => sum + (parseFloat(u.balance) || 0), 0);
            document.getElementById("stat-wallet").textContent = "৳ " + totalWallet.toFixed(2);
        }

        // ==============================================
        // ORDERS TABLE & ACTIONS
        // ==============================================
        function renderOrdersTable() {
            const tbody = document.getElementById("orders-tbody");
            const q = (document.getElementById("order-search").value || "").toLowerCase().trim();

            let filtered = allOrders;
            if (currentOrderFilter !== "all") {
                filtered = filtered.filter(o => (o.status || "").toLowerCase() === currentOrderFilter);
            }
            if (q) {
                filtered = filtered.filter(o =>
                    (o.order_id || "").toLowerCase().includes(q) ||
                    (o.player_uid || "").toLowerCase().includes(q) ||
                    (o.package_name || "").toLowerCase().includes(q) ||
                    (o.sender_number || "").toLowerCase().includes(q) ||
                    (o.trx_id || "").toLowerCase().includes(q)
                );
            }

            if (filtered.length === 0) {
                tbody.innerHTML = `<tr><td colspan="8" class="text-center py-8 text-slate-500 text-xs">কোনো অর্ডার পাওয়া যায়নি।</td></tr>`;
                return;
            }

            tbody.innerHTML = filtered.map(o => {
                const st = (o.status || "completed").toLowerCase();
                let statusBadge = '';
                if (st === "completed") {
                    statusBadge = `<span class="px-2 py-0.5 rounded-full text-[10px] font-bold bg-emerald-500/20 text-emerald-400 border border-emerald-500/40">COMPLETED</span>`;
                } else if (st === "pending") {
                    statusBadge = `<span class="px-2 py-0.5 rounded-full text-[10px] font-bold bg-amber-500/20 text-amber-400 border border-amber-500/40 animate-pulse">PENDING</span>`;
                } else if (st === "processing") {
                    statusBadge = `<span class="px-2 py-0.5 rounded-full text-[10px] font-bold bg-blue-500/20 text-blue-400 border border-blue-500/40">PROCESSING</span>`;
                } else {
                    statusBadge = `<span class="px-2 py-0.5 rounded-full text-[10px] font-bold bg-rose-500/20 text-rose-400 border border-rose-500/40">${st.toUpperCase()}</span>`;
                }

                const dateStr = o.created_at ? new Date(o.created_at).toLocaleString() : new Date(o._creationTime).toLocaleString();

                return `
                    <tr>
                        <td class="font-mono font-bold text-white text-xs">${o.order_id}</td>
                        <td class="font-mono text-cyan-300 font-bold">
                            ${o.player_uid}
                            <button onclick="copyText('${o.player_uid}', 'Player UID')" title="Copy UID" class="ml-1 text-slate-400 hover:text-white">
                                <i class="fa-regular fa-copy text-[10px]"></i>
                            </button>
                        </td>
                        <td>
                            <div class="font-bold text-white flex items-center gap-1.5">
                                <i class="fa-solid fa-gem text-cyan-400 text-[10px]"></i> ${o.package_name}
                            </div>
                            <div class="text-[10px] text-slate-400">${o.product_name || "Free Fire BD"}</div>
                        </td>
                        <td class="font-mono font-bold text-emerald-400">৳${o.amount}</td>
                        <td>
                            <div class="font-semibold text-slate-200">${o.payment_method}</div>
                            ${o.trx_id ? `<div class="text-[10px] text-slate-400 font-mono flex items-center gap-1">Trx: ${o.trx_id} <button onclick="copyText('${o.trx_id}', 'TrxID')" class="hover:text-white"><i class="fa-regular fa-copy text-[9px]"></i></button></div>` : ''}
                        </td>
                        <td class="text-[11px] text-slate-400 whitespace-nowrap">${dateStr}</td>
                        <td>${statusBadge}</td>
                        <td class="text-right">
                            <div class="inline-flex items-center gap-1.5">
                                ${st !== 'completed' ? `
                                <button onclick="updateOrderStatus('${o._id}', 'completed')"
                                        class="px-2 py-1 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-[11px] transition shadow flex items-center gap-1"
                                        title="অর্ডার কমপ্লিট করুন">
                                    <i class="fa-solid fa-check"></i>
                                    <span class="hidden sm:inline">Complete</span>
                                </button>` : ''}

                                <select onchange="updateOrderStatus('${o._id}', this.value)" class="bg-dark-900 border border-slate-700 text-[11px] text-slate-300 rounded-lg px-2 py-1 focus:outline-none">
                                    <option value="" disabled selected>স্ট্যাটাস</option>
                                    <option value="completed">✅ Complete</option>
                                    <option value="processing">🔄 Processing</option>
                                    <option value="pending">⏳ Pending</option>
                                    <option value="cancelled">❌ Cancel</option>
                                </select>

                                <button onclick="deleteOrder('${o._id}')" class="p-1 px-2 rounded-lg bg-rose-500/20 text-rose-400 hover:bg-rose-500 hover:text-white transition text-xs" title="ডিলিট">
                                    <i class="fa-solid fa-trash"></i>
                                </button>
                            </div>
                        </td>
                    </tr>
                `;
            }).join('');
        }

        function filterOrders(status) {
            currentOrderFilter = status;
            ['all', 'pending', 'processing', 'completed', 'cancelled'].forEach(s => {
                const btn = document.getElementById(`filter-${s}`);
                if (btn) {
                    if (s === status) {
                        btn.className = "px-3 py-1.5 rounded-xl text-xs font-bold bg-blue-600 text-white shrink-0";
                    } else {
                        btn.className = "px-3 py-1.5 rounded-xl text-xs font-medium bg-dark-800 text-slate-300 hover:text-white border border-slate-700/50 shrink-0";
                    }
                }
            });
            renderOrdersTable();
        }

        async function updateOrderStatus(orderDocId, newStatus) {
            if (!newStatus) return;
            const res = await convex.mutation("orders:updateStatus", { id: orderDocId, status: newStatus });
            if (res && res.success) {
                const order = allOrders.find(o => o._id === orderDocId);
                if (order) order.status = newStatus;
                updateStats();
                renderOrdersTable();
                showToast(`অর্ডার স্ট্যাটাস আপডেট হয়েছে: ${newStatus.toUpperCase()}`);
            } else {
                showToast("স্ট্যাটাস আপডেট ব্যর্থ হয়েছে!", "error");
            }
        }

        async function deleteOrder(orderDocId) {
            if (!confirm("আপনি কি নিশ্চিত এই অর্ডারটি ডাটাবেস থেকে মুছে ফেলতে চান?")) return;
            const res = await convex.mutation("orders:deleteOrder", { id: orderDocId });
            if (res && res.success) {
                allOrders = allOrders.filter(o => o._id !== orderDocId);
                updateStats();
                renderOrdersTable();
                showToast("অর্ডার ডাটাবেস থেকে মুছে ফেলা হয়েছে।");
            } else {
                showToast("অর্ডার ডিলিট করা যায়নি!", "error");
            }
        }

        function exportOrdersToCSV() {
            if (allOrders.length === 0) {
                alert("এক্সপোর্ট করার মতো কোনো অর্ডার নেই!");
                return;
            }
            let csv = "Order ID,Player UID,Package,Amount,Method,TrxID,Status,Created At\\n";
            allOrders.forEach(o => {
                csv += `"${o.order_id}","${o.player_uid}","${o.package_name}",${o.amount},"${o.payment_method}","${o.trx_id || ''}","${o.status}","${o.created_at || ''}"\\n`;
            });
            const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
            const link = document.createElement("a");
            link.href = URL.createObjectURL(blob);
            link.download = `RRR_Topup_Orders_${Date.now()}.csv`;
            link.click();
            showToast("অর্ডার রিপোর্ট CSV ডাউনলোড হয়েছে!");
        }


        // ==============================================
        // DEPOSITS / ADD MONEY APPROVAL LOGIC
        // ==============================================
        function renderDepositsTable() {
            const tbody = document.getElementById("deposits-tbody");
            const q = (document.getElementById("deposit-search").value || "").toLowerCase().trim();

            let filtered = allDeposits;
            if (currentDepositFilter !== "all") {
                filtered = filtered.filter(d => (d.status || "").toLowerCase() === currentDepositFilter);
            }
            if (q) {
                filtered = filtered.filter(d =>
                    (d.trx_id || "").toLowerCase().includes(q) ||
                    (d.user_phone || "").toLowerCase().includes(q) ||
                    (d.payment_method || "").toLowerCase().includes(q)
                );
            }

            if (filtered.length === 0) {
                tbody.innerHTML = `<tr><td colspan="7" class="text-center py-8 text-slate-500 text-xs">কোনো ডিপোজিট রিকোয়েস্ট নেই।</td></tr>`;
                return;
            }

            tbody.innerHTML = filtered.map(d => {
                const st = (d.status || "completed").toLowerCase();
                let statusBadge = '';
                if (st === "completed") {
                    statusBadge = `<span class="px-2.5 py-0.5 rounded-full text-[10px] font-bold bg-emerald-500/20 text-emerald-400 border border-emerald-500/40">APPROVED</span>`;
                } else if (st === "pending") {
                    statusBadge = `<span class="px-2.5 py-0.5 rounded-full text-[10px] font-bold bg-purple-500/20 text-purple-300 border border-purple-500/40 animate-pulse">PENDING</span>`;
                } else {
                    statusBadge = `<span class="px-2.5 py-0.5 rounded-full text-[10px] font-bold bg-rose-500/20 text-rose-400 border border-rose-500/40">REJECTED</span>`;
                }

                const dateStr = d.created_at ? new Date(d.created_at).toLocaleString() : 'N/A';
                const isBkash = (d.payment_method || "").toLowerCase().includes("bkash");

                return `
                    <tr>
                        <td class="font-mono font-bold text-white text-xs">
                            ${d.trx_id}
                            <button onclick="copyText('${d.trx_id}', 'TrxID')" class="ml-1 text-slate-400 hover:text-white">
                                <i class="fa-regular fa-copy text-[10px]"></i>
                            </button>
                        </td>
                        <td class="font-mono text-cyan-300 font-bold">${d.user_phone}</td>
                        <td>
                            <span class="px-2 py-0.5 rounded-full text-[10px] font-bold ${isBkash ? 'bg-pink-500/20 text-pink-300 border border-pink-500/40' : 'bg-orange-500/20 text-orange-300 border border-orange-500/40'}">
                                ${d.payment_method}
                            </span>
                        </td>
                        <td class="font-mono font-bold text-emerald-400 text-sm">৳${d.amount}</td>
                        <td class="text-[11px] text-slate-400 whitespace-nowrap">${dateStr}</td>
                        <td>${statusBadge}</td>
                        <td class="text-right">
                            <div class="inline-flex items-center gap-1.5">
                                ${st !== 'completed' ? `
                                <button onclick="approveDepositAction('${d._id}', ${d.amount})"
                                        class="px-2.5 py-1 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs transition shadow flex items-center gap-1">
                                    <i class="fa-solid fa-check"></i>
                                    <span>Approve</span>
                                </button>` : ''}

                                ${st === 'pending' ? `
                                <button onclick="rejectDepositAction('${d._id}')"
                                        class="px-2 py-1 rounded-lg bg-dark-700 hover:bg-rose-600 text-slate-300 hover:text-white font-bold text-xs transition">
                                    Reject
                                </button>` : ''}

                                <button onclick="deleteDepositAction('${d._id}')" class="p-1 px-2 rounded-lg bg-rose-500/20 text-rose-400 hover:bg-rose-500 hover:text-white transition text-xs">
                                    <i class="fa-solid fa-trash"></i>
                                </button>
                            </div>
                        </td>
                    </tr>
                `;
            }).join('');
        }

        function filterDeposits(status) {
            currentDepositFilter = status;
            ['all', 'pending', 'completed'].forEach(s => {
                const btn = document.getElementById(`dep-filter-${s}`);
                if (btn) {
                    if (s === status) {
                        btn.className = "px-3 py-1.5 rounded-xl text-xs font-bold bg-purple-600 text-white";
                    } else {
                        btn.className = "px-3 py-1.5 rounded-xl text-xs font-medium bg-dark-800 text-slate-300 hover:text-white border border-slate-700/50";
                    }
                }
            });
            renderDepositsTable();
        }

        async function approveDepositAction(txId, amount) {
            if (!confirm(`আপনি কি নিশ্চিত এই ৳${amount} ডিপোজিট অনুমোদন করতে এবং গ্রাহকের ওয়ালেটে যোগ করতে চান?`)) return;
            const res = await convex.mutation("wallet:approveDeposit", { id: txId });
            if (res && res.success) {
                showToast(`ডিপোজিট অনুমোদিত হয়েছে! ইউজারের ওয়ালেটে ৳${amount} যোগ হয়েছে।`);
                fetchAllData();
            } else {
                showToast(res ? res.message : "অনুমোদন ব্যর্থ হয়েছে!", "error");
            }
        }

        async function rejectDepositAction(txId) {
            if (!confirm("আপনি কি নিশ্চিত এই ডিপোজিটটি বাতিল করতে চান?")) return;
            const res = await convex.mutation("wallet:updateStatus", { id: txId, status: "rejected" });
            if (res && res.success) {
                showToast("ডিপোজিট বাতিল করা হয়েছে।");
                fetchAllData();
            }
        }

        async function deleteDepositAction(txId) {
            if (!confirm("ডিপোজিট হিস্ট্রি থেকে মুছে ফেলবেন?")) return;
            const res = await convex.mutation("wallet:deleteTransaction", { id: txId });
            if (res && res.success) {
                showToast("মুছে ফেলা হয়েছে।");
                fetchAllData();
            }
        }

        function openManualDepositModal() {
            document.getElementById("modal-manual-deposit").classList.remove("hidden");
        }

        async function submitManualDeposit(e) {
            e.preventDefault();
            const phone = document.getElementById("man-dep-phone").value.trim();
            const amount = parseFloat(document.getElementById("man-dep-amount").value);
            const method = document.getElementById("man-dep-method").value;
            const trx = (document.getElementById("man-dep-trx").value || `MAN-${Date.now().toString().slice(-6)}`).trim();

            if (!phone || !amount || amount <= 0) {
                alert("সঠিক ফোন ও টাকার পরিমাণ লিখুন!");
                return;
            }

            const res = await convex.mutation("wallet:addMoney", {
                phone: phone,
                amount: amount,
                payment_method: method,
                sender_number: phone,
                trx_id: trx
            });

            if (res && res.success) {
                showToast(`৳${amount} সফলভাবে ${phone} ওয়ালেটে জমা হয়েছে!`);
                closeModal("modal-manual-deposit");
                document.getElementById("man-dep-phone").value = "";
                document.getElementById("man-dep-amount").value = "";
                fetchAllData();
            } else {
                showToast("ডিপোজিট ব্যর্থ হয়েছে!", "error");
            }
        }


        // ==============================================
        // DIAMOND PACKAGES MANAGEMENT
        // ==============================================
        function renderPackagesTable() {
            const tbody = document.getElementById("packages-tbody");
            if (allPackages.length === 0) {
                tbody.innerHTML = `<tr><td colspan="5" class="text-center py-8 text-slate-500 text-xs">কোনো প্যাকেজ পাওয়া যায়নি।</td></tr>`;
                return;
            }

            tbody.innerHTML = allPackages.map(pkg => {
                const inStock = pkg.in_stock !== 0;
                return `
                    <tr>
                        <td class="font-bold text-white flex items-center gap-2">
                            <i class="fa-solid fa-gem text-cyan-400"></i>
                            <span>${pkg.name}</span>
                        </td>
                        <td><span class="px-2 py-0.5 rounded-lg bg-blue-500/20 text-blue-300 font-mono text-xs font-bold">${pkg.tag || "Diamond"}</span></td>
                        <td class="font-mono font-bold text-emerald-400 text-sm">৳ ${pkg.price}</td>
                        <td>
                            <button onclick="togglePackageStock('${pkg._id}', ${inStock ? 0 : 1})"
                                    class="px-2.5 py-0.5 rounded-full text-[10px] font-bold cursor-pointer transition ${inStock ? 'bg-emerald-500/20 text-emerald-400 border border-emerald-500/40 hover:bg-emerald-500/30' : 'bg-rose-500/20 text-rose-400 border border-rose-500/40 hover:bg-rose-500/30'}">
                                ${inStock ? 'IN STOCK 🟢' : 'OUT OF STOCK 🔴'}
                            </button>
                        </td>
                        <td class="text-right">
                            <div class="inline-flex items-center gap-1.5">
                                <button onclick="editPackagePrice('${pkg._id}', ${pkg.price})" class="px-2.5 py-1 rounded-lg bg-dark-800 hover:bg-dark-700 border border-slate-700 text-blue-300 text-xs font-semibold">
                                    <i class="fa-solid fa-pen-to-square mr-1"></i> মূল্য পরিবর্তন
                                </button>
                                <button onclick="deletePackage('${pkg._id}')" class="p-1 px-2 rounded-lg bg-rose-500/20 text-rose-400 hover:bg-rose-500 hover:text-white transition text-xs">
                                    <i class="fa-solid fa-trash"></i>
                                </button>
                            </div>
                        </td>
                    </tr>
                `;
            }).join('');
        }

        async function togglePackageStock(pkgId, newStock) {
            const res = await convex.mutation("packages:updateStock", { id: pkgId, in_stock: newStock });
            if (res && res.success) {
                showToast(`স্টক স্ট্যাটাস আপডেট হয়েছে: ${newStock ? 'IN STOCK' : 'OUT OF STOCK'}`);
                fetchAllData();
            }
        }

        function openAddPackageModal() {
            document.getElementById("modal-package").classList.remove("hidden");
        }

        async function submitNewPackage(e) {
            e.preventDefault();
            const name = document.getElementById("pkg-name").value.trim();
            const tag = document.getElementById("pkg-tag").value.trim();
            const price = parseFloat(document.getElementById("pkg-price").value) || 0;

            const res = await convex.mutation("packages:add", {
                product_id: 21,
                name: name,
                price: price,
                tag: tag,
                in_stock: 1
            });

            if (res && res.success) {
                showToast("নতুন ডায়মন্ড প্যাকেজ সফলভাবে যুক্ত হয়েছে!");
                closeModal("modal-package");
                document.getElementById("pkg-name").value = "";
                document.getElementById("pkg-tag").value = "";
                document.getElementById("pkg-price").value = "";
                fetchAllData();
            } else {
                showToast("প্যাকেজ যোগ করতে সমস্যা হয়েছে!", "error");
            }
        }

        async function editPackagePrice(pkgId, currPrice) {
            const newPrice = prompt("নতুন মূল্য দিন (৳ BDT):", currPrice);
            if (newPrice !== null && !isNaN(parseFloat(newPrice))) {
                const res = await convex.mutation("packages:update", {
                    id: pkgId,
                    price: parseFloat(newPrice)
                });
                if (res && res.success) {
                    showToast("প্যাকেজের মূল্য আপডেট করা হয়েছে!");
                    fetchAllData();
                }
            }
        }

        async function deletePackage(pkgId) {
            if (!confirm("আপনি কি নিশ্চিত এই প্যাকেজটি মুছে ফেলতে চান?")) return;
            const res = await convex.mutation("packages:remove", { id: pkgId });
            if (res && res.success) {
                showToast("প্যাকেজ মুছে ফেলা হয়েছে।");
                fetchAllData();
            }
        }


        // ==============================================
        // USERS & WALLET LOGIC
        // ==============================================
        function renderUsersTable() {
            const tbody = document.getElementById("users-tbody");
            const q = (document.getElementById("user-search").value || "").toLowerCase().trim();

            let filtered = allUsers;
            if (q) {
                filtered = filtered.filter(u =>
                    (u.name || "").toLowerCase().includes(q) ||
                    (u.phone || "").toLowerCase().includes(q) ||
                    (u.email || "").toLowerCase().includes(q)
                );
            }

            if (filtered.length === 0) {
                tbody.innerHTML = `<tr><td colspan="6" class="text-center py-8 text-slate-500 text-xs">কোনো ইউজার পাওয়া যায়নি।</td></tr>`;
                return;
            }

            tbody.innerHTML = filtered.map(u => {
                const dateStr = u.created_at ? new Date(u.created_at).toLocaleDateString() : 'N/A';
                return `
                    <tr>
                        <td class="font-bold text-white flex items-center gap-2">
                            <div class="w-7 h-7 rounded-full bg-blue-500/20 text-blue-300 flex items-center justify-center text-xs">👤</div>
                            <span>${u.name}</span>
                        </td>
                        <td class="font-mono text-cyan-300 font-bold">${u.phone}</td>
                        <td class="text-slate-400 text-xs">${u.email || "N/A"}</td>
                        <td class="font-mono font-bold text-emerald-400 text-sm">৳ ${(u.balance || 0).toFixed(2)}</td>
                        <td class="text-slate-400 text-xs">${dateStr}</td>
                        <td class="text-right">
                            <button onclick="openWalletModal('${u._id}', '${u.name}', ${u.balance || 0})"
                                    class="px-3 py-1.5 rounded-xl bg-[#2563eb] hover:bg-[#1d4ed8] text-white font-bold text-xs transition shadow flex items-center gap-1.5 ml-auto">
                                <i class="fa-solid fa-coins"></i>
                                <span>ব্যালেন্স অ্যাডজাস্ট</span>
                            </button>
                        </td>
                    </tr>
                `;
            }).join('');
        }

        function openWalletModal(userId, name, currBalance) {
            selectedUserId = userId;
            document.getElementById("wallet-modal-user").textContent = name;
            document.getElementById("wallet-modal-curr").textContent = "৳ " + currBalance.toFixed(2);
            document.getElementById("wallet-amount-input").value = "";
            document.getElementById("modal-wallet").classList.remove("hidden");
        }

        async function submitWalletAdjustment() {
            const type = document.getElementById("wallet-action-type").value;
            const amt = parseFloat(document.getElementById("wallet-amount-input").value);
            if (!amt || amt <= 0) {
                alert("সঠিক পরিমাণ লিখুন!");
                return;
            }

            const res = await convex.mutation("users:updateBalance", {
                id: selectedUserId,
                amount: amt,
                type: type
            });

            if (res && res.success) {
                showToast(`ব্যালেন্স আপডেট সম্পন্ন! নতুন ব্যালেন্স: ৳${res.newBalance.toFixed(2)}`);
                closeModal("modal-wallet");
                fetchAllData();
            } else {
                showToast("ব্যালেন্স আপডেট ব্যর্থ হয়েছে!", "error");
            }
        }


        // ==============================================
        // SITE SETTINGS & ANNOUNCEMENTS
        // ==============================================
        function handleSaveNotice(e) {
            e.preventDefault();
            const text = document.getElementById("setting-notice-text").value.trim();
            localStorage.setItem("rrrtopup_site_notice", text);
            showToast("সাইট নোটিশ সফলভাবে আপডেট হয়েছে!");
        }

        function handleSavePaymentNumbers(e) {
            e.preventDefault();
            const bk = document.getElementById("setting-bkash-no").value.trim();
            const ng = document.getElementById("setting-nagad-no").value.trim();
            localStorage.setItem("rrrtopup_bkash_no", bk);
            localStorage.setItem("rrrtopup_nagad_no", ng);
            showToast("বিকাশ ও নগদ নম্বর আপডেট করা হয়েছে!");
        }

        async function pingCloudLatency() {
            const start = Date.now();
            const pingEl = document.getElementById("cloud-ping-val");
            pingEl.textContent = "Testing...";
            try {
                await fetch(`${CONVEX_CLOUD_URL}/api/query`, {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({ path: "orders:listRecent", args: {} })
                });
                const elapsed = Date.now() - start;
                pingEl.textContent = `${elapsed}ms 🟢`;
                showToast(`Convex Cloud Latency: ${elapsed}ms`);
            } catch(e) {
                pingEl.textContent = "Error 🔴";
            }
        }


        // ==============================================
        // UTILITIES & MODAL HELPERS
        // ==============================================
        function copyText(txt, label) {
            navigator.clipboard.writeText(txt);
            showToast(`Copied ${label}: ${txt}`);
        }

        function closeModal(id) {
            const el = document.getElementById(id);
            if (el) el.classList.add("hidden");
        }

        // Init on DOM Load
        document.addEventListener("DOMContentLoaded", () => {
            checkAdminAuth();
            
            // Load saved settings if any
            const savedNotice = localStorage.getItem("rrrtopup_site_notice");
            if (savedNotice) document.getElementById("setting-notice-text").value = savedNotice;

            const savedBkash = localStorage.getItem("rrrtopup_bkash_no");
            if (savedBkash) document.getElementById("setting-bkash-no").value = savedBkash;

            const savedNagad = localStorage.getItem("rrrtopup_nagad_no");
            if (savedNagad) document.getElementById("setting-nagad-no").value = savedNagad;
        });
    </script>
</body>
</html>
'''

with open('/storage/emulated/0/Codex/freefire-topup/admin.html', 'w', encoding='utf-8') as f:
    f.write(admin_html_content)

print(f"admin.html generated successfully! Total size: {len(admin_html_content)} bytes")
