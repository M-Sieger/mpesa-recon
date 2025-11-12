# Roadmap – M-Recon (6-Month + Long-Term)

**Created:** 21. Oktober 2024  
**Updated:** 13. Januar 2025  
**Version:** 2.0 (Strategic Pivot)  
**Timeline:** Jan 2025 - Dec 2025

---

## Overview

**Mission:** Scale from 0 to 10,000 users via SACCO partnerships, achieve KES 5M ARR (break-even), secure seed funding.

**Phases:**
- **Phase 0:** Validation (Jan 13-27) - Prove SACCO interest + PDF parsing
- **Phase 1:** MVP Build (Feb-Mar) - Build product
- **Phase 2:** Pilot Launch (Apr-Jun) - 3 SACCOs, 1,500 users
- **Phase 3:** Scale (Jul-Dec) - 10 SACCOs, 10,000 users
- **Phase 4:** Expansion (2026+) - Regional expansion, new products

---

## PHASE 0: VALIDATION (Jan 13-27, 2025) ← CURRENT

**Goal:** Validate Product-Market Fit assumptions

**Deliverables:**
- [ ] 2+ SACCO partnerships (verbal LOIs)
- [ ] PDF parsing PoC: 90%+ accuracy on 20 real PDFs
- [ ] 100+ waitlist signups
- [ ] 60%+ WTP at KES 500/mo (10 customer interviews)

**Decision Gate (Jan 27):**
- ✅ GO: Start MVP build if all criteria met
- ⚠️ PIVOT: Adjust strategy if weak signals
- ❌ STOP: Reconsider if no validation

**Timeline:** 2 weeks  
**Budget:** $500

→ See [`MVP-PLAN.md`](./MVP-PLAN.md) for detailed week-by-week plan

---

## PHASE 1: MVP BUILD (Feb 1 - Mar 31, 2025)

**Goal:** Ship working product: Backend + Web + Mobile

**Timeline:** 8 weeks  
**Budget:** $10K

→ See [`MVP-PLAN.md`](./MVP-PLAN.md) Phase 1 section for full details

---

## PHASE 2: PILOT LAUNCH (Apr 1 - Jun 30, 2025)

**Goal:** Launch 3 SACCO pilots, validate loan-access value prop

**Target:** 1,500 active users across 3 SACCOs  
**Timeline:** 3 months  
**Budget:** $2.7K

→ See [`MVP-PLAN.md`](./MVP-PLAN.md) Phase 2 section for full details

---

## PHASE 3: SCALE (Jul 1 - Dec 31, 2025)

**Goal:** Scale to 10 SACCOs, 10,000 users, achieve break-even

### Q3 2025 (Jul-Sep): Expand SACCO Partnerships

**Target:**
- 7 more SACCOs (total: 10)
- 5,000 users (halfway to 10K)
- KES 2.5M ARR

**New Features (Differentiators):**

**Timeline:** Monat 5-6 (4 Wochen)  
**Impact:** Time-to-Value -40%, Retention +15%

---

#### 2.3 PWA-Launch (iOS + Desktop)
**Problem:** iOS-Nutzer ausgeschlossen (ca. 15% Markt)  
**Lösung:** Progressive Web App mit Offline-Support

**Deliverables:**
- [ ] **React PWA** (Vite + TypeScript + Tailwind)
  - [ ] Aktuellen React-Prototype als Basis nutzen
  - [ ] Service Worker für Offline-Funktionalität
  - [ ] IndexedDB für lokale Datenhaltung
  - [ ] Web-Manifest für PWA-Installation
- [ ] **Shared-Backend** (FastAPI bereits vorhanden)
  - [ ] Identische API-Endpoints wie Android-App
  - [ ] CORS-Konfiguration für Web-Clients
- [ ] **Responsive Design** (Mobile + Desktop)
  - [ ] Mobile-First Design (iOS Safari-optimiert)
  - [ ] Desktop-Layout für größere Screens
  - [ ] Touch + Mouse/Keyboard-Input

**Timeline:** Monat 5-6 (6 Wochen parallel zu 2.2)  
**Impact:** TAM +15%, neue Nutzersegmente (iOS-User, Office-Worker)

**Note:** Aktueller `client/` Ordner wird als Basis verwendet

---

#### 2.4 Organische Akquise-Kanäle
**Problem:** Paid-CAC steigt bei Skalierung  
**Lösung:** Content + Referral-Programm

**Deliverables:**
- [ ] SEO-optimierter Blog (WordPress/Ghost)
  - Top-10-Keywords: "eTIMS compliance Kenya", "M-Pesa bookkeeping"
