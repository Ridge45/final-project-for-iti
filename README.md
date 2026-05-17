# Restaurant Management System (Django Web Application)

[![Django Version](https://img.shields.io/badge/Django-4.2.25-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Python Version](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Database](https://img.shields.io/badge/Database-PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![License](https://img.shields.io/badge/License-MIT-brightgreen?style=for-the-badge)](file:///c:/Users/maged/Downloads/final-project-for-iti-main/LICENSE)

A comprehensive, production-grade **Django-based web application** designed to streamline and automate day-to-day restaurant operations. The platform integrates a modern, responsive user interface with a robust backend architecture, empowering restaurant staff and administrators to seamlessly manage food menus, orders, customer metrics, and secure accounts.

<p align="center">
  <img src="iti last.gif" alt="Restaurant Management Preview" width="100%" style="border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.15);"/>
</p>


### 1. Accounts Module (accounts/)
* **Secure Authentication:** Integrates standard Django auth with custom security filters.
* **Role-Based Permissions:** Restricts item creations, updates, and deletes to verified staff and superusers using robust view decorators (`@staff_required` / `@login_required`).

### 2. Menu Module (menu/)
* **Class-Based CRUD Views:** Leverages robust Django Class-Based Views (`ListView`, `CreateView`, `UpdateView`, `DeleteView`) for fast and bug-free menu operations.
* **Advanced Real-Time Filtering:** Implements dynamic query set logic to search and paginate menu options instantly.
* **Image Processing:** Uses Python's `Pillow` library to store and serve high-definition item images locally and dynamically.

### 3. Orders Module (orders/)
* **Order Tracking & Processing:** Supports multiple order statuses and tracks real-time progress.
* **Shopping Cart & Checkout Integration:** Interacts seamlessly with the custom menu lists for standard customer flows.

### 4. Customers Module (customers/)
* **CRM Functionality:** Registers customer profiles, contact info, and saves long-term dining and order histories for loyalty analysis.

---

## Technology Stack

| Component | Technology | Description |
| :--- | :--- | :--- |
| **Backend Framework** | Django 4.2.25 | Premium Python-based web framework using MVC/MVT patterns. |
| **Database Engine** | PostgreSQL | Enterprise-grade Relational Database for reliable transactions. |
| **Frontend UI** | HTML5 / CSS3 / JavaScript | Responsive layout, tailored aesthetics, and animations. |
| **Image Engine** | Pillow | Django-integrated library to validate and compress food items. |
| **Utilities** | ASGI / SQLParse / Tzdata | Performance tools, async gateway protocols, and timezone converters. |

---

## Setup & Installation

Follow these steps to run the Restaurant Management System locally:

### Prerequisites
* **Python 3.10+** installed.
* **PostgreSQL** server running locally or remotely.

---

### Step 1: Clone and Navigate
```bash
git clone https://github.com/Ridge45/final-project-for-iti.git
cd final-project-for-iti/restaurant_project
```

### Step 2: Establish the Virtual Environment
Create and activate an isolated development environment:
* **Windows (PowerShell):**
  ```powershell
  python -m venv .venv
  .venv\Scripts\activate
  ```
* **Linux / macOS:**
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```

### Step 3: Install Core Dependencies
Install the required packages using the requirements list:
```bash
pip install -r requirements.txt
```

### Step 4: Configure the PostgreSQL Database
1. Launch PostgreSQL and create a database named `restaurant_db`:
   ```sql
   CREATE DATABASE restaurant_db;
   ```
2. Update the credentials in `restaurant_project/settings.py` (lines 67-76):
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'restaurant_db',
           'USER': 'your_postgres_user',
           'PASSWORD': 'your_postgres_password',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

### Step 5: Execute Migrations
Generate and write tables to your PostgreSQL database:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 6: Create the Admin Account
Create a superuser to access the management dashboard:
```bash
python manage.py createsuperuser
```
*(Enter your username, email, and password as prompted).*

### Step 7: Static & Media Assets Setup
Prepare directories to serve images and static elements:
```bash
python manage.py collectstatic --noinput
```

### Step 8: Run the Server
```bash
python manage.py runserver
```
The server will start on [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

---

## Global Routes & Access Points

| Portal | URL Route | Description |
| :--- | :--- | :--- |
| **Main Website (Menu Page)** | `http://127.0.0.1:8000/` | Entry point for customers to view the menu. |
| **Food Catalog Management** | `http://127.0.0.1:8000/menu/` | Main interactive control views for dishes. |
| **Order Gateway** | `http://127.0.0.1:8000/orders/` | Managing current tables and checkouts. |
| **Client Control** | `http://127.0.0.1:8000/customers/` | Customer history directory. |
| **Admin Dashboard** | `http://127.0.0.1:8000/admin/` | Complete Django Admin power-panel. |

---

## License & Terms

This project is licensed under the standard **MIT License**. Check out the [LICENSE](file:///c:/Users/maged/Downloads/final-project-for-iti-main/LICENSE) file in the root directory for the complete legal text.

Developed as a Final Graduation Project for **ITI (Information Technology Institute)**. Built with precision, optimization, and scale in mind.
