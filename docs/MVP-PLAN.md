# MVP-Plan – M-Recon (90 Tage)

**Erstellt:** 21. Oktober 2025  
**Version:** 1.0  
**Ziel:** Lauffähiges MVP mit 17.500 zahlenden Nutzern in 12 Monaten

---

## Sprint-Übersicht

| Sprint | Dauer | Hauptziel | Budget |
|--------|-------|-----------|--------|
| Sprint 1 | Tage 1-30 | Validierung (Beta-Test) | $25.000 |
| Sprint 2 | Tage 31-60 | Akquise (Public Beta) | $35.000 |
| Sprint 3 | Tage 61-90 | Monetarisierung | $20.000 |
| **Gesamt** | **90 Tage** | **Product-Market-Fit** | **$80.000** |

---

## Sprint 1: Validierung (Tage 1-30)

### Ziel
Technische Machbarkeit beweisen + Kernwertversprechen mit echten Nutzern validieren

### Team
- 1 Gründer/CEO (Product + Business Dev)
- 2 Full-Stack-Entwickler (1x Android, 1x Backend)
- 1 Teilzeit-Marketing (Community-Management)

### Deliverables

#### Woche 1-2: Development
- [ ] Android-App Skeleton (Kotlin + Jetpack Compose)
- [ ] Backend-API (FastAPI + PostgreSQL)
- [ ] PDF-Parsing-Engine (Kreuzberg Integration)
- [ ] Basic UI: Upload → Parse → Display Transactions

#### Woche 3: Testing & Beta-Prep
- [ ] Unit-Tests für Parser (>95% Coverage)
- [ ] Closed Beta APK Build
- [ ] Beta-Feedback-Formular (Google Forms)
- [ ] WhatsApp-Support-Gruppe erstellen

#### Woche 4: Beta-Launch
- [ ] 20 Beta-Nutzer rekrutieren (über LinkedIn, Twitter, KMU-Gruppen)
- [ ] Onboarding-Sessions (WhatsApp Video-Calls)
- [ ] Tägliches Monitoring: Crashes, Parsing-Fehler
- [ ] Wöchentliche User-Interviews (3-5 Nutzer)

### Success-Kriterien (Go/No-Go)
- ✅ **>80% Aktivierung** (16/20 Beta-Nutzer laden Statement hoch)
- ✅ **>95% Parsing-Erfolg** bei Beta-Statements
- ✅ **NPS >40** nach 2 Wochen Nutzung
- ❌ **No-Go:** Kern-Parsing unzuverlässig (<90%) ODER Nutzer sehen keinen Wert

### Budget-Breakdown
| Kategorie | Betrag |
|-----------|--------|
| Personal | $12.000 |
| Tech/Infrastruktur | $2.000 |
| Marketing (Beta-Rekrutierung) | $1.000 |
| Admin/Legal | $3.000 |
| Puffer (15%) | $3.750 |
| **Gesamt** | **$21.750** |

---

## Sprint 2: Akquise (Tage 31-60)

### Ziel
Erste Akquise-Kanäle testen + Wachstum auf 100+ aktive Nutzer

### Deliverables

#### Woche 5: Public Beta Launch
- [ ] App auf Google Play Store (Open Beta)
- [ ] Landing-Page mit Value-Prop (WordPress/Webflow)
- [ ] WhatsApp-Bot für Onboarding (Twilio API)

#### Woche 6-7: Paid Marketing-Tests
- [ ] Facebook Ads (KMU-Gruppen Targeting)
  - Budget: $5.000
  - Ziel: CPI <$2,00
- [ ] Google Ads (Keywords: "eTIMS compliance", "M-Pesa bookkeeping")
  - Budget: $5.000
  - Ziel: CPI <$2,50
- [ ] A/B-Test: 3 Ad-Creatives pro Kanal

#### Woche 8: Partnership-Outreach
- [ ] Women Enterprise Fund: Pitch-Deck + Meeting
- [ ] KEPSA (Kenya Private Sector Alliance): Partnerschaftsgespräch
- [ ] 2 KMU-Verbände kontaktieren (Sektoren: Retail, Food)

### Success-Kriterien (Go/No-Go)
- ✅ **100+ WAU** (Weekly Active Users)
- ✅ **CPI <$2,00** (gemischt aus Facebook/Google)
- ✅ **Install-to-Signup >30%**
- ✅ **CAC <$15** (aus bezahlten Kanälen)
- ❌ **No-Go:** CAC >$20 (nicht nachhaltig für $47 LTV)

### Budget-Breakdown
| Kategorie | Betrag |
|-----------|--------|
| Personal | $12.000 |
| Marketing/Ads | $15.000 |
| Tech/Infrastruktur | $3.000 |
| Admin | $1.000 |
| Puffer (15%) | $5.250 |
| **Gesamt** | **$36.250** |