- [ ] YouTube-Channel (Swahili + Englisch)
  - Tutorial: "eTIMS in 5 Minuten erklärt"
  - Testimonials von KMU-Besitzern
- [ ] Referral-Programm
  - "Empfehle 3 Freunde → 1 Monat Premium kostenlos"
  - In-App-Incentive

**Timeline:** Monat 4-6 (kontinuierlich)  
**Impact:** Organischer Traffic 40% des Gesamt-Traffics, CAC -25%

---

### Milestones (Phase 2)

| Woche | Milestone | Metrik |
|-------|-----------|--------|
| Woche 16 | eTIMS-API Live (Beta) | 50 Premium-Upgrades |
| Woche 20 | Smart-Kategorisierung Live | Kategorisierungs-Zeit -40% |
| Woche 22 | PWA Launch | 10% Traffic von iOS/Desktop |
| Woche 24 | 1.000 zahlende Nutzer | MRR $47.000 |

---

## Phase 3: Skalierung (Monat 7-12)

### Ziel
Von 1.000 auf 17.500 zahlende Nutzer (SOM Jahr 1)

### Schlüssel-Initiativen

#### 3.1 B2B-Enterprise-Tier
**Problem:** Größere KMU (10-50 Mitarbeiter) brauchen Multi-User  
**Lösung:** Team-Features + erweiterte Permissions

**Deliverables:**
- [ ] Multi-User-Zugang (Owner, Accountant, Viewer-Rollen)
- [ ] Team-Dashboard (zentrales Reporting)
- [ ] Audit-Log (wer hat was geändert)
- [ ] Enterprise-Pricing: KSh 5.000/Monat (bis 10 User)

**Timeline:** Monat 7-9  
**Impact:** ARPA +60% für Enterprise-Kunden

---

#### 3.2 Bank-Statement-Integration
**Problem:** KMU nutzen M-Pesa + Bankkonto  
**Lösung:** Support für Standard-Bank-PDF/CSV

**Deliverables:**
- [ ] Parser für Top-3-Banken (KCB, Equity, Co-op Bank)
- [ ] Unified-Transaction-View (M-Pesa + Bank kombiniert)
- [ ] Duplicate-Detection (gleiche Transaktion in M-Pesa + Bank)

**Timeline:** Monat 8-10  
**Impact:** TAM +20% (größere KMU mit Bankkonten)

---

#### 3.3 Credit-Score-Partnership
**Problem:** KMU brauchen Kredite, aber keine Credit-History  
**Lösung:** Anonymisierte Daten für Kreditbewertung nutzen

**Deliverables:**
- [ ] Partnerschaft mit Mikrofinanz-Institution (z.B. KWFT)
- [ ] Opt-in: User erlaubt Sharing von Cashflow-Data für Kredit-Score
- [ ] "Kredit-Readiness-Check" in App
- [ ] Revenue-Share: 5% Vermittlungsprovision

**Timeline:** Monat 10-12  
**Impact:** Neue Revenue-Stream, höhere User-Retention

---

#### 3.4 Expansion: Nairobi → National
**Problem:** Bisher nur städtische Gebiete  
**Lösung:** Offline-First + USSD-Fallback für Low-Connectivity

