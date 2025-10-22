# M-Recon Tech Stack

**Erstellt:** 22. Oktober 2025  
**Version:** 1.0  
**Status:** In Implementation

---

## Tech-Stack-Übersicht

### MVP-Phase (Monat 0-3)
- **Mobile:** Native Android (Kotlin + Jetpack Compose)
- **Backend:** FastAPI (Python 3.11+) + PostgreSQL
- **Deployment:** Railway/Render (Backend), Google Play (Android)

### Post-MVP (Monat 4-6)
- **Web:** React PWA (TypeScript + Vite)
- **Backend:** Gleiche FastAPI-Infrastruktur
- **Deployment:** Vercel/Netlify (PWA)

---

## 📱 Android App (MVP)

### Core Framework
- **Language:** Kotlin 1.9+
- **UI Framework:** Jetpack Compose (Material 3)
- **Min SDK:** Android 10 (API 29) - deckt 85%+ kenianischen Markt
- **Target SDK:** Android 14 (API 34)

### Architecture
- **Pattern:** Clean Architecture + MVVM
- **Layers:**
  - **UI Layer:** Composables + ViewModels
  - **Domain Layer:** Use Cases + Business Logic
  - **Data Layer:** Repositories + Data Sources (Local + Remote)

### Key Libraries

#### Dependency Injection
```kotlin
// Hilt (empfohlen von Google)
implementation("com.google.dagger:hilt-android:2.48")
kapt("com.google.dagger:hilt-compiler:2.48")
implementation("androidx.hilt:hilt-navigation-compose:1.1.0")
```

#### Local Database (Offline-First)
```kotlin
// Room
implementation("androidx.room:room-runtime:2.6.0")
implementation("androidx.room:room-ktx:2.6.0")
kapt("androidx.room:room-compiler:2.6.0")
```

#### Networking
```kotlin
// Retrofit + OkHttp
implementation("com.squareup.retrofit2:retrofit:2.9.0")
implementation("com.squareup.retrofit2:converter-gson:2.9.0")
implementation("com.squareup.okhttp3:okhttp:4.12.0")
implementation("com.squareup.okhttp3:logging-interceptor:4.12.0")
```

#### Background Work
```kotlin
// WorkManager (für Sync)
implementation("androidx.work:work-runtime-ktx:2.9.0")
```

#### Image Loading
```kotlin
// Coil (Compose-native)
implementation("io.coil-kt:coil-compose:2.5.0")
```

#### Preferences
```kotlin
// DataStore (statt SharedPreferences)
implementation("androidx.datastore:datastore-preferences:1.0.0")
```

#### State Management
```kotlin
// Kotlin Coroutines + Flow
implementation("org.jetbrains.kotlinx:kotlinx-coroutines-android:1.7.3")
```

#### Testing
```kotlin
// Unit Tests
testImplementation("junit:junit:4.13.2")
testImplementation("org.mockito.kotlin:mockito-kotlin:5.1.0")
testImplementation("org.jetbrains.kotlinx:kotlinx-coroutines-test:1.7.3")

// UI Tests
androidTestImplementation("androidx.compose.ui:ui-test-junit4:1.5.4")
androidTestImplementation("androidx.test.ext:junit:1.1.5")
androidTestImplementation("androidx.test.espresso:espresso-core:3.5.1")
```

### Module Structure
```
app/
├── data/
│   ├── local/         # Room Database, DAOs
│   ├── remote/        # Retrofit APIs
│   └── repository/    # Repository Implementations
├── domain/
│   ├── model/         # Domain Models (Business Objects)
│   ├── usecase/       # Use Cases (Business Logic)
│   └── repository/    # Repository Interfaces
└── ui/
    ├── screens/       # Composable Screens
    ├── components/    # Reusable UI Components
    ├── navigation/    # Navigation Graph
    └── theme/         # Material Theme, Colors, Typography
```

---

## 🐍 Backend (FastAPI)

### Core Framework
- **Language:** Python 3.11+
- **Framework:** FastAPI 0.104+
- **ASGI Server:** Uvicorn

