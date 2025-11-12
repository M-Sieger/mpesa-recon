# Product Vision – M-Recon

**Erstellt:** 21. Oktober 2024  
**Aktualisiert:** 13. Januar 2025  
**Version:** 2.0 (Strategic Pivot)  
**Projekt:** M-Recon (M-Pesa Reconciliation for Loan Access)

---

## Problem Statement

**Primary Problem: Loan Rejection Due to Missing Financial Documentation**

Kenianische informelle SMEs stehen vor einer existenziellen Herausforderung:

1. **29% Loan Rejection Rate:** ~400.000 MSME-Kreditanträge/Jahr werden abgelehnt wegen "insufficient documentation" oder "incomplete financial records". Diese Unternehmer haben oft jahrelange M-Pesa-Historie, aber keine formalen Bücher.

2. **Informal Sector Lock-Out:** 80,8% der 7,4M kenianischen SMEs sind informell. Sie haben:
   - Keine Geschäftskonten (nur persönliche M-Pesa)
   - Keine Buchhaltungssoftware (Excel, wenn überhaupt)
   - Keine historischen Financial Statements
   - **ABER:** Vollständige M-Pesa-Transaktionshistorie (digital, verifizierbar)

3. **SACCOs Demand Better Documentation:** 357 deposit-taking SACCOs (3,3M members, KES 720B deposits) berichten, dass fehlende Financial Records der Hauptgrund für Kreditablehnungen sind. Aktuell verlangen sie:
   - 6-12 Monate Bankkontoauszüge (die die meisten nicht haben)
   - Business Financial Statements (die niemand erstellt)
   - **Alternative:** M-Pesa-Statements werden akzeptiert, aber manuell geprüft (zeitaufwändig für SACCOs)

**Konsequenzen:**
- SMEs bleiben im "Missing Middle" trapped: Zu groß für Mikrokredite, zu klein/informell für Bankkredite
- KES 20B/Jahr an potenziellem Kreditvolumen bleibt ungenutzt
- Informelle Unternehmer zahlen 10-20% Zinsen bei Shylocks statt 12-15% bei SACCOs
- Mangelhafte Finanzplanung durch fehlende Transparenz über Cashflow

**Secondary Problem (Time Waste, aber nicht Hauptschmerz):**
- Manuelle M-Pesa-Abstimmung kostet 2-3h/Woche
- eTIMS-Compliance-Druck (aber weniger akut als Kreditzugang)

---

## Target Audience

### Primäre Zielgruppe (MVP)
**Segment:** Informelle SME-Besitzer (Jua Kali, Mama Mboga, Dukas) via SACCO-Partnerships

**Charakteristika:**
- **Größe:** 1-5 Mitarbeiter (Ein-Personen-Betriebe bis Mikrounternehmen)
- **Sektor:** Einzelhandel, Food & Beverage, Handwerk, Dienstleistungen
- **Transaktionsvolumen:** 100-1000 M-Pesa-Transaktionen/Monat
- **Digitale Kompetenz:** Basic (nutzen M-Pesa täglich, WhatsApp, aber keine Buchhaltungssoftware)
- **Geographie:** Nairobi, Mombasa, Kisumu, Nakuru (urban/peri-urban)
- **Finanzstatus:** 
  - SACCO-Mitglied ODER erwägt Beitritt
  - Hat M-Pesa-Konto (persönlich, manchmal Paybill/Till)
  - Kein Geschäftskonto bei Bank
  - Braucht KES 50K-150K Business Loan

**Pain Hierarchy:**
1. **Kreditzugang** (existenzielles Problem) ← HAUPTFOKUS
2. Cashflow-Transparenz (nice-to-have)
3. eTIMS-Compliance (zukünftiges Problem)
4. Zeit sparen bei Buchhaltung (Bonus)

