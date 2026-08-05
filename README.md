# 🏫 CampusAlert

A web-based **Campus Alert Management System** built with **Django** and **MongoDB**. It allows students to view alerts/notifications and admins to create and manage alerts for the campus community.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Django](https://img.shields.io/badge/Django-3.1.12-green)
![MongoDB](https://img.shields.io/badge/MongoDB-Atlas-darkgreen)

---

## ✨ Features

### 👨‍🎓 Student Side
- **User Registration & Login** – Students can create an account and log in securely.
- **Dashboard** – A personalized dashboard after login.
- **View Alerts** – Browse all campus alerts and notices.
- **History** – View full history of past alerts.
- **Profile** – View logged-in student's profile details.

### 🛡️ Admin Side
- **Admin Login** – Separate admin authentication.
- **Admin Dashboard** – Dedicated control panel for admins.
- **Create Alerts** – Admins can publish new alerts with:
  - Title
  - Description
  - Priority level
  - Alert type
  - Date & Time

---

## 🗂️ Project Structure

```
CampusAlert/
├── alerts/                    # Main app (views, urls, models)
│   ├── migrations/
│   ├── views.py               # All business logic
│   ├── urls.py                # App URL routes
│   └── models.py
├── campusalert/               # Django project configuration
│   ├── settings.py            # Project settings
│   ├── urls.py                # Root URL configuration
│   └── wsgi.py / asgi.py
├── static/                    # CSS & JavaScript files
│   ├── style.css
│   └── script.js
├── templates/                 # HTML templates
│   ├── home.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── alerts.html
│   ├── history.html
│   ├── profile.html
│   ├── admin_login.html
│   ├── admin_dashboard.html
│   └── create_alert.html
├── mongodb.py                 # MongoDB connection config
├── manage.py                  # Django management script
├── requirements.txt           # Python dependencies
└── .gitignore
```

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| **Django** | Backend web framework |
| **MongoDB Atlas** | NoSQL database (via PyMongo) |
| **PyMongo** | MongoDB driver for Python |
| **HTML / CSS** | Frontend structure & styling |
| **JavaScript** | Client-side interactivity |
| **SQLite** | Django default DB (for admin/auth) |

---

## 📦 Prerequisites

Make sure you have the following installed:

- [Python 3.x](https://www.python.org/downloads/)
- [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) account (or local MongoDB)
- [Git](https://git-scm.com/)

---

## 🚀 Installation & Setup

Follow these steps to run the project locally:

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/CampusAlert.git
cd CampusAlert
```

### 2️⃣ Create & Activate a Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure MongoDB

Open `mongodb.py` and update the connection string with your own **MongoDB Atlas** connection URL:

```python
from pymongo import MongoClient

client = MongoClient("YOUR_MONGODB_CONNECTION_STRING")
db = client["CampusAlertDB"]
users = db["users"]
```

> ⚠️ **Security Note:** Never commit your real MongoDB credentials to GitHub. Use environment variables or a `.env` file instead.

### 5️⃣ Run Database Migrations

```bash
python manage.py migrate
```

### 6️⃣ Start the Development Server

```bash
python manage.py runserver
```

Open your browser and visit: **http://127.0.0.1:8000/**

---

## 🔑 Default Admin Credentials

The admin login is hardcoded in `alerts/views.py`:

- **Email:** `admin@gmail.com`
- **Password:** `admin123`

> ⚠️ Change these credentials before deploying to production.

---

## 📄 Pages / Routes

| Route | Description |
|-------|-------------|
| `/` | Home page |
| `/login/` | Student login |
| `/register/` | Student registration |
| `/dashboard/` | Student dashboard |
| `/profile/` | Student profile |
| `/alerts/` | View all alerts |
| `/history/` | Alert history |
| `/admin-login/` | Admin login |
| `/admin-dashboard/` | Admin dashboard |
| `/create-alert/` | Create a new alert (Admin) |

---

## 📦 Dependencies (`requirements.txt`)

```
asgiref==3.11.1
Django==3.1.12
djangorestframework==3.17.1
djongo==1.3.7
dnspython==2.8.0
pillow==12.3.0
pymongo==3.11.4
pytz==2026.2
sqlparse==0.2.4
tzdata==2026.2
```

---

## 🤝 Contributing

Contributions are always welcome! To contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes
4. Commit (`git commit -m "Add feature"`)
5. Push (`git push origin feature-branch`)
6. Open a Pull Request

---

## 📝 License

This project is for educational purposes. Add your license here if needed.

---

## 📧 Contact

For any questions or support, feel free to reach out.

---

**⭐ If you found this project helpful, don't forget to give it a star!**