### Key Dependencies

#### Framework & API
```python
fastapi==0.104.1
uvicorn[standard]==0.24.0
python-multipart==0.0.6  # File uploads
pydantic==2.5.0  # Data validation
pydantic-settings==2.1.0  # Config management
```

#### Database
```python
sqlalchemy==2.0.23
asyncpg==0.29.0  # Async PostgreSQL driver
alembic==1.13.0  # Database migrations
```

#### Document Parsing
```python
# PDF Parsing (Kreuzberg oder Alternative)
pdfplumber==0.10.3  # Fallback
tabula-py==2.9.0  # Falls PDF Tables benötigt
pandas==2.1.3  # Data manipulation
```

#### Authentication & Security
```python
python-jose[cryptography]==3.3.0  # JWT
passlib[bcrypt]==1.7.4  # Password hashing
python-dotenv==1.0.0  # Environment variables
```

#### Background Tasks
```python
celery==5.3.4  # Optional: für Heavy Processing
redis==5.0.1  # Task Queue (falls Celery genutzt wird)
```

#### Testing
```python
pytest==7.4.3
pytest-asyncio==0.21.1
httpx==0.25.2  # Async HTTP Client für Tests
```

### Project Structure
```
server/
├── app/
│   ├── api/
│   │   ├── __init__.py
│   │   ├── upload.py      # File Upload Endpoints
│   │   ├── report.py      # Report Generation Endpoints
│   │   └── auth.py        # Authentication (future)
│   ├── models/
│   │   ├── __init__.py
│   │   ├── transaction.py # SQLAlchemy Models
│   │   └── user.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── pdf_service.py # PDF Parsing Logic
│   │   └── parser_service.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── transaction.py # Pydantic Schemas
│   ├── config.py          # Settings (Database URL, etc.)
│   ├── database.py        # Database Connection
│   └── main.py            # FastAPI App
├── tests/
├── alembic/               # DB Migrations
├── requirements.txt
└── .env                   # Environment Variables
```

---

## 🗄️ Database

### PostgreSQL
- **Version:** PostgreSQL 15+
- **Hosting:** 
  - **Dev:** Docker Container (local)
  - **Production:** Railway/Supabase/Render

### Schema (Initial MVP)

#### `users` Table
```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    phone_number VARCHAR(15) UNIQUE NOT NULL,
    email VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    subscription_tier VARCHAR(20) DEFAULT 'freemium'
);
```