**Nutzungskontext:**
- **Wo:** Im Laden/Büro, zu Hause (PDF auf Handy gespeichert)
- **Wann:** Wenn Kreditantrag ansteht ODER monatlich für Übersicht
- **Gerät:** Android-Smartphone (Budget-Phones: Samsung Galaxy A-Serie, Tecno, Infinix)
- **Konnektivität:** Unzuverlässig → **Offline-First absolut kritisch**

### Sekundäre Zielgruppe (Post-MVP)
**Frauengeführte SMEs (40% des Marktes) via Women Enterprise Fund:**
- Noch stärker von Kreditbarrieren betroffen (Gender Bias bei Kreditvergabe)
- WEF verlangt Bankkonten (Partnership-Opportunity: "Wir helfen bei Kontoeröffnung")
- Konzentriert in High-Transaction-Sektoren (Retail, Food → mehr M-Pesa-Daten)

**SACCO-Mitglieder (Primary Channel, B2B2C):**
- 3,3M Mitglieder in deposit-taking SACCOs
- 70,6% Digital Adoption (bereits an mobile channels gewöhnt)
- SACCOs haben Incentive, Kreditvergabe zu verbessern (mehr Zinseinkommen)

---

## Vision Statement

**M-Recon macht Kreditzugang für informelle kenianische SMEs möglich, indem es ihre M-Pesa-Historie in SACCO/Bank-ready Financial Reports verwandelt – damit hunderttausende Unternehmer das Kapital bekommen, das sie zum Wachsen brauchen.**

**In 3 Jahren:** 
- **100.000+ SMEs** haben erfolgreiche Kreditanträge mit M-Recon gestellt
- **50+ SACCO-Partnerships** (representing 500K+ members)
- **Established Category:** "M-Pesa Financial Records" als akzeptierter Standard für Loan Applications
- **Market Leader:** in PDF-based bookkeeping for informal sector in East Africa

---

## MVP User Stories (Must-Have) - LOAN-ACCESS FOKUS

### User Story 1: M-Pesa-PDF hochladen und entschlüsseln
**Als** informeller SME-Besitzer  
**möchte ich** meinen passwort-geschützten M-Pesa-PDF-Statement mit meiner ID Number hochladen  
**damit** die App alle Transaktionen automatisch ausliest.

**Acceptance Criteria:**
- [ ] Upload-Interface für PDF-Dateien (max. 10 MB)
- [ ] Password-Handling: User gibt ID Number ein → App entschlüsselt PDF
- [ ] Parsing-Erfolgsrate >90% für Standard-M-Pesa-Statements (Personal, Business, Pochi)
- [ ] Extrahierte Felder: Datum, Transaktions-ID, Details (Zahler/Empfänger), Paid In, Withdrawn, Balance
- [ ] Offline-Upload möglich (Verarbeitung lokal, Sync bei Online-Verbindung)
- [ ] Fehlermeldung bei Parsing-Fehler mit Manual-Entry-Option

**Why This Matters for Loan Access:**
→ SACCOs/Banks akzeptieren M-Pesa-Statements, aber manuelles Review kostet Zeit. Automatische Extraktion beschleunigt Approval-Prozess.

### User Story 2: Transaktionen kategorisieren (Income vs Expense)
**Als** SME-Besitzer  
**möchte ich** sehen, welche Transaktionen Einnahmen (Verkäufe) vs. Ausgaben (Lieferanten, Miete) sind  
**damit** ich meinem SACCO zeigen kann, dass mein Business profitabel ist.

**Acceptance Criteria:**
- [ ] Vordefinierte Kategorien: **Income** (Verkäufe, Kundeneinnahmen) vs **Expenses** (Einkäufe, Miete, Gehälter, Transport)
- [ ] Smart-Suggestions: "M-Changa contribution" → Expense, "Received from John Doe" → Income
- [ ] Bulk-Kategorisierung: Alle Transaktionen von "ABC Suppliers" → Expense
- [ ] Manual Override: User kann Kategorien korrigieren
- [ ] Notizen pro Transaktion (z.B. "Payment for 50kg maize")

**Why This Matters for Loan Access:**
→ SACCOs brauchen Income/Expense Split, um Debt-Service-Coverage zu kalkulieren (Kann Unternehmer den Loan zurückzahlen?).

