# Restaurant Management System

A comprehensive **Django-based web application** designed to streamline restaurant operations. This system allows for efficient management of menus, orders, customers, and user accounts, providing a user-friendly interface for both staff and administrators.

## Features

- **Menu M**: edit, and manage restaurant menu items with descriptions, prices, and images.  
- **Order Processing**: Handle customer orders with various statuses 
- **Customer Management**: Maintain a database of customers with contact information and order history.  
- **User Authentication**: Secure login system for staff and administrators using Django's built-in authentication.  
- **Admin Interface**: Powerful Django admin panel for easy data management.  
- **Media Handling**: Support for uploading and displaying menu item images.  
- **Responsive Design**: Clean, user-friendly interface built with Django templates.  

## Technologies Used

- **Backend**: Django 4.2.25  
- **Database**: PostgreSQL  
- **Frontend**: HTML, CSS, JavaScript (Django Templates)  
- **Image Processing**: Pillow  
- **Other**: ASGI, SQLParse, Tzdata

## Installation

  ''''''''''''''' Make sure you are on the restaurant_project forlder before running server '''''''''''''''''''''''''''''''''''''''''''''''''''''''


### Prerequisites

- Python 3.8 or higher  
- PostgreSQL installed and running  
- Git  

### Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Ridge45/final-project-for-iti.git
   cd final-project-for-iti
Create a virtual environment:

bash
Copy code
python -m venv .venv
# On Linux/Mac
source .venv/bin/activate
# On Windows
.venv\Scripts\activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Set up PostgreSQL database:

Create a new PostgreSQL database named restaurant_db

Create a database user restaurant_user with password of your choice

Update the database settings inside restaurant_project/settings.py

Example:

python
Copy code
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
Run database migrations:

bash
Copy code
python manage.py migrate
Create a superuser account:

bash
Copy code
python manage.py createsuperuser
Follow the prompts to create an admin account.

Collect static files:

bash
Copy code
python manage.py collectstatic
Run the development server:

bash
Copy code
python manage.py runserver
Access the application:

Main site → http://127.0.0.1:8000/

Admin panel → http://127.0.0.1:8000/admin/