#### `transactions` Table
```sql
CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    transaction_id VARCHAR(50) UNIQUE NOT NULL,
    date DATE NOT NULL,
    time TIME,
    description TEXT,
    amount DECIMAL(10, 2) NOT NULL,
    category VARCHAR(50),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### `uploads` Table
```sql
CREATE TABLE uploads (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    filename VARCHAR(255) NOT NULL,
    file_type VARCHAR(10) NOT NULL,
    parsing_status VARCHAR(20) DEFAULT 'pending',
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## 🌐 PWA (Post-MVP)

### Core Framework
- **Language:** TypeScript 5+
- **Build Tool:** Vite 5+
- **Framework:** React 18+
- **Styling:** Tailwind CSS 3+

### Key Libraries

```json
{
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-router-dom": "^6.20.0",
    "@tanstack/react-query": "^5.8.0",
    "axios": "^1.6.2",
    "idb": "^7.1.1",
    "papaparse": "^5.4.1",
    "pdfjs-dist": "^4.0.0"
  },
  "devDependencies": {
    "@vitejs/plugin-react": "^4.2.0",
    "vite": "^5.0.0",
    "vite-plugin-pwa": "^0.17.0",
    "tailwindcss": "^3.3.5",
    "typescript": "^5.3.2"
  }
}
```

### PWA Features
- **Service Worker:** Workbox via `vite-plugin-pwa`
- **Offline Storage:** IndexedDB via `idb`
- **Manifest:** `manifest.json` für PWA-Installation
- **Caching Strategy:**
  - API: Network-First (mit Cache-Fallback)
  - Static Assets: Cache-First

---

## 🚀 Deployment & DevOps

### CI/CD (GitHub Actions)

```yaml
name: Android CI

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up JDK 17
        uses: actions/setup-java@v3
        with:
          java-version: '17'
      - name: Build with Gradle
        run: ./gradlew build
      - name: Run Tests
        run: ./gradlew test
```

### Hosting

#### Backend
- **Option 1:** Railway (empfohlen für MVP)
  - Auto-Deploy von GitHub
  - PostgreSQL Addon
  - $5-20/Monat
- **Option 2:** Render
  - Free Tier verfügbar
  - Auto-Deploy
- **Option 3:** AWS EC2 (später für Scale)

#### Android App
- **Google Play Console** (Open Beta Track)
- **Internal Testing:** Google Play Internal Track

#### PWA
- **Option 1:** Vercel (empfohlen)
- **Option 2:** Netlify
- **Option 3:** Cloudflare Pages

---

## 🔐 Security

### Android
- **API Keys:** BuildConfig (nicht in Git)
- **Local DB:** SQLCipher für Encryption (future)
- **Network:** Certificate Pinning (future)

### Backend
- **HTTPS:** Enforced (Let's Encrypt)
- **CORS:** Whitelist-basiert
- **Rate Limiting:** FastAPI-Limiter
- **Input Validation:** Pydantic Models

---

## 📊 Analytics & Monitoring

### MVP
- **Crash Reporting:** Firebase Crashlytics (Android)
- **Analytics:** Mixpanel (User-Events)
- **Backend Monitoring:** Sentry (Errors)

### Production
- **APM:** Datadog / New Relic
- **Logs:** Grafana Loki

---

## 🧪 Testing Strategy

### Android
- **Unit Tests:** JUnit + MockK (>70% Coverage für Business Logic)
- **UI Tests:** Compose Testing + Espresso (kritische User-Flows)
- **E2E Tests:** Maestro (optional)

### Backend
- **Unit Tests:** pytest (>80% Coverage)
- **Integration Tests:** TestClient (FastAPI)
- **API Tests:** Postman/Newman (automatisiert)

---

## 📦 Dependency Management

### Android
- **Build System:** Gradle (Kotlin DSL)
- **Version Catalog:** `libs.versions.toml` für zentrale Dependency-Verwaltung

### Backend
- **Package Manager:** pip + requirements.txt
- **Virtual Env:** venv (bereits vorhanden)

### PWA
- **Package Manager:** pnpm (schneller als npm)

---

## 🔄 Migration Path: React Prototype → PWA

### Aktueller React-Prototype (`client/`)
- **Status:** ✅ Funktioniert bereits
- **Features:** PDF/CSV Upload, Preview, Categorization (UI-only)

### Nutzung für PWA (Monat 5-6)
1. **Behalten:** UI-Komponenten, Styling, Layout
2. **Hinzufügen:**
   - Service Worker (Offline-Support)
   - IndexedDB (lokale Datenhaltung)
   - API-Integration mit Backend
   - PWA-Manifest
3. **Refactoring:**
   - State Management (Zustand/TanStack Query)
   - TypeScript-Typen aus Backend generieren

---

## 📝 Next Steps

### Aktueller Setup-Status (2025-10-22)
- ✅ React-Prototype vorhanden (`client/`)
- ✅ Backend-Struktur vorhanden (`server/`)
- ✅ Python venv existiert
- ❌ Backend-Code fehlt (leer)
- ❌ Android-Projekt fehlt
- ❌ Client-Dependencies nicht installiert

### Empfohlene Setup-Reihenfolge
1. **Backend aufsetzen** (FastAPI + PostgreSQL)
   - ✅ Funktioniert für beide Clients (Android + PWA)
   - ✅ Schnellste Validierung des Parsing-Core
2. **React-Prototype vervollständigen**
   - ✅ Schnelles UI-Testing
   - ✅ Demos für Stakeholder
3. **Android-Projekt starten**
   - ✅ Echtes MVP für Beta-Launch

---

**Status:** 📋 Plan aktualisiert – bereit für Implementation