### User Story 3: Financial Summary Report exportieren (Loan-Ready)
**Als** SME-Besitzer  
**möchte ich** einen professionellen Financial Report (6-12 Monate) exportieren  
**damit** ich ihn meinem SACCO/Bank mit Kreditantrag vorlege.

**Acceptance Criteria:**
- [ ] Export als PDF: **"M-Recon Certified Financial Summary"**
  - Total Income (6/12 months)
  - Total Expenses (breakdown by category)
  - Average Monthly Profit
  - Transaction Count (zeigt Business-Activity)
  - "Verified by M-Recon (PDF parsing accuracy: 95%)"
- [ ] Export als CSV (für manuelle eTIMS-Eingabe später)
- [ ] Zeitraum-Filter: 6 Monate (Standard für SACCOs), 12 Monate, Custom
- [ ] Offline-Funktion: Report wird lokal generiert
- [ ] WhatsApp-Share-Button (direkt an SACCO Loan Officer senden)

**Why This Matters for Loan Access:**
→ Dies ist das Kernprodukt. SACCOs akzeptieren diese Reports als Ersatz für Bankkontoauszüge. "Loan-Ready Badge" signalisiert Qualität.

---
---

## Deferred User Stories (Phase 2-3, Month 4+)

### User Story 4: eTIMS API Integration (Phase 2)
**Als** SME-Besitzer  
**möchte ich** meine kategorisierten Ausgaben automatisch zu eTIMS hochladen  
**damit** ich Tax-Compliant bin ohne manuelle Dateneingabe.

**Why Deferred:** 
- eTIMS API-Integration ist komplex (KRA VSCU API, OAuth)
- MVP-Fokus ist Loan-Access, nicht Tax-Compliance
- Manuelle CSV-Export genügt für frühe Adopter
- Wird Premium-Feature in Phase 2 (Differentiator vs Pay Hero)

### User Story 5: Bank Statement Support (Phase 3)
**Als** fortgeschrittener User  
**möchte ich** auch KCB/Equity-Statements hochladen  
**damit** ich ein vollständiges Financial Picture habe (M-Pesa + Bank).

**Why Deferred:** 
- MVP fokussiert auf Informal Sector (die haben keine Bankkonten)
- Bank-Statement-Parsing braucht eigene Parser (verschiedene Formate)
- Erst relevant wenn 10K+ users (dann lohnt sich Investment)

---

## Success Metrics - LOAN-ACCESS FOKUS

### Validation Phase (Jan 13-27, 2025) ← CURRENT
- [ ] **2+ SACCO partnerships** (signed LOIs)
- [ ] **100+ waitlist signups**
- [ ] **PDF parsing PoC:** 90%+ accuracy on 20 real PDFs
- [ ] **10 customer interviews:** 60%+ WTP at KES 500/mo

### MVP Phase (Feb-Mar 2025)
- [ ] **1,500 active users** (via 3 SACCO pilots)
- [ ] **50%+ adoption** within pilot groups
- [ ] **90%+ parsing accuracy** (production)
- [ ] **15-20% loan approval uplift** (measured vs control group)
- [ ] **<10% monthly churn**
- [ ] **NPS >4**

### Scale Phase (Apr-Dec 2025)
- [ ] **10,000 active users** (10 SACCOs)
- [ ] **KES 5M ARR** (break-even)
- [ ] **25% of users** report successful loan application with M-Recon report
- [ ] **Seed funding closed:** USD 250-500K
- [ ] **eTIMS integration live** (differentiator)

### North Star Metric
**"Number of SMEs who successfully obtained loans using M-Recon reports"**
- Target Year 1: 2,500 successful loan applications (25% conversion from 10K users)
- Proxy metric (before we can track full cycle): "Reports exported and shared via WhatsApp"

---

## Tech Stack - PDF-FIRST, OFFLINE-FIRST

### MVP (Phase 1: Feb-Mar 2025)

