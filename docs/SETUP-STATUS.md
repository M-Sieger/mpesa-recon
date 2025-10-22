# Setup Status – M-Recon

**Last Updated:** 22. Oktober 2025  
**Current Phase:** Pre-Sprint 1 Setup

---

## 📊 Setup-Übersicht

| Component | Status | Progress | Notes |
|-----------|--------|----------|-------|
| **Backend (FastAPI)** | 🔴 Not Started | 0% | Ordnerstruktur vorhanden, Code fehlt |
| **Android App** | 🔴 Not Started | 0% | Projekt muss erstellt werden |
| **React Prototype** | 🟡 Partial | 60% | UI vorhanden, Dependencies fehlen, Backend-Integration fehlt |
| **Database** | 🔴 Not Started | 0% | PostgreSQL muss aufgesetzt werden |
| **Documentation** | 🟢 Complete | 95% | Alle Pläne dokumentiert |

---

## 🎯 Aktuelle Prioritäten

### Priorität 1: Backend (FastAPI)
**Warum zuerst?**
- Funktioniert für BEIDE Clients (Android + PWA)
- Kern-Feature: PDF-Parsing kann isoliert getestet werden
- Schnellste Validierung der technischen Machbarkeit

**Was zu tun ist:**
1. ✅ `requirements.txt` erstellen mit Dependencies
2. ✅ FastAPI Server-Code in `server/app/main.py`
3. ✅ PostgreSQL lokal oder via Docker aufsetzen
4. ✅ PDF-Parsing-Service implementieren
5. ✅ Upload-Endpoint erstellen
6. ✅ Basic Tests schreiben

**Geschätzter Aufwand:** 2-3 Tage

---

### Priorität 2: React Prototype vervollständigen
**Warum?**
- Schnelles UI/UX-Testing
- Demos für Stakeholder
- Vorbereitung für PWA-Phase (Monat 5-6)

**Was zu tun ist:**
1. ✅ Dependencies installieren (`pnpm install`)
2. ✅ Backend-API-Integration
3. ✅ State Management verbessern
4. ✅ Kategorisierung-UI implementieren
5. ✅ Export-Funktion (CSV/PDF)

**Geschätzter Aufwand:** 1-2 Tage (parallel zu Backend)

---

### Priorität 3: Android App Setup
**Warum später?**
- Benötigt Backend-API zum Testen
- Größerer Zeitaufwand
- Echtes MVP für Beta-Launch (Tag 30)

**Was zu tun ist:**
1. ✅ Android Studio Projekt erstellen
2. ✅ Multi-Module-Struktur aufsetzen
3. ✅ Hilt + Room + Retrofit konfigurieren
4. ✅ Basic UI mit Jetpack Compose
5. ✅ API-Integration testen

**Geschätzter Aufwand:** 5-7 Tage

---

## 📋 Detaillierter Status

### Backend (FastAPI)

#### ✅ Erledigt
- [x] Ordnerstruktur erstellt (`server/app/`)
- [x] Python Virtual Environment (venv)
- [x] Unterordner: `api/`, `models/`, `services/`

#### ❌ Ausstehend
- [ ] `requirements.txt` mit Dependencies
- [ ] `app/main.py` - FastAPI App-Initialization
- [ ] `app/config.py` - Settings (Database URL, Secret Key)
- [ ] `app/database.py` - Database Connection
- [ ] `app/models/transaction.py` - SQLAlchemy Models
- [ ] `app/schemas/transaction.py` - Pydantic Schemas
- [ ] `app/services/pdf_service.py` - PDF Parsing Logic
- [ ] `app/api/upload.py` - Upload Endpoint
- [ ] `app/api/report.py` - Report Generation
- [ ] PostgreSQL Setup (lokal oder Docker)
- [ ] Alembic Migrations
- [ ] Unit Tests (pytest)

**Dependencies benötigt:**
```txt
fastapi==0.104.1
uvicorn[standard]==0.24.0
sqlalchemy==2.0.23
asyncpg==0.29.0
alembic==1.13.0
pdfplumber==0.10.3
pandas==2.1.3
python-multipart==0.0.6
pydantic==2.5.0
pydantic-settings==2.1.0
python-dotenv==1.0.0
pytest==7.4.3
pytest-asyncio==0.21.1
httpx==0.25.2
```

---

### React Prototype

#### ✅ Erledigt
- [x] Vite + React + TypeScript Setup
- [x] UI-Komponenten:
  - [x] `Header.tsx`
  - [x] `UploadSection.tsx`
  - [x] `FileInfo.tsx`
  - [x] `PreviewTable.tsx`
  - [x] `AnalyzeButton.tsx`
- [x] PDF-Parser (pdfjs-dist) - Client-Side
- [x] CSV-Parser (papaparse)
- [x] Passwortgeschützte PDFs unterstützt
- [x] `package.json` mit Dependencies

#### ❌ Ausstehend
- [ ] `node_modules` installieren (`pnpm install`)
- [ ] Backend-API-Integration (Upload zu FastAPI)
- [ ] Kategorisierung-UI
- [ ] Export-Funktion (CSV/PDF Download)
- [ ] State Management (TanStack Query oder Zustand)
- [ ] Error Handling verbessern
- [ ] Loading States

**Dependencies vorhanden:**
```json
{
  "dependencies": {
    "papaparse": "^5.5.3",
    "pdfjs-dist": "^5.3.93",
    "react": "^19.1.0",
    "react-dom": "^19.1.0"
  }
}
```

**Dependencies noch benötigt:**
```json
{
  "dependencies": {
    "axios": "^1.6.2",
    "@tanstack/react-query": "^5.8.0"
  }
}
```