---

## Sprint 3: Monetarisierung (Tage 61-90)

### Ziel
Zahlungsbereitschaft validieren + erste MRR generieren

### Deliverables

#### Woche 9: Payment-Integration
- [ ] Pesapal SDK Integration (Android)
- [ ] Subscription-Management (Backend)
- [ ] In-App-Purchase-Flow:
  - Freemium → Standard Upgrade
  - Standard → Premium Upgrade

#### Woche 10: Pricing-Test
- [ ] Rollout Paid-Tiers (Freemium bleibt)
- [ ] A/B-Test Pricing:
  - Variante A: Standard KSh 500/Monat
  - Variante B: Standard KSh 750/Monat (mit "Einführungsrabatt")
- [ ] Email-Kampagne an Freemium-Nutzer (Upgrade-CTA)

#### Woche 11-12: Partnership-Formalisierung
- [ ] MOU mit WEF unterzeichnen
- [ ] Co-Branding-Version für WEF-Mitglieder
- [ ] Pilot: 100 WEF-Mitglieder mit 60-Tage-Free-Trial

### Success-Kriterien (Go/No-Go)
- ✅ **>2% Free-to-Paid-Konversion**
- ✅ **MRR >$500** ($47 ARPA × ~11 zahlende Nutzer)
- ✅ **1 Partnerschafts-MOU** unterzeichnet
- ❌ **No-Go:** <1,5% Konversion (Pricing-Problem) ODER WEF-Partnership scheitert

### Budget-Breakdown
| Kategorie | Betrag |
|-----------|--------|
| Personal | $12.000 |
| Marketing | $3.000 |
| Tech/Infrastruktur | $2.000 |
| Admin/Legal | $1.000 |
| Puffer (15%) | $3.000 |
| **Gesamt** | **$21.000** |

---

## Post-Sprint 3: Entscheidungspunkt

### If Success (alle Go-Kriterien erfüllt):
→ **Weiter mit Post-MVP-Plan** (siehe ROADMAP.md)
→ Vorbereitung Series-A-Fundraising ($500K-$1M)

### If Partial Success (1-2 Kriterien verfehlt):
→ **Pivot-Sprint** (30 Tage):
- Wenn CAC zu hoch: Fokus auf organische Kanäle (Content, Referrals)
- Wenn Konversion zu niedrig: Pricing-Anpassung + Feature-Priorisierung
- Wenn Partnership scheitert: Alternative Partner (Mikrofinanz-Institutionen)

### If Failure (3+ Kriterien verfehlt):
→ **Kritische Neubewertung**:
- Product-Market-Fit nicht erreicht
- Optionen: Pivot auf B2B (Banken), Pivot auf andere Märkte (Uganda, Tanzania), oder Stop

---

## Risiko-Mitigationen (Sprint-übergreifend)

| Risiko | Wahrscheinlichkeit | Mitigation |
|--------|-------------------|------------|
| Safaricom ändert PDF-Format | Mittel | Community-Reporting-System + flexible Parser-Engine |
| KMU zahlen nicht | Mittel | eTIMS-Compliance-Botschaft stärken, Freemium-Limit senken |
| Pesapal-Integration verzögert sich | Niedrig | Backup: Mpesa-API-Fallback (manuelle Zahlungs-Verifikation) |
| WEF-Partnership scheitert | Mittel | Backup-Partner: KWFT (Kenya Women Finance Trust) |

---

## Metriken-Dashboard (Wöchentlich tracken)

### Acquisition
- Installs (Google Play)
- Install-to-Signup-Rate
- CAC (pro Kanal)

### Activation
- % Nutzer, die Statement hochladen
- Parsing-Erfolgsrate
- Time-to-First-Value (TTFV)

### Retention
- DAU / MAU
- Wöchentliche Retention (D7, D14, D30)

### Revenue
- Free-to-Paid-Konversion
- MRR
- ARPA

### Referral (optional Sprint 3)
- NPS
- Referral-Rate

---

## Team-Setup

### Rollen
- **CEO/Founder:** Product Vision, Business Dev, Partnerships
- **Android-Dev:** Native App, Offline-Sync, UI/UX
- **Backend-Dev:** FastAPI, Parsing-Engine, Database
- **Marketing (Teilzeit):** Ads-Management, Community, Content

### Tools
- **Kommunikation:** Slack
- **Projekt-Management:** Linear (oder Notion)
- **Design:** Figma
- **Code:** GitHub
- **CI/CD:** GitHub Actions
- **Analytics:** Mixpanel (für User-Tracking)
- **Support:** WhatsApp Business

---

## Nächster Schritt

Nach MVP (Tag 90) → siehe **`ROADMAP.md`** für 12-24-Monats-Plan

**Status:** ⏳ Warte auf Bestätigung vor Sprint 1-Start