#### Backend
- **Framework:** FastAPI (Python 3.11+)
- **Database:** Supabase (PostgreSQL + Auth + Storage)
- **PDF Parsing:** PDFPlumber + custom regex patterns
- **Authentication:** Supabase Auth (email/phone)
- **File Storage:** Supabase Storage (encrypted PDFs)
- **Deployment:** Railway.app or Fly.io (pay-as-you-grow)

**Why This Stack:**
- FastAPI: Fast development, auto-docs, async support
- Supabase: Reduces backend complexity (auth, storage, DB in one)
- PDFPlumber: Proven for M-Pesa PDF parsing (80-95% accuracy expected)
- Railway: Simple deployment, scales easily, Kenya-accessible

#### Frontend (Web)
- **Framework:** React 18 + TypeScript
- **Styling:** Tailwind CSS (fast iteration)
- **State Management:** Zustand (lightweight)
- **Build Tool:** Vite (fast dev server)
- **Deployment:** Vercel (global CDN, Kenya-optimized)

**Purpose:** Waitlist page + Admin dashboard + Beta testing (web-first for speed)

#### Mobile (Android)
- **Framework:** React Native + Expo (faster iteration than native Kotlin)
- **Offline Storage:** SQLite (via expo-sqlite)
- **Background Sync:** Expo Task Manager
- **PDF Handling:** react-native-pdf + expo-file-system

**Why React Native:**
- Faster MVP development (shared codebase with web)
- Expo simplifies offline-first architecture
- Easy to pivot to native if needed (eject from Expo)
- Good enough performance for CRUD app (not gaming)

**Why NOT Native Kotlin (originally planned):**
- 8-week timeline too tight for native development
- React Native gets us 80% of benefits with 50% of time
- Can always go native in Phase 2 if performance issues

### Post-MVP (Phase 2-3: Apr-Dec 2025)

#### eTIMS Integration
- **API:** KRA VSCU API (OAuth 2.0)
- **Storage:** Encrypted eTIMS credentials in Supabase
- **Sync:** Background job (checks for new transactions, auto-submits)

#### ML Categorization
- **Model:** scikit-learn Random Forest (simple, interpretable)
- **Training Data:** Anonymized user categorizations (opt-in)
- **Deployment:** FastAPI endpoint (inference)

#### USSD Version
- **Platform:** Africa's Talking USSD API
- **Use Case:** Ultra-low-data users (feature phones)
- **Limitation:** Text-only interface, no PDF upload (SMS parsing instead)

---
## Competitive Positioning - SACCO-PARTNERSHIP MOAT

### Direct Competitors
**Pay Hero (Main Competitor):**
- **Strength:** API-first (Daraja integration), formal businesses focus, established brand
- **Weakness:** Excludes informal sector (70%+ of market), NO loan-access positioning, NO SACCO partnerships
- **Our Advantage:** PDF-first (inclusive), Offline-first, Loan-access focus, SACCO network effects

### Indirect Competitors
- **Excel/Manual Books:** Free but time-consuming, no loan-ready reports
- **Local Accountants:** KES 5K-10K/month, not accessible to informal SMEs
- **Branch/Tala:** Offer loans but don't solve documentation problem

### White Space (Our Opportunity)
**Offline + PDF + Loan-Access + SACCO Partnerships = NOBODY**

### Defensibility (Moat)
1. **SACCO Network Effects:** 5 SACCOs × 10K members = 50K users → Hard to switch
2. **Data Moat:** 25K+ parsed statements → ML training data for categorization
3. **Partnership Lock-In:** SACCOs won't switch easily (integration costs)
4. **Brand:** "M-Recon Certified Reports" become trusted standard for loan applications

---

## GTM Strategy - B2B2C via SACCOs

### Phase 1: SACCO Partnerships (70% of Users)
**Target:** 5 pilot SACCOs in Q1-Q2 2025

