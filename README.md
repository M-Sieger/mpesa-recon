# 🎯 M-RECON: MASTER PLAN & SINGLE SOURCE OF TRUTH

> **Letzte Aktualisierung:** 13. Januar 2025  
> **Status:** Pre-MVP Validation Phase  
> **Nächstes Gate:** 27. Januar 2025 (GO/NO-GO Decision)

[![Status](https://img.shields.io/badge/Status-Validation_Phase-yellow)]()
[![Focus](https://img.shields.io/badge/Focus-SACCO_Partnerships-blue)]()
[![GTM](https://img.shields.io/badge/GTM-B2B2C-green)]()

---

## 📋 **EXECUTIVE SUMMARY**

**M-Recon** ist eine Financial Inclusion Platform für informelle kenianische SMEs, die M-Pesa-PDFs in kreditwürdige Financial Records umwandelt. 

**Primary GTM:** SACCO-Partnerships  
**Core Thesis:** 29% der MSME-Kredite (400K/Jahr) werden wegen fehlender Dokumentation abgelehnt - M-Recon löst das, erhöht Approval-Rates um 15-25%.

**Current Focus:** Validate Product-Market-Fit via SACCO-Pilots in Q1 2025.

---

## 🚀 **VISION, MISSION & POSITIONING**

### Vision (3-5 Jahre)
> "Jeder informelle SME-Besitzer in Kenya kann einen Business-Loan bekommen."

### Mission (12-18 Monate)
> "50.000 kenianischen SMEs ermöglichen, ihre M-Pesa-Historie in Kreditzugang zu verwandeln."

### Positioning Statement
```
Für informelle SME-Besitzer in Kenya (Jua Kali, Mama Mboga, Dukas),
die Kredite brauchen aber abgelehnt werden wegen fehlender Records,
ist M-Recon eine Mobile-First Bookkeeping App,
die M-Pesa-PDFs in SACCO/Bank-ready Financial Reports verwandelt.

Anders als Pay Hero (API-first, formal businesses),
fokussiert M-Recon auf Loan-Access für Informal Sector via PDF-Parsing + SACCO-Partnerships.
```

---

## � **CURRENT STATUS (Stand: 13. Jan 2025)**

### ✅ Validated
- [x] **Loan-Access Pain Point:** 29% rejections wegen fehlender Docs (400K MSMEs/Jahr)
- [x] **PDF-First Strategy:** Daraja API würde 70%+ informal SMEs ausschließen
- [x] **SACCO Partnerships:** 70,6% digital adoption, proven precedents (Kwara, Branch)
- [x] **Unit Economics:** 41:1 LTV:CAC ratio via partnerships

### ⚠️ To Be Validated (Next 14 Tage)
- [ ] **PDF Parsing Accuracy:** PoC mit 20 real PDFs (Target: 90%+)
- [ ] **SACCO Interest:** 2-3 confirmed conversations
- [ ] **WTP:** 60%+ bereit KES 500/mo zu zahlen für loan-access
- [ ] **Waitlist Demand:** 30+ signups

### ❌ Pivoted/Deprioritized
- [x] ~~WEF als Primary Partner~~ → Long-term play (bank account requirement)
- [x] ~~eTIMS im MVP~~ → Too complex, erst Phase 2 (Monat 4-6)
- [x] ~~Consumer-First GTM~~ → **SACCO-Partnership-First** (B2B2C)

---

## 🏗️ **STRATEGIC PILLARS**

### 1. Product Strategy: PDF-First Offline Bookkeeping
```
Core Features (MVP - 4 Layers):
  
  LAYER 1: Extraction (✅ DONE - 100% accuracy!)
    → PDFPlumber-based parser
    → Password-protected PDF support (ID number)
    → Extract: date, amount, description, transaction ID
  
  LAYER 2: Categorization (⏸️ IN PROGRESS - Critical!)
    → Rule-based classifier (Business/Personal)
    → 6-8 core categories
    → Income vs Expense detection
  
  LAYER 3: Financial Summary (⏸️ IN PROGRESS - Critical!)
    → 6-month aggregations (Total Income/Expenses)
    → Monthly averages
    → Cashflow trends (growing/stable/declining)
    → Loan capacity estimate
  
  LAYER 4: Professional Reports (⏸️ IN PROGRESS - Critical!)
    → PDF report generation (ReportLab)
    → Bank statement quality
    → "Submit to SACCO" ready
    → CSV export (manual eTIMS entry)
  
  LAYER 5: Offline Mobile App (⏸️ Phase 1 Feb-Mar)
    → React Native + SQLite
    → Local processing
    → Background sync

Deferred (Phase 2, Month 4-6):
  ⏸️ eTIMS API Integration
  ⏸️ ML-based Categorization
  ⏸️ Bank Statement Support
  ⏸️ USSD Version (*XXX#)

CRITICAL INSIGHT (Jan 13):
  Parser alone (Layer 1) = no value to SACCO
  Must complete Layers 2-4 for demo-ready MVP
  Timeline: 5 days (Jan 13-17) before SACCO pitches
```

### 2. GTM Strategy: SACCO-Partnership-Driven
```
Priority 1: SACCO Partnerships (70% of CAC/Users)
  → Target: 5 pilot SACCOs (10K members each)
  → Model: Free for first 100 members, then KES 500/mo
  → Pitch: "Reduce member loan rejections by 25%"

Priority 2: Consumer Waitlist (20% - validation)
  → Target: 100+ signups in 30 days
  → Channel: Facebook groups, Grace's network

Priority 3: WEF Partnership (10% - long-term)
  → Positioning: "Help members get bank accounts"
  → Pilot: 50-100 groups (500-1,000 women)
```

### 3. Business Model: B2B2C Freemium
```
Pricing:
  💚 Free Tier: 50 transactions/month, basic reports
  💎 Premium: KES 500/month
      → Unlimited transactions
      → Auto-categorization
      → Priority support
      → "Loan-ready" badge

Revenue Streams:
  1. User Subscriptions (70%): KES 500 × 25,000 users = KES 12.5M/year
  2. SACCO Partnerships (20%): KES 10K-25K/SACCO/month × 10 = KES 1.2M-3M/year
  3. Referral Fees (10%): KES 100 per approved loan × 5,000 = KES 500K/year
```

---

## 🗓️ **ROADMAP: 6-MONTH PLAN**

### **PHASE 0: VALIDATION (Jan 13 - Jan 27, 2025)** ← WIR SIND HIER
```
Week 1 (Jan 13-17): MVP VALUE LAYER BUILD
  Day 1 (Jan 13):
    [✅] PDF Parser: Extract transactions (100% accuracy achieved!)
    [ ] Categorization Logic: Build rule-based classifier
         → Business vs Personal income/expenses
         → 6-8 core categories (payments, transfers, bills, etc.)
  
  Day 2 (Jan 14):
    [ ] Test Categorization: Validate on 124 transactions
    [ ] Summary Generator: Build financial aggregation logic
         → Total income/expenses (6 months)
         → Monthly averages
         → Cashflow trends
  
  Day 3 (Jan 15):
    [ ] PDF Report Generator: Professional output format
         → 1-page summary (bank statement style)
         → Income/Expense breakdown
         → Loan capacity estimate
  
  Day 4 (Jan 16):
    [ ] End-to-End Testing: Full pipeline
         → Upload PDF → Parse → Categorize → Report
    [ ] Polish: Fix edge cases, improve formatting
  
  Day 5 (Jan 17):
    [ ] Demo Prep: Test with 2-3 different PDFs
    [✅] DEMO-READY: Can show PDF → Professional Report

Week 2 (Jan 20-27): MARKET VALIDATION
  [ ] SACCO Outreach: 5 CEOs via LinkedIn (with working demo!)
  [ ] SACCO Demos: Show live PDF → Report transformation
  [ ] Waitlist Launch: m-recon.com live (optional)
  [ ] Grace Interviews: 10 SMEs (WTP validation)
  [ ] Technical Validation: Test with 10+ real PDFs
  
DECISION GATE (Jan 27):
  ✅ GO: If 2+ SACCO interest + demo works + 60%+ WTP → START MVP
  ⚠️ PIVOT: If weak SACCO interest → Adjust pitch/features
  ❌ STOP: If demo breaks or no demand → Reconsider

CRITICAL PATH CHANGE:
  OLD: Parser PoC → SACCO Outreach → Decision
  NEW: Parser PoC → Value Layer (Categories/Report) → SACCO Demos → Decision
  
WHY: Parser alone = no value. Must show professional report for SACCO buy-in.
```

### **PHASE 1: MVP BUILD (Feb 1 - Mar 31, 2025)**
```
Timeline: 8 weeks
Team: 1 founder (you) + freelancers (frontend, mobile)
Budget: ~KES 300K (USD $2,300)

PREREQUISITE FROM PHASE 0:
  ✅ Core Value Layer Built:
     → Transaction Categorization (Business/Personal)
     → Financial Summary Generator
     → Professional PDF Report Output
  ✅ Validated with 2+ SACCOs (they want it!)

Deliverables:
  ✅ Backend API: FastAPI + PostgreSQL/Supabase
      → PDF upload endpoint
      → Parser integration (already built!)
      → Categorization service (already built!)
      → Report generation (already built!)
      → User authentication
  ✅ Web App: React (waitlist → onboarding → upload → report)
      → Upload PDF interface
      → View transactions (categorized)
      → Download professional report
  ✅ Android MVP: React Native (offline-first)
      → Offline PDF upload
      → Local categorization
      → Background sync to server
  ✅ SACCO Integration: API for bulk member reports

Tech Stack:
  - Backend: FastAPI (Python) + Supabase (auth, storage)
  - Parsing: PDFPlumber + custom logic (DONE in Phase 0!)
  - Categorization: Rule-based classifier (DONE in Phase 0!)
  - Reports: ReportLab PDF generation (DONE in Phase 0!)
  - Frontend: React (Vercel deployment)
  - Mobile: React Native (Android-first)
  - Offline: SQLite + background sync
  
FOCUS: Wrap working core logic in production API + UI
```

### **PHASE 2: PILOT LAUNCH (Apr 1 - Jun 30, 2025)**
```
Target: 2-3 SACCO Pilots
  - Partner A: 10K members, target 500 users (5%)
  - Partner B: 8K members, target 400 users (5%)
  - Partner C: 15K members, target 600 users (4%)
  
Total Target: 1,500 users (break-even!)

Success Metrics:
  ✅ 50%+ adoption within pilot groups
  ✅ 90%+ parsing accuracy (user-reported)
  ✅ 15-20% loan approval uplift (measured vs control)
  ✅ <10% monthly churn
  ✅ 4+ NPS score

Funding Target: Seed Round (USD 250K-500K)
  - FSD Kenya Grant: USD 50-100K
  - Acumen/Novastar: USD 250-400K
```

### **PHASE 3: SCALE (Jul 1 - Dec 31, 2025)**
```
Target: 10 SACCOs, 10,000 users
Revenue: KES 5M ARR (USD ~$40K)
Team: 5 people (1 PM, 2 devs, 1 sales, 1 support)

New Features:
  ✅ eTIMS API Integration (differentiator!)
  ✅ ML-based Categorization
  ✅ USSD Version (*XXX#)
  ✅ Bank Statement Support (KCB, Equity)

WEF Partnership:
  ✅ Bank account facilitation (Postbank/Equity partnership)
  ✅ Pilot: 50-100 groups (500-1,000 women)
```

---

## 📂 **PROJECT STRUCTURE**

```
mpesa-recon/
├── android/                    # Native Android App (React Native) - PHASE 1
│   └── (to be created in MVP build phase)
├── client/                     # React Web App (Waitlist + Admin)
│   ├── src/
│   │   ├── components/        # UI Components (Upload, Preview, Reports)
│   │   ├── utils/             # PDF/CSV Parser (client-side PoC)
│   │   └── App.tsx
│   ├── package.json
│   └── vite.config.ts
├── server/                     # FastAPI Backend
│   ├── app/
│   │   ├── api/               # API Endpoints (upload, parse, reports)
│   │   ├── models/            # SQLAlchemy Models (User, Transaction, Upload)
│   │   ├── services/          # Business Logic (PDF parsing, categorization)
│   │   └── main.py
│   ├── requirements.txt
│   └── venv/                  # Python Virtual Environment
├── docs/                       # Documentation
│   ├── MVP-PLAN.md            # Detailed 90-day plan (NEEDS UPDATE)
│   ├── PRODUCT-VISION.md      # Product vision (NEEDS UPDATE)
│   ├── ROADMAP.md             # 6-month roadmap (NEEDS UPDATE)
│   ├── TECH-STACK.md          # Tech stack details (NEEDS UPDATE)
│   ├── RISK-ASSESSMENT.md     # Risk analysis
│   └── SACCO-STRATEGY.md      # SACCO partnership playbook (TO CREATE)
└── README.md                   # This file (Master Plan)
```

---

## 🚀 **TECH STACK**

### MVP (Phase 1: Feb-Mar 2025)
- **Backend:** FastAPI (Python 3.11+) + Supabase (PostgreSQL + Auth + Storage)
- **PDF Parsing:** PDFPlumber + custom regex logic
- **Frontend:** React + TypeScript + Vite (waitlist + admin dashboard)
- **Mobile:** React Native (Android-first, offline-first with SQLite)
- **Deployment:** Vercel (frontend), Railway/Fly.io (backend)

### Post-MVP (Phase 2-3: Apr-Dec 2025)
- **eTIMS Integration:** KRA VSCU API
- **ML Categorization:** scikit-learn (simple classifier)
- **USSD:** Africa's Talking API
- **Bank Statements:** Custom parsers for KCB, Equity formats

**Why PDF-First?**
- Daraja API requires registered business (excludes 70%+ informal SMEs)
- M-Pesa PDFs are universally accessible (everyone has them)
- Offline-first critical for Kenya's connectivity challenges

→ See [`docs/TECH-STACK.md`](docs/TECH-STACK.md) for details

---

## 🛠️ **SETUP & INSTALLATION**

### Prerequisites
- **Backend:** Python 3.11+, PostgreSQL 15+ (or Supabase account)
- **Mobile:** React Native CLI, Android Studio
- **Web Prototype:** Node.js 18+, pnpm

### 1. Backend Setup (FastAPI)

```bash
# Navigate to server directory
cd server

# Activate virtual environment
source venv/bin/activate  # Linux/Mac
# .\venv\Scripts\Activate.ps1  # Windows

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
# Create .env file with:
# DATABASE_URL=postgresql://user:password@localhost/mpesa_recon
# SUPABASE_URL=your-supabase-url
# SUPABASE_KEY=your-supabase-key
# SECRET_KEY=your-secret-key

# Run migrations (after creation)
alembic upgrade head

# Start server
uvicorn app.main:app --reload
```

**Backend runs on:** `http://localhost:8000`  
**API Docs:** `http://localhost:8000/docs`

### 2. React Web App Setup

```bash
# Navigate to client directory
cd client

# Install dependencies
pnpm install

# Start dev server
pnpm dev
```

**Frontend runs on:** `http://localhost:5173`

### 3. Android App Setup (Phase 1 - To Be Created)

```bash
# To be documented after MVP build kickoff
# Planned: React Native with Expo (faster iteration)
```

---

## 🎯 **IMMEDIATE ACTIONS (THIS WEEK: Jan 13-19)**

### Monday (TODAY) ✅
- [x] Update documentation with new strategic direction
- [ ] LinkedIn: Message 5 SACCO CEOs (Kimisitu, Finmat, Tower, Police, Kenya Re)
- [ ] Download 3 M-Pesa PDFs from Scribd for parsing PoC

### Tuesday-Wednesday
- [ ] PDF Parsing PoC: Test PDFPlumber on 3 PDFs (Target: 85%+ accuracy)
- [ ] Waitlist Page: Update with loan-access focus → Deploy via Vercel
- [ ] Grace Coordination: Schedule 10 SME interviews for WTP validation

### Thursday-Friday
- [ ] Grace Interviews: Execute 10 SME interviews (Questions: Loan rejections? WTP for loan-access?)
- [ ] WEF Email: Send partnership inquiry (low priority)
- [ ] SACCO Follow-ups: Respond to any LinkedIn replies

**DECISION GATE: Jan 27, 2025**
- Evaluate: SACCO interest + Parsing accuracy + Signups + WTP
- Decide: GO / PIVOT / STOP

---

## 📈 **SUCCESS METRICS (OKRs)**

### Q1 2025 (Validation Phase) ← CURRENT
```
Objective: Validate Product-Market Fit

KR1: 2+ SACCO partnerships signed (LOIs)
KR2: 100+ waitlist signups
KR3: PDF parsing PoC: 90%+ accuracy
KR4: 10 customer interviews: 60%+ WTP at KES 500/mo
```

### Q2 2025 (MVP + Pilot)
```
Objective: Launch MVP & Prove Value

KR1: 1,500 active users (3 SACCO pilots)
KR2: 15-20% loan approval uplift (measured)
KR3: 90%+ parsing accuracy (production)
KR4: <10% monthly churn
KR5: 4+ NPS score
```

### Q3-Q4 2025 (Scale)
```
Objective: Scale to 10K Users & Profitability

KR1: 10,000 active users (10 SACCOs)
KR2: KES 5M ARR (break-even)
KR3: Seed funding: USD 250-500K closed
KR4: eTIMS integration live (moat!)
KR5: <5% monthly churn
```

---

## 🎯 **CRITICAL ASSUMPTIONS & RISKS**

### Top 5 Assumptions (Must Be True)
```yaml
1. PDF Parsing Accuracy:
   Assumption: >90% achievable with PDFPlumber
   If Wrong: Need ML model ($10K cost, 2-month delay)
   
2. SACCO Interest:
   Assumption: 3+ SACCOs willing to pilot
   If Wrong: Pivot to consumer-first (higher CAC)
   
3. Loan Approval Uplift:
   Assumption: 15-20% improvement measurable
   If Wrong: Reposition as "time-saving" (weaker value prop)
   
4. Unit Economics:
   Assumption: CAC KES 200-500 via SACCOs
   Real Risk: Could be 2-3x higher (KES 500-1,500)
   
5. Adoption Rate:
   Assumption: 50% of SACCO pilot members adopt
   Real Risk: Could be 20-30%
```

### Top 5 Risks (With Mitigation)
```yaml
1. ⚠️ PDF Parsing Fails (<80% accuracy)
   Mitigation: Hybrid approach (auto-parse + manual review)
   Fallback: API-first for Paybill/Till users only
   
2. ⚠️ SACCO Partnerships Don't Materialize
   Mitigation: Over-recruit (pitch 10, need 3)
   Fallback: Consumer-first GTM + Facebook ads
   
3. ⚠️ WEF Bank Requirement Blocks Adoption
   Mitigation: Partner with Postbank for easy account opening
   Fallback: Focus on SACCO-only strategy
   
4. ⚠️ Pay Hero Pivots to Loan-Access Positioning
   Mitigation: Move fast on SACCO partnerships (lock-in)
   Differentiation: Offline-first + women-focus
   
5. ⚠️ Technical Complexity (Offline Sync) Delays MVP
   Mitigation: Launch web-only first, mobile in Phase 2
   Fallback: WiFi-only version (no offline sync)
```

---

## 👥 **KEY CONTACTS & RESOURCES**

### SACCO Targets (LinkedIn Outreach)
```
1. Kimisitu SACCO - Winner of Enterprise IT Adoption 2025
2. Finmat SACCO - AI/data analytics for credit scoring
3. Tower SACCO - Member empowerment focus
4. Police SACCO (KPS) - M-Tawi virtual branch success
5. Kenya Re SACCO - Bank statement requirements for loans
```

### WEF Contact
```
Rachel Musyoki (CEO, appointed Dec 2024)
Email: info@wef.co.ke
Phone: +254-714-606-845
Pitch: "Help WEF members meet bank account requirements"
```

### Grace (Local Partner)
```
Role: Customer interviews, market access, admin support
Tasks:
  - Source 10 SME interviewees
  - Collect 20 redacted M-Pesa PDFs
  - Nairobi-based support (if needed)
```

### Investors (Target for Q2 2025 Seed Round)
```
Tier 1:
  - FSD Kenya (Grant: USD 50-100K)
  - Acumen Fund (Seed: USD 250K-500K)
  - Novastar Ventures (Seed: USD 250K-1M)
```

---

## 🧭 **DECISION FRAMEWORK**

### GO/NO-GO Criteria (Jan 27, 2025)
```yaml
STRONG GO (Start MVP):
  ✅ 2+ SACCO conversations with strong interest
  ✅ PDF parsing PoC: 85-90%+ accuracy
  ✅ 30+ waitlist signups
  ✅ 60%+ WTP at KES 500/mo
  → ACTION: Hire devs, start backend build

YELLOW (Adjust & Retry):
  ⚠️ 1 SACCO conversation (weak interest)
  ⚠️ 70-80% parsing accuracy
  ⚠️ 10-20 signups
  ⚠️ 40-50% WTP
  → ACTION: Refine pitch, retry outreach

RED STOP (Pivot or Abandon):
  ❌ 0 SACCO interest after 10+ contacts
  ❌ <70% parsing accuracy
  ❌ <10 signups
  ❌ <30% WTP
  → ACTION: Pivot or stop
```

---

## 📚 **KEY RESEARCH FINDINGS**

### Market Validation
- **7.4M SMEs** in Kenya (80.8% informal)
- **29% loan rejections** due to insufficient docs (~400K applications/year)
- **Average loan size:** KES 50-150K for MSMEs
- **Total addressable credit:** KES 20B/year locked due to documentation

### SACCO Insights
- **357 deposit-taking SACCOs** (SASRA-regulated)
- **3.3M members**, KES 720B deposits
- **70.6% digital adoption** (mobile channels)
- **Kwara precedent:** Doubled SACCO memberships in 1 year

### Competitor Analysis
- **Pay Hero:** API-first, formal businesses, NO loan-access focus
- **White Space:** Offline + PDF + Loan-Access + SACCO partnerships = NOBODY
- **Threat Level:** Medium (could pivot, but different product DNA)

---

## 📝 **CHANGELOG**

```
2025-01-13: Strategic Pivot - Master Plan Created
  - Shifted focus from bookkeeping pain to loan-access value prop
  - Prioritized SACCO partnerships over consumer-first GTM
  - Deferred eTIMS integration to Phase 2
  - Set Decision Gate (Jan 27)
  - Created actionable 2-week validation sprint

Next Update: 2025-01-27 (after Decision Gate)
```

---

## 💬 **NOTES & REFLECTIONS**

```
[2025-01-13]
Major strategic realignment based on market research:
- Pain point: Loan rejections (29%) >> time-saving from bookkeeping
- GTM: SACCO partnerships (proven model: Kwara) >> direct consumer acquisition
- Product: PDF-first (inclusive) >> API-first (excludes informal sector)
- Timeline: 2-week validation sprint before committing to MVP build

Focus Areas:
1. SACCO CEO outreach (LinkedIn, 5 targets)
2. PDF parsing technical validation (20 real PDFs)
3. Customer WTP validation (Grace interviews)
4. Waitlist demand signal (30+ signups target)

Decision Gate: Jan 27 - GO/PIVOT/STOP based on validation results
```

---

**🎯 END OF MASTER PLAN**

---

## 🚀 **HOW TO USE THIS DOCUMENT**

1. **GitHub:** This README.md is the Single Source of Truth - always up to date
2. **Daily:** Read "IMMEDIATE ACTIONS" section every morning
3. **Weekly:** Update "Current Status" + "Notes & Reflections"
4. **Gates:** Re-read "Decision Framework" at milestones (Jan 27, Mar 31, Jun 30)
5. **Confusion:** Ctrl+F search for keywords (SACCO, PDF, WEF, etc.)

**This is your North Star. Everything else is noise.** 🧭

---

## 📖 **RELATED DOCUMENTATION**

- [`docs/PRODUCT-VISION.md`](docs/PRODUCT-VISION.md) - Detailed product vision (to be updated)
- [`docs/MVP-PLAN.md`](docs/MVP-PLAN.md) - 90-day MVP plan (to be updated)
- [`docs/ROADMAP.md`](docs/ROADMAP.md) - 6-month roadmap (to be updated)
- [`docs/TECH-STACK.md`](docs/TECH-STACK.md) - Technical architecture (to be updated)
- [`docs/RISK-ASSESSMENT.md`](docs/RISK-ASSESSMENT.md) - Risk analysis
- [`docs/SACCO-STRATEGY.md`](docs/SACCO-STRATEGY.md) - SACCO partnership playbook (to be created)

---

## 📞 **CONTACT**

**Project Lead:** M-Sieger  
**Repository:** [github.com/M-Sieger/mpesa-recon](https://github.com/M-Sieger/mpesa-recon)  
**Status Updates:** Weekly (check CHANGELOG section)

---

**Built with ❤️ for Kenyan SMEs seeking financial inclusion**

```powershell
# Android Studio öffnen
# File → Open → android/ Ordner auswählen
# Gradle Sync abwarten
# Run 'app' Configuration
```

---

## 📋 Aktueller Status (2025-10-22)

### ✅ Erledigt
- [x] Projekt-Struktur erstellt
- [x] React-Prototype mit PDF/CSV-Upload (UI-only)
- [x] Python Virtual Environment (venv)
- [x] Dokumentation (MVP-Plan, Product Vision, Roadmap, Risk Assessment)
- [x] Tech-Stack definiert

### 🔄 In Arbeit
- [ ] **Backend:** FastAPI Server + PostgreSQL Setup
- [ ] **Backend:** PDF-Parsing mit Kreuzberg/pdfplumber
- [ ] **Android:** Projekt-Setup (Kotlin + Compose)

### 📅 Nächste Schritte (Sprint 1 - Woche 1-2)
1. **Backend implementieren** (FastAPI + DB + PDF-Parser)
2. **Android-Projekt aufsetzen** (Multi-Module-Architektur)
3. **API-Integration testen** (Android ↔ Backend)
4. **20 Beta-Tester rekrutieren**

---

## 📖 Dokumentation

| Dokument | Beschreibung |
|----------|--------------|
| [`docs/MVP-PLAN.md`](docs/MVP-PLAN.md) | 90-Tage-Plan (3 Sprints: Validierung, Akquise, Monetarisierung) |
| [`docs/PRODUCT-VISION.md`](docs/PRODUCT-VISION.md) | Product Vision, User Stories, Tech-Stack-Entscheidungen |
| [`docs/ROADMAP.md`](docs/ROADMAP.md) | 12-24-Monate Roadmap (PMF → Scale → Expansion) |
| [`docs/RISK-ASSESSMENT.md`](docs/RISK-ASSESSMENT.md) | Risiken & Mitigationsstrategien |
| [`docs/TECH-STACK.md`](docs/TECH-STACK.md) | Detaillierte Tech-Specs, Libraries, Architecture |
| [`Due Diligence_ M-Pesa App für KMU.md`](Due%20Diligence_%20M-Pesa%20App%20für%20KMU.md) | Investoren-Due-Diligence-Bericht |

---

## 🎯 MVP-Ziele (90 Tage)

### Sprint 1 (Tag 1-30): Validierung
- **Ziel:** 20 Beta-Nutzer, >80% Aktivierung, >95% Parsing-Erfolg
- **Budget:** $25.000

### Sprint 2 (Tag 31-60): Akquise
- **Ziel:** 100+ WAU, CPI <$2, CAC <$15
- **Budget:** $35.000

### Sprint 3 (Tag 61-90): Monetarisierung
- **Ziel:** >2% Free-to-Paid, MRR >$500, 1 Partnership-MOU
- **Budget:** $20.000

→ Siehe [`docs/MVP-PLAN.md`](docs/MVP-PLAN.md) für Details

---

## 💡 Key Features (MVP)

### Kernfunktionalität
1. **Datei-Upload:** PDF/CSV-Upload (max. 10 MB)
2. **Parsing:** Automatische Extraktion von Datum, Betrag, Transaktions-ID, Details
3. **Kategorisierung:** Verkäufe, Miete, Lieferanten, Gehälter, etc.
4. **Export:** CSV/PDF-Report für eTIMS-Einreichung
5. **Offline-First:** Volle Funktionalität ohne Internet

### Post-MVP Features
- Automatische eTIMS-API-Integration (1-Klick-Submission)
- Smart-Kategorisierung (ML-basiert)
- Bank-Statement-Integration
- Multi-User-Zugang (Enterprise-Tier)

---

## 🏗️ Architecture (Android MVP)

### Clean Architecture + MVVM

```
┌─────────────────────────────────────────┐
│           UI Layer (Compose)            │
│  ┌──────────────────────────────────┐   │
│  │  UploadScreen  │  TransactionList│   │
│  └──────────────────────────────────┘   │
└────────────┬────────────────────────────┘
             │ observes StateFlow
┌────────────▼────────────────────────────┐
│     Presentation Layer (ViewModels)     │
│  ┌──────────────────────────────────┐   │
│  │ UploadVM  │  TransactionVM       │   │
│  └──────────────────────────────────┘   │
└────────────┬────────────────────────────┘
             │ calls UseCases
┌────────────▼────────────────────────────┐
│      Domain Layer (Use Cases)           │
│  ┌──────────────────────────────────┐   │
│  │ ParsePdfUseCase                  │   │
│  │ CategorizeTransactionUseCase     │   │
│  └──────────────────────────────────┘   │
└────────────┬────────────────────────────┘
             │ uses Repositories
┌────────────▼────────────────────────────┐
│       Data Layer (Repositories)         │
│  ┌──────────────────────────────────┐   │
│  │ TransactionRepository            │   │
│  └─────┬──────────────────┬─────────┘   │
│        │ Local (Room)     │ Remote (API)│
│  ┌─────▼──────┐    ┌──────▼──────┐      │
│  │ Room DB    │    │ Retrofit    │      │
│  └────────────┘    └─────────────┘      │
└─────────────────────────────────────────┘
```

---

## 🔐 Security

### Android
- **Local DB:** Room mit Encryption (SQLCipher - future)
- **API Keys:** BuildConfig (nicht in Git)
- **Network:** HTTPS enforced

### Backend
- **HTTPS:** Let's Encrypt
- **CORS:** Whitelist-basiert
- **Rate Limiting:** FastAPI-Limiter
- **Input Validation:** Pydantic Models

---

## 🧪 **TESTING STRATEGY**

### Backend Testing
- **Unit Tests:** pytest (>80% coverage target)
- **API Tests:** FastAPI TestClient
- **PDF Parsing Tests:** Real PDF validation suite (20+ samples)

### Frontend Testing
- **Unit Tests:** Vitest (React components)
- **E2E Tests:** Playwright (critical user flows)

### Mobile Testing (Phase 1)
- **Unit Tests:** Jest (React Native)
- **E2E Tests:** Detox (Android flows)

---

## 🤝 **CONTRIBUTING & BETA ACCESS**

Currently in Pre-MVP Validation Phase. Interested in:
- **Beta Testing:** Join waitlist at [m-recon.com] (to be launched)
- **SACCO Partnerships:** Contact via LinkedIn or email
- **Technical Contributions:** GitHub Issues for bug reports

**Partnership Inquiries:** See "KEY CONTACTS" section above

---

## 📜 **LICENSE**

Proprietary – All Rights Reserved  
© 2025 M-Recon. Patent Pending.

---
