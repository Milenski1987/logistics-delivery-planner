# 🚚 RouteMaster — Route & Delivery Management System
![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![Django](https://img.shields.io/badge/Django-6.0.1-green?logo=django)
![License](https://img.shields.io/badge/License-MIT-yellow)
![PostgreSQL](https://img.shields.io/badge/Database-PostgreSQL-336791?logo=postgresql)
![WhiteNoise](https://img.shields.io/badge/Static-WhiteNoise-lightgrey)

**RouteMaster** is a Django-based web application for managing logistics operations — all from a single, easy-to-use interface.



---

## 📋 Table of Contents

- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [System Overview](#-system-overview)
- [Screenshots](#-screenshots)
- [Dependencies](#-dependencies)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [Running the App](#-running-the-app)
- [Setting Up PostgreSQL](#-setting-up-postgresql)
- [Apps Overview](#-apps-overview)
- [Contributing](#-contributing)
- [License](#-license)

---

## ✨ Features

- **Driver Management** – Track driver profiles
- **Vehicle Management** – Track a fleet of vehicles with relevant details
- **Route Planning** – Define and manage routes, delivery points and assignments
- **Admin Panel** – Manage all data through Django's built-in admin interface

---

## 🧩 System Overview

- Each **Route** consists of multiple **Delivery Points**
- **Assignments** link Drivers and Vehicles to specific Routes
- The system ensures organized planning and execution of deliveries

---

## 📸 Screenshots

<table> <tr> <td align="center"> 
<img src="docs/images/Home.png" width="500"/><br> 
<sub>Home</sub> </td> <td align="center"> 
<img src="docs/images/Assignments.png" width="500"/><br> 
<sub>Assignments</sub> </td> </tr> </table>

---

## 🛠 Tech Stack

| Layer      | Technology                          |
|------------|-------------------------------------|
| Backend    | Python / Django                     |
| Frontend   | HTML / Django Templates / Bootstrap |
| Database   | PostgreSQL                          |
| Static Files | Whitenoise                          |

---

## 📁 Project Structure

```
logistics-delivery-planner/
│
├── logisticsDeliveryPlanner/   # Main Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── common/                     # Shared utilities, base models, mixins
├── drivers/                    # Driver management app
├── vehicles/                   # Vehicle fleet management app
├── routes/                     # Route, Delivery Point and Assignment management app
│   
├── templates/                  # HTML templates
├── static/                     # Static assets (images)
│
├── manage.py
├── requirements.txt            # Project dependencies
├── .env-example                # Example environment config
└── README.md
```

---

## 📦 Dependencies

All dependencies are listed in `requirements.txt`. Here's what each one does:

| Package | Version | Description |
|---|---|---|
| `Django` | 6.0.1 | The core web framework powering the entire application |
| `asgiref` | 3.11.0 | ASGI compatibility layer required by Django for async support |
| `psycopg2-binary` | 2.9.11 | PostgreSQL database adapter for Python — connects Django to your Postgres database |
| `python-dotenv` | 1.2.1 | Loads environment variables from the `.env` file into the app at runtime |
| `sqlparse` | 0.5.5 | SQL query formatter used internally by Django for readable query output |
| `tzdata` | 2025.3 | Timezone database used by Django for accurate timezone handling across environments |
| `whitenoise` | 6.11.0 | Serves static files directly from Django when `DEBUG = False`, without needing a separate web server like Nginx |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- pip
- virtualenv (recommended)
- PostgreSQL (see [Setting Up PostgreSQL](#-setting-up-postgresql))

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/Milenski1987/logistics-delivery-planner.git
cd logistics-delivery-planner
```

**2. Create and activate a virtual environment**

* *Windows:*
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```
* *macOS/Linux:*
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Set up environment variables**

Create a `.env` file in the root directory (next to `manage.py`). You can copy the example file:
```bash
cp .env-example .env
```

Then fill in your values:

| Variable | Example Value | Description |
|---|---|---|
| `SECRET_KEY` | `django-insecure-xxxx...` | Django's secret key used for cryptographic signing. Generate a new one for production — never share it publicly |
| `DB_NAME` | `routemaster` | Name of your PostgreSQL database |
| `DB_USER` | `routemaster_user` | PostgreSQL user with access to the database |
| `DB_PASSWORD` | `your_password` | Password for the PostgreSQL user |
| `DB_HOST` | `127.0.0.1` | Database host — use `127.0.0.1` for local development |
| `DB_PORT` | `5432` | Database port — `5432` is the PostgreSQL default |


> 💡 To generate a secure `SECRET_KEY` for production, run:
> ```bash
> python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
> ```

---


**5. Apply migrations (added data migration to populate database)**

```bash
python manage.py migrate
```

**6. Create a superuser (optional)**

```bash
python manage.py createsuperuser
```

**7. Collect static files**

```bash
python manage.py collectstatic
```

---

## ▶️ Running the App

```bash
python manage.py runserver
```

Then open your browser at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

The admin panel is available at: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

---


## 🐘 Setting Up PostgreSQL

### 1. Install PostgreSQL

**macOS (Homebrew):**
```bash
brew install postgresql@15
brew services start postgresql@15
```

**Ubuntu / Debian:**
```bash
sudo apt update
sudo apt install postgresql postgresql-contrib
sudo systemctl start postgresql
sudo systemctl enable postgresql
```

**Windows:**

Download and run the installer from [postgresql.org/download/windows](https://www.postgresql.org/download/windows/)

---

### 2. Create the Database and User

Open the PostgreSQL shell:

```bash
# macOS / Linux
psql postgres

# Ubuntu (switch to the postgres system user first)
sudo -u postgres psql
```

Then run the following SQL commands:

```sql
CREATE DATABASE database_name_of_your_choice;
CREATE USER username_of_your_choice WITH PASSWORD 'passowrd_of_your_choice';
ALTER ROLE username_of_your_choice SET client_encoding TO 'utf8';
ALTER ROLE username_of_your_choice SET default_transaction_isolation TO 'read committed';
ALTER ROLE username_of_your_choice SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE database_name_of_your_choice TO username_of_your_choice;
\q
```

Replace 'database_name_of_your_choice' with name you want for your database.

Replace 'username_of_your_choice' with name you want for your username.

Replace 'passowrd_of_your_choice' with paswword you want for your username password.

---

### 3. Configure `settings.py`

Make sure your `DATABASES` setting reads from your `.env` file:

```python
import os
from dotenv import load_dotenv

load_dotenv()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST', 'localhost'),
        'PORT': os.getenv('DB_PORT', '5432'),
    }
}
```

---

## 🗂 Apps Overview

### `common`
Contains utility functions, and any cross-app models or mixins. Other apps import from here to avoid code duplication.

### `drivers`
Handles everything related to drivers.

### `vehicles`
Manages the vehicle fleet. Includes vehicle registration, type categorization, capacity info.

### `routes`
The core of the application. Allows planners to create, update and delete Delivery Points, Routes and Assignments (assign vehicles and drivers to routes).

---

## 🤝 Contributing

Contributions are welcome! To get started:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/my-feature`
3. Commit your changes: `git commit -m "Add my feature"`
4. Push to the branch: `git push origin feature/my-feature`
5. Open a Pull Request

Please make sure your code follows the existing structure and includes relevant tests where applicable.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).