---

### Android App

#### ✅ Erledigt
- Nichts (noch nicht gestartet)

#### ❌ Ausstehend
- [ ] **Android Studio Projekt** erstellen
  - [ ] Kotlin + Jetpack Compose Template
  - [ ] Min SDK 29 (Android 10)
  - [ ] Target SDK 34 (Android 14)
- [ ] **Multi-Module Setup**
  - [ ] `:app` - Main App Module
  - [ ] `:data` - Data Layer
  - [ ] `:domain` - Business Logic
  - [ ] `:ui` - UI Components
- [ ] **Dependencies** (siehe `docs/TECH-STACK.md`)
  - [ ] Hilt (Dependency Injection)
  - [ ] Room (Local Database)
  - [ ] Retrofit (Networking)
  - [ ] WorkManager (Background Sync)
  - [ ] Jetpack Compose (UI)
- [ ] **Basic Screens**
  - [ ] Splash Screen
  - [ ] Upload Screen
  - [ ] Transaction List
  - [ ] Settings Screen
- [ ] **Navigation** (Compose Navigation)
- [ ] **Theme** (Material 3)

---

### Database (PostgreSQL)

#### ✅ Erledigt
- Nichts

#### ❌ Ausstehend
- [ ] **Lokal Setup** (eine der Optionen):
  - **Option 1:** PostgreSQL direkt auf WSL installieren
  - **Option 2:** Docker Container (empfohlen)
  - **Option 3:** Cloud (Supabase Free Tier, Railway)
- [ ] **Schema erstellen**
  - [ ] `users` Table
  - [ ] `transactions` Table
  - [ ] `uploads` Table
- [ ] **Alembic Migrations** Setup
- [ ] **Test-Daten** einfügen

**Empfohlenes Setup (Docker):**
```powershell
# In server/ Verzeichnis
docker run --name mpesa-db -e POSTGRES_PASSWORD=dev -e POSTGRES_DB=mpesa_recon -p 5432:5432 -d postgres:15
```

**Connection String:**
```
DATABASE_URL=postgresql://postgres:dev@localhost:5432/mpesa_recon
```

---

## 🚀 Empfohlene Setup-Reihenfolge

### Phase 1: Backend Foundation (Tag 1-2)
```
1. PostgreSQL Setup (Docker)
2. requirements.txt erstellen
3. FastAPI Server-Code
4. PDF-Parsing-Service
5. Upload-Endpoint
6. Testen mit Postman/curl
```

### Phase 2: React Prototype (Tag 2-3, parallel)
```
1. pnpm install
2. Backend-API-Integration
3. Kategorisierung-UI
4. Export-Funktion
5. End-to-End-Test (Upload → Parse → Export)
```

### Phase 3: Android App (Tag 4-7)
```
1. Android Studio Projekt
2. Multi-Module Setup
3. Hilt + Room + Retrofit
4. Basic UI (Upload + List)
5. API-Integration
6. Offline-Sync testen
```

---

## 📝 Nächste konkrete Schritte

### JETZT (nächste 30 Minuten)
1. ✅ Backend `requirements.txt` erstellen
2. ✅ PostgreSQL via Docker starten
3. ✅ FastAPI `main.py` mit Hello-World-Endpoint

### HEUTE (nächste 2-3 Stunden)
1. ✅ PDF-Parsing-Service implementieren
2. ✅ Upload-Endpoint erstellen
3. ✅ Testen mit Sample-PDF

### MORGEN
1. ✅ React Client: Dependencies installieren
2. ✅ API-Integration im React-Client
3. ✅ End-to-End-Test: Upload von React → FastAPI

---

## 🎯 Definition of Done (Sprint 1 - Woche 1-2)

### Backend
- [x] FastAPI Server läuft auf localhost:8000
- [x] `/upload` Endpoint funktioniert
- [x] PDF-Parsing >95% Erfolgsrate (getestet mit 10 Sample-PDFs)
- [x] PostgreSQL speichert Transaktionen
- [x] API Docs unter /docs verfügbar

### React Prototype
- [x] Upload-Funktion → Backend
- [x] Transaktionen werden angezeigt
- [x] Kategorisierung möglich
- [x] CSV-Export funktioniert

### Android App
- [x] Projekt erstellt und konfiguriert
- [x] Login-Screen (Basic)
- [x] Upload-Screen funktioniert
- [x] API-Call zu Backend erfolgreich
- [x] Room DB speichert Daten lokal

---

## 🔧 Tools & Umgebung

### Benötigte Software
- [x] Python 3.11+ (vorhanden)
- [x] Node.js 18+ (für React)
- [x] pnpm (Package Manager)
- [ ] PostgreSQL 15+ (oder Docker)
- [ ] Android Studio Hedgehog+
- [ ] JDK 17+

### Entwicklungsumgebung
- **OS:** Windows (mit WSL Ubuntu 24.04)
- **Editor:** VS Code
- **Terminal:** PowerShell
- **Git:** vorhanden

---

## 📊 Progress Tracking

### Weekly Goals (Woche 1)
- [ ] Backend: CRUD-Endpoints für Transactions
- [ ] Backend: PDF-Parsing mit 95%+ Erfolg
- [ ] React: Vollständige UI-Flow
- [ ] Android: Projekt-Setup + Basic UI

### Weekly Goals (Woche 2)
- [ ] Backend: Authentication (JWT)
- [ ] Backend: Unit Tests (>80% Coverage)
- [ ] Android: Offline-Sync implementiert
- [ ] Android: Material 3 Theme

---

**Status:** 🟡 Setup in Progress  
**Next Update:** Nach Backend-Setup (in 1-2 Tagen)
