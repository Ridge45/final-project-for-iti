# Restaurant Management System

<p align="center">
  <img src="iti last.gif" width="900"/>
</p>

A comprehensive Django-based web application designed to streamline restaurant operations. The system enables efficient management of menus, orders, customers, and user accounts through a clean and user-friendly interface for both staff and administrators.

---

## Features

- Menu Management  
  Add, edit, and manage restaurant menu items with descriptions, prices, and images.

- Order Processing  
  Handle customer orders with multiple order statuses.

- Customer Management  
  Store customer information and track order history.

- User Authentication  
  Secure login system using Django authentication.

- Admin Dashboard  
  Powerful Django admin panel for managing all system data.

- Media Handling  
  Upload and display menu item images.

- Responsive Design  
  Clean and responsive user interface.

---

## Technologies Used

| Technology | Usage |
|---|---|
| Django 4.2.25 | Backend Framework |
| PostgreSQL | Database |
| HTML/CSS/JavaScript | Frontend |
| Pillow | Image Processing |
| ASGI / SQLParse / Tzdata | Additional Dependencies |

---

## Installation

Make sure you are inside the `restaurant_project` folder before running the server.

### 1. Clone the Repository

```bash
git clone https://github.com/Ridge45/final-project-for-iti.git
cd final-project-for-iti
```

### 2. Create Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate Virtual Environment

#### Windows

```bash
.venv\Scripts\activate
```

#### Linux / macOS

```bash
source .venv/bin/activate
```

---

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 5. Configure PostgreSQL Database

Create a PostgreSQL database named:

```text
restaurant_db
```

Update the database settings inside:

```text
restaurant_project/settings.py
```

Example configuration:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'restaurant_db',
        'USER': 'restaurant_user',
        'PASSWORD': 'your_password_here',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

---

### 6. Run Database Migrations

```bash
python manage.py migrate
```

---

### 7. Create Superuser

```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin account.

---

### 8. Collect Static Files

```bash
python manage.py collectstatic
```

---

### 9. Run Development Server

```bash
python manage.py runserver
```

---

## Access the Application

| Service | URL |
|---|---|
| Main Website | http://127.0.0.1:8000/ |
| Admin Panel | http://127.0.0.1:8000/admin/ |

---

## Project Preview

Add screenshots inside an `assets` folder.

Example:

```md
![Home Page](assets/home.png)
```

---

## Author

Developed as a final project for ITI.
