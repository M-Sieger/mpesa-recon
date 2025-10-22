# Product Vision – M-Recon

**Erstellt:** 21. Oktober 2025  
**Version:** 1.0  
**Projekt:** M-Recon (M-Pesa Reconciliation & Compliance)

---

## Problem Statement

Kenianische kleine und mittlere Unternehmen (KMU) stehen vor einer doppelten Herausforderung:

1. **Manuelle M-Pesa-Abstimmung:** Mit 35,82 Millionen aktiven M-Pesa-Nutzern wickeln KMU täglich hunderte Transaktionen ab. Die manuelle Übertragung dieser Transaktionen aus PDF-Kontoauszügen oder SMS-Benachrichtigungen in Geschäftsbücher oder Tabellenkalkulationen ist **extrem zeitaufwändig (mehrere Stunden pro Woche)**, **fehleranfällig** (Tippfehler, ausgelassene Transaktionen) und **nicht skalierbar**.

2. **eTIMS-Compliance-Druck:** Das neue Mandat der Kenya Revenue Authority (KRA) verlangt, dass **alle** Unternehmen – einschließlich nicht-MwSt-registrierter und informeller Betriebe – ihre Betriebsausgaben mit eTIMS-konformen Rechnungen belegen müssen, um sie steuerlich geltend zu machen. Ohne digitale Buchführung drohen höhere Steuern und Bußgelder.

**Konsequenzen:**
- Ungenaue Finanzaufzeichnungen behindern strategische Entscheidungen
- Fehlende formale Aufzeichnungen verhindern Zugang zu Bankkrediten
- Manuelle Abstimmung bindet wertvolle Zeit, die in das Geschäftswachstum investiert werden könnte
- Nicht-Compliance mit eTIMS führt zu direkten finanziellen Verlusten (höhere Steuerlast)

---

## Target Audience

### Primäre Zielgruppe (MVP)
**Segment:** Kenianische KMU (KKMU – Kleinst-, Klein- und Mittelunternehmen)

**Charakteristika:**
- **Größe:** 1-10 Mitarbeiter
- **Sektor:** Einzelhandel, Dienstleistungen, Handwerk, Food & Beverage, Handwerker
- **Transaktionsvolumen:** 50-500 M-Pesa-Transaktionen pro Monat
- **Digitale Kompetenz:** Mittel (nutzen Smartphones, WhatsApp, M-Pesa täglich)
- **Geographie:** Städtisch und stadtnahe Gebiete (Nairobi, Mombasa, Kisumu, Nakuru)
- **Lizenzstatus:** Mix aus lizenzierten (1,56 Mio.) und nicht-lizenzierten (5,85 Mio.) Unternehmen

**Nutzungskontext:**
- **Wo:** Im Laden/Büro, unterwegs (bei Lieferanten/Kunden)
- **Wann:** Abends nach Geschäftsschluss, Wochenende (wenn Zeit für Buchhaltung ist)
- **Gerät:** Android-Smartphone (80,8% Smartphone-Penetration, Android-Dominanz)
- **Konnektivität:** Oft unzuverlässig oder kostspielig → **Offline-First zwingend**

### Sekundäre Zielgruppe (Post-MVP)
**Frauengeführte KMU (40% des Marktes):**
- Überproportional stark von fehlenden formalisierten Finanzaufzeichnungen betroffen
- Benötigen saubere Aufzeichnungen für Zugang zu Mikrokrediten (z.B. Women Enterprise Fund)
- Konzentriert in Sektoren mit hohem Transaktionsvolumen (Einzelhandel, Food)

**Kooperationspartner:**
- Women Enterprise Fund (WEF) – zur Unterstützung von Kreditvergabe-Prozessen
- KMU-Verbände und Genossenschaften
- Mikrofinanzinstitutionen

---

## Vision Statement

**M-Recon macht M-Pesa-Transaktionen für kenianische KMU sofort verwertbar, indem es mühsame manuelle Abstimmung automatisiert und eTIMS-Compliance mit einem Klick ermöglicht – damit Unternehmer Zeit und Geld sparen und den Zugang zu Krediten erhalten.**

**In 3 Jahren:** Die führende Finanz-Compliance- und Abstimmungslösung für 100.000+ KMU in Ostafrika, die als vertrauenswürdiger Partner für Banken, Mikrofinanzinstitutionen und Steuerbehörden gilt.

---

## MVP User Stories (Must-Have)

### User Story 1: M-Pesa-Kontoauszug hochladen und parsen
**Als** KMU-Besitzer  
**möchte ich** meinen M-Pesa-PDF-Kontoauszug oder CSV-Export mit einem Klick hochladen  
**damit** alle Transaktionen automatisch extrahiert und in einer übersichtlichen Tabelle angezeigt werden.