**Pitch to SACCOs:**
- "Reduce member loan rejections by 25%"
- "Increase loan portfolio (more interest income)"
- "Differentiate from competitors (digital innovation)"
- "Free for first 100 members, then KES 10K/month partnership fee"

**Precedents:**
- Kwara (SACCO digital platform): Doubled memberships in 1 year
- Branch (credit scoring): SACCO partnerships proven model

**Target SACCOs:**
1. Kimisitu SACCO (Winner of Enterprise IT Adoption 2025)
2. Finmat SACCO (AI/data analytics focus)
3. Tower SACCO (Member empowerment)
4. Police SACCO (M-Tawi success)
5. Kenya Re SACCO (Bank statement requirements for loans)

### Phase 2: Consumer Waitlist (20% - Validation)
**Target:** 100+ signups in 30 days

**Channels:**
- Facebook groups (Kenya SME groups)
- Grace's network (local validation)
- Paid ads (Facebook, Google - low budget)

### Phase 3: WEF Partnership (10% - Long-term)
**Target:** 50-100 women's groups (500-1,000 women)

**Challenge:** WEF requires bank accounts (barrier to entry)

**Solution:** Partner with Postbank/Equity for easy account opening
- M-Recon helps meet bank account documentation requirements
- WEF members use M-Recon to maintain good financial records

---

## Business Model - B2B2C Freemium

### Pricing
**Free Tier:**
- 50 transactions/month
- Basic reports (PDF/CSV)
- Manual categorization

**Premium Tier: KES 500/month (USD ~$4)**
- Unlimited transactions
- Auto-categorization (ML-powered in Phase 2)
- Priority support (WhatsApp)
- "Loan-Ready Badge" on reports
- Offline-first sync

**SACCO Partnership Tier: KES 10K-25K/month**
- Free for first 100 members
- Then bulk discount (KES 300/user/month)
- Co-branded reports
- Dedicated support
- API integration (future)

### Bewusste Design-Entscheidungen:
- **Keine direkte M-Pesa-API-Integration:** File-Upload-basiert (keine API-Lizenz von Safaricom nötig, schneller Go-to-Market)
- **Keine Blockchain/Web3:** Kein Overkill für das Problem, fokussiert auf pragmatische Lösung
- **Keine eigene PSP-Lizenz:** Partnerschaft mit Pesapal (siehe Tech-Stack)

---

## Marktgröße & Opportunity

### Total Addressable Market (TAM)
**7,4 Millionen KKMU** in Kenia (KNBS-Daten)
- 40% BIP-Beitrag
- 14,9 Millionen Beschäftigte

### Serviceable Addressable Market (SAM)
**3,5 Millionen KMU** (50% des TAM)
- Kriterien: Nutzen M-Pesa geschäftlich + besitzen Smartphone
- Basierend auf: 35,82 Mio. aktive M-Pesa-Nutzer + 80,8% Smartphone-Penetration

### Serviceable Obtainable Market (SOM – Jahr 1)
**17.500 zahlende KMU** (0,5% des SAM)
- Konservativer Einstiegspunkt für Seed-Phase
- Fokus: Early Adopters in städtischen Gebieten + eTIMS-Compliance-Pressure

---

## Regulatorischer Katalysator: eTIMS-Mandat

### Was ist eTIMS?
Electronic Tax Invoice Management System (eTIMS) der Kenya Revenue Authority (KRA):
- **Verpflichtung:** ALLE Unternehmen müssen Betriebsausgaben mit eTIMS-Rechnungen belegen
- **Gilt für:** MwSt-registrierte UND nicht-registrierte Unternehmen (auch Informal-Sector)
- **Konsequenz bei Nicht-Compliance:** Ausgaben können NICHT steuerlich geltend gemacht werden → höhere Steuerlast

### Warum das M-Recon treibt:
- **Dringlichkeit:** Compliance ist keine Option, sondern Notwendigkeit
- **Primäres Wertversprechen:** "Sparen Sie Geld bei Ihren Steuern" (nicht nur "Sparen Sie Zeit")
- **Markt-Timing:** Regulatorischer Rückenwind reduziert Customer-Education-Kosten drastisch
- **Positionierung:** M-Recon als **Compliance-Utility** (nicht nur Produktivitäts-Tool)

