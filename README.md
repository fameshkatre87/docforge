<div align="center">

# 📄 DocForge

### Professional PDF & Image Management SaaS Platform

[![Django](https://img.shields.io/badge/Django-4.2-092E20?style=for-the-badge&logo=django&logoColor=white)](https://djangoproject.com)
[![Vue.js](https://img.shields.io/badge/Vue.js-3.0-4FC08D?style=for-the-badge&logo=vue.js&logoColor=white)](https://vuejs.org)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-316192?style=for-the-badge&logo=postgresql&logoColor=white)](https://postgresql.org)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

**Merge PDFs • Split PDFs • Word↔PDF • Remove Pages • Resize Images • Compress Images**

[🌐 Live Demo](#) • [📖 API Docs](#api-endpoints) • [🚀 Quick Start](#quick-start)

</div>

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🔗 **Merge PDFs** | Combine multiple PDF files into one |
| ✂️ **Split PDF** | Divide PDF into separate parts (ZIP download) |
| 🗜️ **Compress PDF** | Reduce PDF size without quality loss |
| 📝 **Word → PDF** | Convert .docx files to PDF instantly |
| 📄 **PDF → Word** | Extract PDF content to editable .docx |
| 🗑️ **Remove Pages** | Delete specific pages from any PDF |
| 🖼️ **Images → PDF** | Convert multiple images to a single PDF |
| ↔️ **Resize Image** | Resize to any custom dimension |
| 🗜️ **Compress Image** | Reduce image size with quality control |
| 🔐 **JWT Auth** | Optional login — tools work without account |
| 🛡️ **Admin Panel** | User management and platform statistics |
| 📱 **Mobile Ready** | Fully responsive with hamburger navigation |

---

## 🛠️ Tech Stack

**Frontend**
- Vue 3 + Vite
- Pinia (State Management)
- Vue Router 4
- Axios (HTTP Client)
- Tailwind CSS

**Backend**
- Django 4.2
- Django REST Framework
- JWT Authentication (SimpleJWT)
- CORS Headers

**Database & Storage**
- PostgreSQL
- Pillow (Image Processing)
- PyPDF2 (PDF Processing)
- python-docx (Word Processing)
- ReportLab (PDF Generation)

---

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- Node.js 18+
- PostgreSQL 14+

### 1. Clone Repository
```bash
git clone https://github.com/fameshkatre87/docforge.git
cd docforge
```

### 2. Backend Setup
```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your database credentials

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Start server
python manage.py runserver
```

### 3. Frontend Setup
```bash
cd frontend

# Install dependencies
npm install

# Start dev server
npm run dev
```

### 4. Open Browser
```
http://localhost:5173
```

---

## 📁 Project Structure
```
docforge/
├── backend/
│   ├── config/              # Django settings, urls, wsgi
│   ├── apps/
│   │   ├── users/           # Auth, JWT, CustomUser model
│   │   ├── pdf_tools/       # PDF operations + history
│   │   └── image_tools/     # Image operations + history
│   ├── manage.py
│   └── requirements.txt
│
└── frontend/
    ├── src/
    │   ├── api/             # Axios with JWT interceptors
    │   ├── stores/          # Pinia stores (auth, files)
    │   ├── router/          # Vue Router + guards
    │   ├── components/      # AppLayout, ToolCard
    │   ├── composables/     # useTool (shared upload logic)
    │   └── views/
    │       └── tools/       # All tool pages
    ├── package.json
    └── vite.config.js
```

---

## 🔌 API Endpoints

| Method | Endpoint | Auth | Description |
|--------|----------|------|-------------|
| POST | `/api/auth/register/` | Public | Register user |
| POST | `/api/auth/login/` | Public | Login → JWT tokens |
| POST | `/api/auth/refresh/` | Public | Refresh token |
| GET | `/api/auth/me/` | Required | Get profile |
| POST | `/api/pdf/merge/` | Optional | Merge PDFs |
| POST | `/api/pdf/split/` | Optional | Split PDF → ZIP |
| POST | `/api/pdf/compress/` | Optional | Compress PDF |
| POST | `/api/pdf/from-word/` | Optional | Word → PDF |
| POST | `/api/pdf/to-word/` | Optional | PDF → Word |
| POST | `/api/pdf/remove-pages/` | Optional | Remove pages |
| POST | `/api/pdf/images-to-pdf/` | Optional | Images → PDF |
| POST | `/api/image/resize/` | Optional | Resize image |
| POST | `/api/image/compress/` | Optional | Compress image |
| GET | `/api/auth/admin/stats/` | Admin | Platform stats |
| GET | `/api/auth/admin/users/` | Admin | All users |

---

## ⚙️ Environment Variables

Create `backend/.env` file:
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
DB_NAME=docforge
DB_USER=postgres
DB_PASSWORD=yourpassword
DB_HOST=localhost
DB_PORT=5432
ALLOWED_HOSTS=localhost,127.0.0.1
CORS_ALLOWED_ORIGINS=http://localhost:5173
```


---

## 🤝 Contributing

1. Fork karo
2. Feature branch banao (`git checkout -b feature/AmazingFeature`)
3. Commit karo (`git commit -m 'Add AmazingFeature'`)
4. Push karo (`git push origin feature/AmazingFeature`)
5. Pull Request kholein

---

## 📄 License

MIT License — free to use, modify and distribute.

---

<div align="center">

Made with ❤️ using Django + Vue.js

⭐ **Star this repo if you found it helpful!**

</div>