**Acceptance Criteria:**
- [ ] Upload-Interface für PDF- und CSV-Dateien (max. 10 MB)
- [ ] Parsing-Erfolgsrate >98% für Standard-M-Pesa-Kontoauszüge
- [ ] Extrahierte Felder: Datum, Uhrzeit, Transaktions-ID, Details (Zahler/Empfänger), Betrag
- [ ] Fehlermeldung bei unbekanntem Format mit Support-Kontakt
- [ ] Offline-Upload möglich (Sync bei nächster Online-Verbindung)

### User Story 2: Transaktionen kategorisieren
**Als** KMU-Besitzer  
**möchte ich** jede Transaktion einer Kategorie zuordnen (Verkäufe, Miete, Lieferanten, Gehälter, etc.)  
**damit** ich sehe, wofür mein Geld ausgegeben wird und meine Steuererklärung vorbereiten kann.

**Acceptance Criteria:**
- [ ] Vordefinierte Kategorien: Verkäufe, Einkäufe, Miete, Gehälter, Transport, Steuern, Sonstiges
- [ ] Bulk-Kategorisierung: Alle Transaktionen von "Safaricom Airtime" → "Betriebsausgaben"
- [ ] Eigene Kategorien erstellen und speichern
- [ ] Smart-Suggestions: App schlägt Kategorien basierend auf Transaktionsdetails vor
- [ ] Notizen pro Transaktion hinzufügen (z.B. "Mehl für Bäckerei")

### User Story 3: eTIMS-konformen Bericht exportieren
**Als** KMU-Besitzer  
**möchte ich** einen übersichtlichen Bericht meiner kategorisierten Ausgaben als CSV oder PDF exportieren  
**damit** ich diese Daten für meine eTIMS-Einreichung bei der KRA nutzen kann.

**Acceptance Criteria:**
- [ ] Export als CSV (für manuelle eTIMS-Eingabe)
- [ ] Export als PDF-Zusammenfassung (Gesamt-Einnahmen, Gesamt-Ausgaben pro Kategorie)
- [ ] Zeitraum-Filter: Monat, Quartal, Jahr, Custom-Range
- [ ] Offline-Funktion: Report wird lokal generiert, kein Internet erforderlich
- [ ] Report enthält KRA-konforme Formatierung (Hinweis auf eTIMS-Anforderungen)

---

## Success Metrics (MVP – erste 90 Tage)

### Validierungsphase (Sprint 1: Tag 1-30)
- [ ] **20 Beta-Nutzer** rekrutiert
- [ ] **>80% Aktivierungsrate** (Beta-Nutzer laden mind. 1 Statement hoch)
- [ ] **>95% Parsing-Erfolgsrate** bei Beta-User-Statements
- [ ] **Net Promoter Score (NPS) >40**

### Akquisitionsphase (Sprint 2: Tag 31-60)
- [ ] **100+ wöchentlich aktive Nutzer (WAU)**
- [ ] **Cost Per Install (CPI) <$2,00**
- [ ] **Install-to-Signup-Rate >30%**
- [ ] **Customer Acquisition Cost (CAC) <$15** (aus bezahlten Kanälen)

### Monetarisierungsphase (Sprint 3: Tag 61-90)
- [ ] **>2% Free-to-Paid-Konversion**
- [ ] **Monatlich wiederkehrender Umsatz (MRR) >$500**
- [ ] **1 Partnerschafts-MOU unterzeichnet** (WEF oder KMU-Verband)

### Geschäftsziele (Jahr 1)
- [ ] **17.500 zahlende Nutzer** (0,5% des SAM von 3,5 Mio. KMU)
- [ ] **LTV:CAC-Ratio von 3,5:1**
- [ ] **Churn-Rate <30% jährlich**

---

## Tech-Stack (Vorgeschlagen)

### Frontend (Mobile)
- **Plattform (MVP):** Native Android App (Kotlin + Jetpack Compose)
- **Architecture:** Clean Architecture mit MVVM
- **Key Libraries:**
  - **Jetpack Compose:** Moderne deklarative UI
  - **Room:** Lokale SQLite-Datenbank
  - **WorkManager:** Background-Synchronisation
  - **Hilt:** Dependency Injection
  - **Retrofit:** API-Calls zum Backend
  - **Coil:** Image Loading
  - **DataStore:** App-Preferences