---

## Go-to-Market-Strategie (Kurzfassung)

### Primäre Kanäle:
### Revenue Projections (Year 1)
**Optimistic Case (SACCO-Partnership Success):**
- 10,000 users × KES 500/mo × 12 months = KES 60M (~USD $460K ARR)
- 10 SACCOs × KES 15K/mo × 12 months = KES 1.8M (~USD $14K ARR)
- **Total:** ~USD $475K ARR

**Realistic Case:**
- 5,000 users × KES 500/mo × 12 months = KES 30M (~USD $230K ARR)
- 5 SACCOs × KES 10K/mo × 12 months = KES 600K (~USD $4.6K ARR)
- **Total:** ~USD $235K ARR

**Break-Even Target:** 1,500 users (KES 9M ARR = USD ~$70K)

### Unit Economics
**LTV:CAC Ratio:** 41:1 (via SACCO partnerships)
- LTV: KES 12,000 (KES 500/mo × 24 months avg. lifetime)
- CAC: KES 300 (partnership-driven, low direct spend)

**Payback Period:** <1 month (extremely fast ROI)

---

## Non-Functional Requirements

### Performance
- **Mobile App:**
  - App Start: <2s (cold), <0.5s (warm)
  - PDF Parsing: <5s for 100-transaction statement
  - Report Generation: <3s for 1000 transactions
  - Offline-first: 100% functionality without internet

### Security
- **Authentication:** Supabase Auth (email/phone OTP)
- **Data Encryption:**
  - In-Transit: HTTPS/TLS 1.3
  - At-Rest: SQLite encryption (mobile), PostgreSQL encryption (backend)
- **File Security:** 
  - Max file size: 10MB
  - Format validation: PDF only
  - ID number verification for password-protected PDFs

### Accessibility
- **Mobile:** TalkBack compatibility, min 48x48dp touch targets, 4.5:1 color contrast
- **Web:** WCAG 2.2 AA compliance

### Offline-Functionality
- **Critical:** App MUST work 100% offline (no internet = no dealbreaker)
- **Local Storage:** Last 180 days of transactions (~50MB max)
- **Sync Strategy:** Background sync when online, exponential backoff on failures

---

## Out-of-Scope (MVP - Deferred to Phase 2+)

### NOT in MVP (but on Roadmap):
- [ ] **eTIMS API Integration:** Manual CSV export for now → Auto-submission in Phase 2
- [ ] **SMS Parsing:** READ_SMS permission + complex UX → Phase 3
- [ ] **Multi-User Access:** Single-user only in MVP → Team features later
- [ ] **Bank Statement Support:** M-Pesa only → Bank integration Phase 3
- [ ] **AI Forecasting:** ML-based cashflow predictions → Phase 4
- [ ] **Multi-Currency:** KES only → USD/EUR support if international demand
- [ ] **iOS Native App:** React Native covers iOS → Native only if needed
- [ ] **Accounting Software Integration:** QuickBooks/Xero APIs → Phase 4

---

## Key Market Research Findings

### Problem Validation
- **7.4M SMEs** in Kenya (80.8% informal)
- **29% loan rejection rate** due to insufficient documentation (~400K applications/year)
- **Average loan size:** KES 50K-150K for MSMEs
- **Total addressable credit:** KES 20B/year locked due to documentation gap

### SACCO Opportunity
- **357 deposit-taking SACCOs** (SASRA-regulated)
- **3.3M members**, KES 720B in deposits
- **70.6% digital adoption** (mobile channels)
- **Precedent:** Kwara doubled SACCO memberships in 1 year with digital platform

### Competitor Gap
- **Pay Hero:** API-first (excludes informal sector), NO loan-access focus, NO SACCO partnerships
- **White Space:** Offline + PDF + Loan-Access + SACCO partnerships = **NOBODY**

---

