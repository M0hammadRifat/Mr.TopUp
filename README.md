# Free Fire Topup Portal & Admin Dashboard

A high-performance, mobile-optimized Free Fire Topup and Wallet Management platform connected to a real-time **Convex Cloud** database backend.

---

## 🚀 Overview

- **Public Storefront (`index.html`):**
  - Ultra-fast, zero page-reload experience.
  - 3-slide hero promotional carousel with touch swiping and indicator dots.
  - 24+ Diamond top-up packages with instant search and category filters.
  - Deposit & Wallet balance integration with bKash and Nagad.
  - Zero admin references or links visible to normal users.

- **Ultimate Admin Suite (`admin.html`):**
  - Completely isolated admin room accessed strictly via `admin.html`.
  - Secure authentication with custom admin login credentials.
  - Real-time cloud sync with automatic notification chime (Web Audio API).

---

## 💎 Admin Panel Features & Control Rooms

### 1. Executive Analytics & Metric Cards
- **Total Revenue & Today's Sales:** Live financial totals calculated from completed orders.
- **Diamond Meter:** Total diamonds successfully delivered to players.
- **Order Queue Status:** Real-time counters for Pending Orders and Pending Wallet Deposits.
- **Users & Wallet Pool:** Total registered players and aggregate wallet balance held in Convex.
- **Estimated Net Profit:** Margin tracking calculated across sales volume.

### 2. Visual Charts & Payment Breakdown
- **7-Day Dynamic Sales Bar Chart:** Native SVG bar chart visualizing the last 7 days of order sales volume.
- **Payment Method Distribution:** Real-time percentage breakdown between bKash, Nagad, and Wallet payments.

### 3. Built-in Free Fire UID Instant Checker
- Integrated player verification tool directly in the admin header.
- Enter any Free Fire Player UID to instantly fetch and verify player nickname and server region before completing an order.

### 4. Audio Notification Chime (Zero External Dependencies)
- Uses native browser **Web Audio API** (`AudioContext`) to synthesize a melodic 2-tone chime whenever new pending orders or deposits arrive during auto-sync.
- Sound toggle button included in the navigation header.

### 5. Orders Management Room
- Filter pills: All, Pending, Processing, Completed, Cancelled.
- Instant search by Order ID, Player UID, or Customer Name.
- 1-click **Complete** and **Cancel** buttons with direct Convex Cloud mutation.
- 1-click copy buttons for Player UID and Transaction ID.
- **Export to CSV:** Instant download of order history reports.

### 6. Deposits & Payment Approvals Room
- **1-Click Approve:** Approving a deposit instantly updates the status and **automatically credits the user's Convex wallet balance**.
- **1-Click Reject / Delete:** Instant rejection with audit tracking.
- **Manual Add Money:** Credit or bonus funds directly to any user account with optional custom note.

### 7. Diamond Packages Room
- Manage all 24+ packages (Regular Diamonds, Weekly/Monthly Memberships, Level Up Pass, Evo Gun Tokens).
- **Live Stock Toggle:** 1-click In-Stock / Out-of-Stock toggle with instant storefront sync.
- **Inline Price Editor:** Quick update of package prices without full page reload.
- **Add / Delete Package:** Add custom diamond packages on demand.

### 7.1 ⚡ 100% Free bKash & Nagad Auto Payment (SMS Webhook Automation)
- **Zero Merchant Fee & Works on Personal SIMs:** No trade license, merchant account, or third-party paid subscriptions required.
- **Convex HTTP Action Webhook:**
  - Endpoint: `https://quixotic-cuttlefish-352.convex.site/api/sms-webhook`
  - Accepts incoming SMS notifications from Android automation apps (**MacroDroid** / **SMS Forwarder** / **Tasker**).
- **Intelligent Parser & Bidirectional Auto-Approval:**
  - Extracts gateway, TrxID, amount, and sender phone number using regex patterns supporting bKash (Send Money, Cash In, Payment) and Nagad (Money Received, Cash In).
  - **Scenario A (SMS first):** User submits deposit -> instantly matched and approved in 0.5s!
  - **Scenario B (Deposit first):** User submits deposit before SMS arrives -> automatically marked approved and credited the second the SMS hits the webhook.
  - **Fraud & Double-Spend Shield:** Blocks re-use of already claimed TrxIDs.