- **Begründung:** 
  - Android dominiert kenianischen Markt (80,8% Penetration)
  - Native Performance für finanzielle Anwendungen (Sicherheit, Reaktionsfähigkeit)
  - Beste Offline-Fähigkeiten (Room DB + WorkManager)
  - Zukunftssichere SMS-Parsing-Integration (READ_SMS-Permission)
  - Material 3 Design für moderne, intuitive UX

### Frontend (Post-MVP)
- **Plattform (6-12 Monate):** Progressive Web App (PWA)
- **Tech-Stack:** React + Vite + TypeScript
- **Begründung:**
  - Kosteneffiziente Erweiterung auf iOS & Desktop ohne separate native App
  - Service Worker für Offline-Funktionalität
  - Einfache Updates ohne App-Store-Review
- **Note:** Aktueller React-Prototype dient als Proof-of-Concept für PWA-Phase

### Backend
- **Framework:** Python 3.11+ mit FastAPI
- **Begründung:**
  - Python ist ideal für Document-Parsing (Kreuzberg, Unstructured Libs)
  - FastAPI: Modern, schnell, automatische OpenAPI-Docs, async-Support
  - Große Community für ML-Features (zukünftige Smart-Categorization)

### Document Parsing
- **Library:** Kreuzberg / Unstructured (Python)
- **Erfolgsrate:** >97-100% laut Benchmarks für strukturierte PDF-Dokumente
- **Fallback:** Manuelle Korrektur-UI für Edge-Cases (<2%)

### Datenbank
- **Lokal (Mobile):** SQLite via Room (Android)
- **Backend:** PostgreSQL 16
- **Begründung:**
  - SQLite: Leichtgewichtig, perfekt für Offline-First
  - PostgreSQL: Robust, JSONB-Support für flexible Schemas, bewährt für SaaS

### State Management (Android)
- **Lösung:** Jetpack ViewModel + StateFlow + Compose State
- **Architecture Pattern:** MVVM (Model-View-ViewModel)
- **Data Flow:**
  - **UI Layer:** Composables observieren ViewModels via StateFlow
  - **Domain Layer:** Use Cases orchestrieren Business-Logik
  - **Data Layer:** Repositories abstrahieren Datenquellen (Local Room DB + Remote API)
- **Begründung:**
  - Native Android-Solution, kein zusätzliches Framework nötig
  - Lifecycle-aware, verhindert Memory-Leaks
  - Reaktives Pattern mit Kotlin-Coroutines
  - Klare Separation of Concerns (Testability)

### Testing
- **Unit-Tests:** JUnit 5 (Android), pytest (Backend)
- **UI-Tests:** Espresso (Android), Maestro (Cross-Platform E2E als Alternative)
- **Backend-Tests:** pytest + httpx (FastAPI-Testing-Client)
- **Coverage-Ziel:** >70% für kritische Pfade (Parsing, Kategorisierung, Export)

### CI/CD
- **Platform:** GitHub Actions
- **Pipeline:**
  - **On Push:** Lint (ktlint/flake8), Unit-Tests, Type-Check
  - **On PR:** Integration-Tests, E2E-Tests (kritische User-Flows)
  - **On Merge to main:** Automatisches Deployment zu Staging (Railway/Render für Backend, Google Play Internal Track für Android)
  - **On Git Tag (v1.x.x):** Production-Deployment (manuell getriggert)

### Authentication & Security
- **Auth:** JWT-basiert (Access-Token 15 Min + Refresh-Token 7 Tage in HttpOnly-Cookie)
- **Verschlüsselung:** SQLCipher für lokale Datenbank-Verschlüsselung (Android)
- **API-Security:** Rate-Limiting (FastAPI-Limiter), Input-Validation (Pydantic)

### Payment Integration (Post-MVP Sprint 3)
- **PSP-Partner:** Pesapal
- **Begründung:**
  - Etablierte API-Dokumentation
  - Fokus auf KMU-Markt (8.000+ Händler)
  - Unterstützt M-Pesa, Kreditkarten, Bank-Transfers
  - Niedrigere Transaktionskosten als Alternativen

---

## Non-Functional Requirements

### Performance
- **Mobile App:**
  - App-Start: <2s (Cold Start), <0,5s (Hot Start)
  - PDF-Parsing: <5s für 100-Transaktionen-Statement
  - Export-Generierung: <3s für 1000 Transaktionen
- **Backend API:**
  - Response Time: <200ms (p95) für Standard-Requests
  - Parsing-Endpoint: <10s für 10MB PDF

### Security
- **Authentifizierung:** JWT mit automatischem Token-Refresh
- **Datenverschlüsselung:**
  - In-Transit: HTTPS/TLS 1.3
  - At-Rest: SQLCipher (Mobile), PostgreSQL Encryption (Backend)
