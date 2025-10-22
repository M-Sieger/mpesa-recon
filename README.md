# M-Recon – M-Pesa Reconciliation & Compliance App

> **Eine Mobile-First-Lösung für kenianische KMU zur Automatisierung der M-Pesa-Transaktionsabstimmung und eTIMS-Compliance**

[![Status](https://img.shields.io/badge/Status-MVP_Development-orange)]()
[![Android](https://img.shields.io/badge/Platform-Android-green)]()
[![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688)]()

---

## 🎯 Projekt-Übersicht

M-Recon löst ein kritisches Problem für 7,4 Millionen kenianische KMU: Die manuelle, zeitaufwändige Abstimmung von M-Pesa-Transaktionen und die Einhaltung der neuen eTIMS-Steuervorgaben.

### Das Problem
- **Manuelle Abstimmung:** KMU verbringen Stunden damit, M-Pesa-PDFs in Excel/Hauptbücher zu übertragen
- **eTIMS-Compliance:** KRA verlangt digitale Nachweise für ALLE Betriebsausgaben
- **Kreditbarrieren:** Fehlende formale Finanzaufzeichnungen verhindern Zugang zu Bankkrediten

### Die Lösung
- **Upload:** M-Pesa-PDF/CSV hochladen
- **Parse:** Automatische Extraktion (>98% Erfolgsrate)
- **Categorize:** Transaktionen kategorisieren (Verkäufe, Miete, Lieferanten, etc.)
- **Export:** eTIMS-konformen Bericht generieren

---

## 📂 Projekt-Struktur

```
mpesa-recon/
├── android/                    # Native Android App (Kotlin + Jetpack Compose) - GEPLANT
│   └── (wird erstellt)
├── client/                     # React PWA Prototype (für Post-MVP)
│   ├── src/
│   │   ├── components/        # UI-Komponenten
│   │   ├── utils/             # PDF/CSV Parser
│   │   └── App.tsx
│   ├── package.json
│   └── vite.config.ts
├── server/                     # FastAPI Backend
│   ├── app/
│   │   ├── api/               # API Endpoints
│   │   ├── models/            # SQLAlchemy Models
│   │   ├── services/          # Business Logic
│   │   └── main.py
│   ├── requirements.txt
│   └── venv/                  # Python Virtual Environment
├── docs/                       # Dokumentation
│   ├── MVP-PLAN.md            # 90-Tage-Roadmap
│   ├── PRODUCT-VISION.md      # Product Vision & Tech-Stack
│   ├── ROADMAP.md             # 12-24 Monate Plan
│   ├── RISK-ASSESSMENT.md     # Risikoanalyse
│   └── TECH-STACK.md          # Detaillierte Tech-Specs
└── README.md                   # Diese Datei
```

---

## 🚀 Tech-Stack

### MVP (Monat 0-3): Native Android
- **Frontend:** Kotlin + Jetpack Compose
- **Backend:** FastAPI (Python 3.11+) + PostgreSQL
- **Offline-First:** Room DB + WorkManager
- **Architecture:** Clean Architecture + MVVM

### Post-MVP (Monat 4-6): PWA
- **Frontend:** React + TypeScript + Vite
- **Backend:** Gleiche FastAPI-Infrastruktur
- **Offline:** Service Workers + IndexedDB

**Warum Native Android zuerst?**
- 80,8% Android-Marktanteil in Kenia
- Beste Offline-Performance (kritisch bei unreliable connectivity)
- Native Security für Finanz-App
- Zukünftige SMS-Parsing-Integration

→ Siehe [`docs/TECH-STACK.md`](docs/TECH-STACK.md) für Details

---

## 🛠️ Setup & Installation

### Voraussetzungen
- **Backend:** Python 3.11+, PostgreSQL 15+
- **Android:** Android Studio Hedgehog+, JDK 17+
- **PWA Prototype:** Node.js 18+, pnpm

### 1. Backend Setup (FastAPI)

```powershell
# Navigate to server directory
cd server

# Activate virtual environment
.\venv\Scripts\Activate.ps1

# Install dependencies (noch leer - wird erstellt)
pip install -r requirements.txt

# Set up environment variables
# Erstelle .env Datei mit:
# DATABASE_URL=postgresql://user:password@localhost/mpesa_recon
# SECRET_KEY=your-secret-key

# Run migrations (nach Erstellung)
alembic upgrade head

# Start server
uvicorn app.main:app --reload
```

**Backend läuft auf:** `http://localhost:8000`  
**API Docs:** `http://localhost:8000/docs`

### 2. React Prototype Setup (Optional - für UI-Testing)

```powershell
# Navigate to client directory
cd client

# Install dependencies
pnpm install

# Start dev server
pnpm dev
```

**Frontend läuft auf:** `http://localhost:5173`

### 3. Android App Setup (Noch nicht erstellt)

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

## 🧪 Testing

### Android
- **Unit Tests:** JUnit + MockK (>70% Coverage)
- **UI Tests:** Compose Testing (kritische Flows)
- **E2E Tests:** Maestro (optional)

### Backend
- **Unit Tests:** pytest (>80% Coverage)
- **API Tests:** TestClient (FastAPI)

---

## 🤝 Contributing

Aktuell in Pre-Seed-Phase. Bei Interesse an Beta-Testing oder Partnership:
- **Email:** [Kontakt einfügen]
- **GitHub Issues:** Für technische Fragen

---

## 📜 License

Proprietary – Alle Rechte vorbehalten

---

## 📞 Kontakt & Support

**Projekt:** M-Recon  
**Status:** MVP Development (Sprint 1)  
**Target Market:** 3,5 Millionen kenianische KMU  
**Next Milestone:** 20 Beta-Nutzer (Tag 30)

---

**Built with ❤️ for Kenyan SMEs**