- **In-Admin Test Simulator:** Allows admin to simulate live webhook calls and inspect parsed JSON responses without making real transactions.
- **Live SMS Logs Table:** Real-time log of all incoming SMS notifications with filter pills (All, Claimed, Unclaimed).

### 7.2 🔥 Free Fire Auto Like & Live Player ID Inspector (Modeled after Free-Fire-free-APIS)
- **Multi-Region Live Lookup:** Supports querying Garena Free Fire player data across regions (`BD`, `IND`, `SG`, `PK`, `ID`, `BR`, `US`, `RU`, `ME`).
- **Comprehensive Gamer Profile Card:**
  - In-game Nickname with 1-click copy.
  - Player UID with 1-click copy.
  - Live Likes Counter (`liked` / ❤️) with 24-hour delivery capacity tracking (max 200/day).
  - Level with animated EXP Progress bar.
  - Battle Royale (BR) & Clash Squad (CS) Rank badges (Master, Heroic, Grandmaster, Diamond).
  - Guild/Clan details (Clan Name, Level, Member Capacity).
  - Bio / Signature quote and Fair Play Honor score.
- **Embedded & Modal Mode:**
  - Embedded tab switcher directly inside **FF Auto Like** (`pid === 41`) allowing instant toggling between Like Packages and Profile Inspection.
  - Dedicated **FF ID & লাইক চেকার** category card and modal inspector with Keyword / Name Search (`/api/v1/search-players`) and UID lookup (`/api/v1/player-profile`).
- **1-Click Ordering Router:** Automatically routes verified UIDs into the Auto Like and Diamond Topup workflows without re-typing.

### 8. Users CRM & Wallet Controls
- Customer database with **VIP Tier Badges** (Platinum, Gold, Silver, Standard) based on total spend.
- **Direct Wallet Adjustments:**
  - `+ Add`: Credit funds (promotions, compensation, deposit).
  - `- Deduct`: Debit funds (corrections, chargebacks).
  - `= Set`: Manually set exact wallet balance.
- View user order history in 1-click.

### 9. Coupons & Discount Vouchers Room
- Create promo codes with Flat (৳) or Percentage (%) discounts.
- Set minimum spend thresholds and maximum discount caps.
- Toggle coupon active status and track usage statistics.

### 10. Hero Banners & Slider Manager
- Configure promotional banners displayed on the home page slider.
- Update banner image URLs, titles, and target action links with live image preview.

### 11. Security Audit Logs Room
- Real-time chronological timeline tracking every admin action (approvals, balance edits, status changes).
- Search logs and clear logs capability.

### 12. System Settings & Maintenance Room
- **Marquee Notice Editor:** Update the live scrolling announcement bar across the public site.
- **Emergency Maintenance Mode:** 1-click toggle to put the public store into maintenance mode.
- **bKash & Nagad Numbers:** Update merchant/personal payment receiving numbers.
- **Admin Password Change:** Update admin security credentials.
- **Cloud Latency Ping:** Measure real-time roundtrip ping to Convex Cloud.

---

## 🛠️ Convex Backend Architecture

- **Deployment URL:** `https://quixotic-cuttlefish-352.convex.cloud`
- **Key Backend Functions:**
  - `wallet:approveDeposit`: Atomically marks transaction approved and credits user wallet balance.
  - `wallet:adjustBalance`: Admin balance override (`add`, `deduct`, `set`).
  - `wallet:deleteTransaction`: Removes deposit records.
  - `orders:updateStatus`: Updates order status to `completed`, `processing`, or `cancelled`.
  - `packages:updateStock`: Toggles package availability in the public store.
  - `packages:updatePrice`: Updates package diamond pricing.
  - `packages:create` / `packages:delete`: Adds or deletes topup packages.

---

## 💻 Local Development

```bash
# Start local server on port 8000
python3 -m http.server 8000 --bind 127.0.0.1

# Access public storefront:
http://127.0.0.1:8000/index.html

# Access admin panel:
http://127.0.0.1:8000/admin.html
```