- **Input-Validation:** Alle API-Inputs via Pydantic-Models validiert
- **File-Upload-Security:** 
  - Max. File-Size: 10 MB
  - Allowed Formats: PDF, CSV (MIME-Type-Validation)
  - Virus-Scanning (ClamAV) vor Parsing (Post-MVP)

### Accessibility
- **Standard:** WCAG 2.2 AA (Web-Komponenten)
- **Mobile:** 
  - TalkBack-Kompatibilität (Android Screen Reader)
  - Mindest-Touch-Target-Größe: 48x48 dp
  - Farbkontrast: ≥4,5:1 für Text
  - Keyboard-Navigation (für externe Keyboards)

### Browser-/OS-Support
- **Android:** Android 10+ (API 29+) – deckt 85%+ des kenianischen Marktes ab
- **PWA (Post-MVP):** 
  - Chrome/Firefox/Safari/Edge (letzte 2 Versionen)
  - iOS 15.4+ (für PWA-Installation)

### Offline-Funktionalität
- **Critical:** App MUSS offline voll funktionsfähig sein (kein Internet = kein Dealbreaker)
- **Lokal gespeichert:** Letzte 180 Tage Transaktionsdaten (ca. 1.000-5.000 Transaktionen)
- **Sync-Strategie:**
  - Pull-Sync beim App-Start (wenn Online)
  - Push-Sync mit exponentieller Backoff-Strategie bei fehlgeschlagenen Versuchen
  - Konfliktlösung: "Last-Write-Wins" (basierend auf Timestamp)
- **Speicherlimit:** Max. 50 MB lokale Datenbank (automatische Bereinigung älterer Daten)

### Reliability & Availability
- **Backend-Uptime:** >99,5% (max. 3,65 Stunden Downtime/Monat)
- **Error-Handling:**
  - Graceful Degradation bei Backend-Ausfall (App zeigt lokale Daten)
  - Retry-Mechanismus für kritische API-Calls (z.B. Statement-Upload)
  - User-Friendly Error-Messages (keine Tech-Jargon)

---

## Out-of-Scope (Nicht-MVP)

### Für MVP NICHT enthalten (aber Post-MVP-Roadmap):
- [ ] **Automatische eTIMS-API-Integration:** MVP nutzt manuellen Export → Auto-Submission kommt in Phase 2
- [ ] **SMS-Parsing:** Automatisches Parsen von M-Pesa-SMS-Benachrichtigungen (erfordert READ_SMS-Permission + komplexere UX)
- [ ] **Multi-User-Zugang:** MVP ist Single-User pro Konto (Team-Features für Enterprise-Tier später)
- [ ] **Bankkonto-Integration:** Nur M-Pesa im MVP (keine Bank-Statement-Integration)
- [ ] **Erweiterte Analysen:** KI-basierte Ausgaben-Prognosen, Cashflow-Forecasting (erfordert Datenbasis)
- [ ] **Multi-Currency-Support:** MVP ist KSh-only (USD/EUR-Support für internationale Transaktionen später)
- [ ] **iOS Native App:** PWA deckt iOS ab (native App nur bei signifikantem iOS-Marktanteil)
- [ ] **Integration mit Buchhaltungssoftware:** Keine QuickBooks/Xero-Integration im MVP (API-Endpunkte für Export-Formate später)

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
1. **Digitale Werbung:** Facebook/Instagram (KMU-Gruppen), Google Ads (Keyword: "eTIMS compliance")
2. **WhatsApp-Bot:** Onboarding + Support (niedrige Hemmschwelle, hohe Verbreitung in Kenia)
3. **KMU-Verbände:** Partnerschaften für Co-Marketing (Women Enterprise Fund, KEPSA)
4. **Content-Marketing:** Blog-Posts zu "eTIMS-Compliance für KMU", YouTube-Tutorials (Swahili/Englisch)

### Zielgruppen-spezifisch:
- **Frauengeführte KMU:** Partnerschaft mit Women Enterprise Fund (WEF) für Pilotprogramm
- **Sektoren:** Einzelhandel (Duka), Food (Hotels/Restaurants), Dienstleistungen (Salons, Autowerkstätten)

---

## Architecture Decision Records (ADRs) – Preview

### ADR-001: Native Android statt Cross-Platform (Flutter/React Native)
**Decision:** Native Android mit Kotlin + Jetpack Compose  
**Status:** ✅ APPROVED  
**Date:** 2025-10-22

**Context:**
- Kenianischer Markt ist 80,8% Android-dominiert
- Offline-First ist kritische Anforderung (unreliable connectivity)
- Finanz-App benötigt höchste Sicherheit und Performance
- Zukünftige SMS-Parsing-Integration geplant

