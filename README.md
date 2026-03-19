# DocForge — PDF & Image Management SaaS

Full-stack web app: **Vue 3 + Django 4 + PostgreSQL**

---

## Quick Start

### 1. PostgreSQL — Create Database
```sql
CREATE DATABASE docforge;
```

### 2. Backend Setup
```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env .env.local              # Edit DB_PASSWORD and SECRET_KEY
# Edit .env with your PostgreSQL credentials

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create admin superuser
python manage.py createsuperuser

# Start server (runs on http://localhost:8000)
python manage.py runserver
```

### 3. Frontend Setup
```bash
cd frontend

# Install dependencies
npm install

# Start dev server (runs on http://localhost:5173)
npm run dev
```

### 4. Open in Browser
Visit: http://localhost:5173

---

## Project Structure

```
docforge/
├── backend/
│   ├── config/            # Django settings, urls, wsgi
│   ├── apps/
│   │   ├── users/         # Auth, JWT, user model, admin
│   │   ├── pdf_tools/     # Merge, split, compress, convert
│   │   └── image_tools/   # Resize, compress
│   ├── manage.py
│   ├── requirements.txt
│   └── .env
│
└── frontend/
    ├── src/
    │   ├── api/           # Axios instance with JWT interceptors
    │   ├── stores/        # Pinia: auth, files
    │   ├── router/        # Vue Router with auth guards
    │   ├── components/    # AppLayout, ToolCard
    │   ├── composables/   # useTool (shared upload logic)
    │   └── views/         # Landing, Login, Register, Dashboard,
    │       └── tools/     # All 7 tool pages
    ├── package.json
    └── vite.config.js     # Proxies /api → localhost:8000
```

---

## API Endpoints

| Method | Endpoint               | Auth     | Description          |
|--------|------------------------|----------|----------------------|
| POST   | /api/auth/register/    | Public   | Register user        |
| POST   | /api/auth/login/       | Public   | Login → JWT tokens   |
| POST   | /api/auth/refresh/     | Public   | Refresh access token |
| GET    | /api/auth/me/          | Required | Get profile          |
| GET    | /api/auth/admin/stats/ | Admin    | Platform stats       |
| GET    | /api/auth/admin/users/ | Admin    | All users            |
| POST   | /api/pdf/merge/        | Required | Merge PDFs           |
| POST   | /api/pdf/split/        | Required | Split PDF → ZIP      |
| POST   | /api/pdf/compress/     | Required | Compress PDF         |
| POST   | /api/pdf/from-word/    | Required | Word → PDF           |
| POST   | /api/pdf/to-word/      | Required | PDF → Word           |
| GET    | /api/pdf/history/      | Required | User's PDF history   |
| POST   | /api/image/resize/     | Required | Resize image         |
| POST   | /api/image/compress/   | Required | Compress image       |
| GET    | /api/image/history/    | Required | User's image history |

---

## Default .env Values (edit before production)
```
SECRET_KEY=django-insecure-docforge-change-this-in-production-xyz123
DEBUG=True
DB_NAME=docforge
DB_USER=postgres
DB_PASSWORD=yourpassword   ← CHANGE THIS
DB_HOST=localhost
DB_PORT=5432
```