## Architecture Decision Records (ADRs)

### ADR-001: React Native vs Native Android
**Decision:** React Native + Expo for MVP  
**Status:** ✅ CHANGED (from original Native Kotlin plan)  
**Date:** 2025-01-13

**Reason:**
- **8-week timeline:** Native Kotlin too slow for MVP (React Native 50% faster)
- **Shared codebase:** Web + Mobile components reusable
- **Offline-first:** Expo SQLite + Task Manager handles offline well
- **Pivot flexibility:** Can eject to native if performance issues arise

**Trade-offs:**
- ✅ Faster time-to-market
- ✅ Smaller team requirements
- ⚠️ Slightly larger bundle size
- ⚠️ Native performance not critical for CRUD app

### ADR-002: PDF-First vs API-First
**Decision:** PDF upload (not Daraja API)  
**Status:** ✅ APPROVED  
**Date:** 2025-01-13

**Reason:**
- **Inclusivity:** Daraja API requires registered business (excludes 70%+ informal SMEs)
- **Universality:** Everyone has M-Pesa PDFs (even without Paybill/Till number)
- **No Partnership Friction:** No need for Safaricom API license (months of negotiations)
- **User Control:** Users decide what data to share (privacy advantage)

**Trade-offs:**
- ✅ Broader market access
- ✅ Faster MVP launch
- ⚠️ Parsing accuracy challenge (mitigated with 90%+ target)

### ADR-003: SACCO-First vs Consumer-First GTM
**Decision:** B2B2C via SACCO partnerships  
**Status:** ✅ APPROVED  
**Date:** 2025-01-13

**Reason:**
- **Lower CAC:** KES 300 via partnerships vs KES 1,500+ direct (5x better)
- **Faster scale:** 1 SACCO = 10K potential users
- **Credibility:** SACCO endorsement = trust signal for members
- **Precedent:** Kwara, Branch proven SACCO partnership model works

**Trade-offs:**
- ✅ 41:1 LTV:CAC ratio
- ✅ Sustainable growth
- ⚠️ Partnership sales cycle (2-3 months)
- ⚠️ Dependency on SACCO buy-in

---

## Next Steps

### Immediate (This Week: Jan 13-19)
- [ ] LinkedIn outreach to 5 SACCO CEOs
- [ ] Download 3 M-Pesa PDFs for parsing PoC
- [ ] Update waitlist page with loan-access messaging
- [ ] Schedule Grace interviews (10 SMEs for WTP validation)

### Short-Term (Next 2 Weeks: Jan 13-27)
- [ ] PDF parsing PoC: 90%+ accuracy on 20 PDFs
- [ ] SACCO conversations: 2-3 calls scheduled
- [ ] Waitlist: 30+ signups
- [ ] Decision Gate (Jan 27): GO/PIVOT/STOP

### Medium-Term (Feb-Mar 2025: If GO)
- [ ] MVP Build: FastAPI backend + React Native app
- [ ] SACCO Pilot Deck creation
- [ ] Partnership agreements with 2-3 SACCOs
- [ ] Pilot launch: 500-1,000 users

---

## Review & Approval

**Status:** ✅ APPROVED (v2.0 - Strategic Pivot)  
**Date:** 13 January 2025

**Key Changes from v1.0:**
1. **Primary Pain:** Loan rejection >> time-saving from bookkeeping
2. **GTM:** SACCO partnerships >> consumer-first
3. **Product:** PDF-first offline bookkeeping for loan-access
4. **Tech:** React Native + Expo >> Native Kotlin (speed priority)
5. **Timeline:** 2-week validation >> then GO/NO-GO decision

**Next Document:** [`MVP-PLAN.md`](./MVP-PLAN.md) - Detailed 90-day execution plan

---

**Version History:**
- v1.0 (21.10.2024) – Initial Product Vision (bookkeeping + eTIMS focus)
- v2.0 (13.01.2025) – Strategic Pivot (loan-access + SACCO partnerships focus)

---

**END OF PRODUCT VISION v2.0**