**Reason:**  
- **Beste Offline-Performance:** Room DB mit native integration, WorkManager für robustes Background-Sync
- **Zukunftssichere SMS-Parsing-Fähigkeit:** READ_SMS Android-Permission nur in nativen Apps zuverlässig
- **Finanz-Apps benötigen maximale Sicherheit & Reaktionsfähigkeit:** Direkter Zugriff auf Hardware-Security (Keystore)
- **Schnellere Time-to-Market für MVP:** Fokus auf eine Plattform = schnellere Iteration
- **Kleinere APK-Größe:** Kritisch für Nutzer mit begrenztem Speicher/Datenvolumen

**Alternatives Considered:**
- **Flutter:** 
  - ❌ Cross-Platform-Vorteil nicht relevant (iOS nur 15% Markt)
  - ❌ Größere APK-Größe (~40MB vs ~15MB native)
  - ❌ Schlechtere Offline-Performance mit sqflite
  - ❌ SMS-Permissions komplexer zu handhaben
- **React Native:** 
  - ❌ Weniger native Integrations
  - ❌ Performance-Bottlenecks bei großen lokalen Datenbanken
  - ❌ Bridge-Overhead für häufige DB-Operationen

**Consequences:**
- ✅ iOS-Nutzer werden über PWA bedient (Post-MVP)
- ✅ Aktueller React-Prototype wird zu PWA-Codebase
- ✅ Entwickler benötigen Kotlin + Android-Expertise

### ADR-002: FastAPI statt Django/Flask für Backend
**Decision:** FastAPI mit Python 3.11+  
**Reason:**
- Modern async-Support (wichtig für concurrency bei Document-Parsing)
- Automatische OpenAPI-Dokumentation (erleichtert API-Entwicklung & Testing)
- Pydantic-Integration für Type-Safe-Validation (reduziert Bugs)
- Beste Python-Library-Support für Document-Parsing (Kreuzberg, Unstructured)

**Alternatives Considered:**
- Django → Zu viel Boilerplate für MVP, monolithischer Ansatz
- Flask → Weniger moderne Features, manuelle OpenAPI-Integration nötig

### ADR-003: File-Upload statt direkter M-Pesa-API-Integration
**Decision:** User lädt PDF/CSV hoch (keine Live-API-Anbindung zu Safaricom)  
**Reason:**
- **Machbarkeit:** Keine Safaricom-API-Lizenz nötig (monatelanger Prozess, hohe Kosten)
- **Time-to-Market:** Schnellerer MVP-Launch (keine Verhandlungen mit Safaricom)
- **User-Mental-Model:** KMU erhalten bereits monatliche Statements per E-Mail → bekannter Workflow
- **Datenschutz:** User hat volle Kontrolle über Daten (kein automatischer Bank-Zugriff)

**Alternatives Considered:**
- Direkte API-Integration → Nicht realistisch für Seed-Phase-Startup

---

## Next Steps: Phase 2 (Architecture Design)

Nach Bestätigung dieser Product Vision geht es weiter mit:

1. **Detaillierte Architektur-Dokumentation** (`/docs/ARCHITECTURE.md`)
2. **Ordnerstruktur-Design** (Feature-based vs. Layer-based)
3. **API-Design** (Backend-Endpoints, Request/Response-Schemas)
4. **Data-Flow-Diagramme** (User-Action → Component → API → DB → Sync)
5. **Testing-Strategie** (Unit/Integration/E2E, Coverage-Ziele)
6. **CI/CD-Pipeline-Details** (GitHub Actions Workflows)

---

## Review & Approval

**Status:** ⏳ Warte auf User-Bestätigung

**Fragen für Review:**
1. ✅ **Tech-Stack OK?** (Native Android MVP, FastAPI Backend, PostgreSQL)
2. ✅ **MVP-User-Stories decken Kern-Problem?** (Upload → Kategorisieren → eTIMS-Export)
3. ✅ **Offline-First-Ansatz akzeptabel?** (Room DB + Sync-Manager)
4. ✅ **Preis-Modell realistisch?** (Freemium + KSh 500/Monat Standard-Tier)
5. ✅ **Out-of-Scope-Entscheidungen sinnvoll?** (Keine SMS-Parsing, keine iOS-Native im MVP)

**Approval:** Bitte bestätige mit "✅ Product Vision approved – weiter mit Phase 2 (Architecture)" oder gib Feedback zu Anpassungen.

---

**Version History:**
- v1.0 (21.10.2025) – Initial Product Vision basierend auf Due-Diligence-Analyse