**Deliverables:**
- [ ] USSD-Code (*XXX#) für Basic-Funktionen (Balance-Check, Statement-Request)
- [ ] Data-Compression für langsamere Netzwerke
- [ ] Partnership mit Safaricom für Co-Marketing (Rural-Areas)

**Timeline:** Monat 11-12  
**Impact:** TAM +30% (ländliche KMU)

---

### Milestones (Phase 3)

| Monat | Milestone | Metrik |
|-------|-----------|--------|
| Monat 9 | Enterprise-Tier Live | 200 Enterprise-Kunden |
| Monat 10 | Bank-Integration Live | 30% Nutzer integrieren Bank |
| Monat 11 | First Credit-Partnership | 500 Loan-Applications |
| Monat 12 | 17.500 zahlende Nutzer | MRR $820.000 |

---

## Phase 4: Markt-Expansion (Monat 13-24)

### Ziel
Von 17.500 auf 50.000+ zahlende Nutzer durch geografische Expansion

### Schlüssel-Initiativen

#### 4.1 Uganda & Tanzania Launch
**Problem:** Ostafrika-Märkte ähnlich zu Kenia  
**Lösung:** Lokalisierung + Payment-Adapter

**Deliverables:**
- [ ] Support für MTN Mobile Money (Uganda)
- [ ] Support für Tigo Pesa, M-Pesa Tanzania
- [ ] Lokale Compliance (URA, TRA Tax-Systeme)
- [ ] Local-Language-Support (Luganda, Swahili-Varianten)

**Timeline:** Monat 13-18  
**Impact:** TAM +200% (Uganda 1,2 Mio. KMU, Tanzania 3 Mio. KMU)

---

#### 4.2 Accounting-Software-Integration
**Problem:** Power-User wollen Export zu QuickBooks/Xero  
**Lösung:** API-Integrationen

**Deliverables:**
- [ ] QuickBooks-Integration (OAuth + Transaction-Sync)
- [ ] Xero-Integration
- [ ] Generic-CSV-Export (für andere Tools)

**Timeline:** Monat 16-18  
**Impact:** Retention +20% für Power-User

---

#### 4.3 Whitelabel-SaaS (B2B2C)
**Problem:** Banken/MFIs wollen eigene Branding  
**Lösung:** Whitelabel-Lösung für Finanzinstitutionen

**Deliverables:**
- [ ] Whitelabel-SDK (Custom-Branding)
- [ ] Multi-Tenant-Architecture (Backend)
- [ ] Partner-Dashboard (Nutzer-Management)
- [ ] Pricing: $50.000/Jahr + Revenue-Share

**Timeline:** Monat 19-24  
**Impact:** Neue Revenue-Stream, B2B-Skalierung

---

### Milestones (Phase 4)

| Monat | Milestone | Metrik |
|-------|-----------|--------|
| Monat 18 | Uganda Launch | 5.000 ugandische Nutzer |
| Monat 20 | Tanzania Launch | 8.000 tansanische Nutzer |
| Monat 22 | QuickBooks-Integration | 1.000 Power-User nutzen es |
| Monat 24 | 50.000 zahlende Nutzer | MRR $2,35M |

---

## Finanzplan-Übersicht

### Revenue-Projektion

| Phase | Zeitraum | Zahlende Nutzer | ARPA (Jahr) | ARR |
|-------|----------|-----------------|-------------|-----|
| MVP | M0-3 | 11 | $47 | $517 |
| PMF | M4-6 | 1.000 | $47 | $47.000 |
| Scale | M7-12 | 17.500 | $47 | $822.500 |
| Expansion | M13-24 | 50.000 | $50 | $2,5M |

### Funding-Bedarf

| Runde | Zeitpunkt | Betrag | Verwendung |
|-------|-----------|--------|------------|
| **Pre-Seed** | Monat 0 | $80K | MVP (90 Tage) |
| **Seed** | Monat 3 | $500K | PMF + Scale (M4-12) |
| **Series A** | Monat 12 | $2M | Expansion (M13-24) |

---

## Team-Wachstum

| Phase | Team-Größe | Neue Rollen |
|-------|------------|-------------|
| MVP | 4 | Gründer, 2 Devs, 1 Marketing |
| PMF | 8 | +2 Devs, +1 Product Manager, +1 Sales |
| Scale | 15 | +4 Devs, +1 DevOps, +1 Customer Success, +1 Data Analyst |
| Expansion | 25 | +5 Devs, +2 Sales, +2 Support, +1 Country Manager (Uganda/Tanzania) |

---

## Risiko-Matrix (Long-Term)

| Risiko | Eintritts-Zeitpunkt | Mitigation |
|--------|---------------------|------------|
| Safaricom launched eigenes Tool | M12-24 | First-Mover-Advantage, Partnerships, Feature-Lead |
| Regulatorische Änderungen (eTIMS) | M6-18 | Flexible Architektur, enge KRA-Kommunikation |
| Währungsrisiko (KES-Volatilität) | M13+ | USD-Pricing für internationale Expansion |
| Data-Privacy-Regulierung | M18+ | GDPR-ähnliche Compliance von Tag 1 |

---

## Exit-Szenarien (5-7 Jahre)

### Option 1: Acquisition
**Potenzielle Käufer:**
- Safaricom (strategisch)
- Internationale FinTech (Stripe, Paystack)
- Accounting-Software (QuickBooks, Xero)

**Bewertung:** $50-100M (basierend auf 10x ARR bei $10M ARR)

### Option 2: IPO/SPAC
**Voraussetzungen:**
- ARR >$50M
- Multi-Country-Präsenz (3+ Märkte)
- Profitabilität oder klarer Path-to-Profitability

### Option 3: Strategic Partnership
**Beispiel:** Joint-Venture mit Safaricom (M-Pesa for Business Integration)

---

## Nächste Schritte

1. **Pre-Seed-Fundraising** ($80K) → MVP starten
2. **Sprint 1 kickoff** (siehe MVP-PLAN.md)
3. **Nach Tag 90:** Seed-Pitch ($500K) basierend auf MVP-Metriken

**Status:** ⏳ Roadmap erstellt – bereit für Phase 1-Start
