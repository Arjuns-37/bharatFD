*** 🏢BharatFD - Multilingual FAQ Model***
This project provides a multilingual FAQ model with automatic translation support, built using Django and leveraging the googletrans library for translation. 
The FAQ model can store questions and answers in multiple languages, and it uses Django's caching system to improve performance by reducing the number of API calls for translation.


## Installation Steps

1)Clone the repository

    git clone https://github.com/Arjuns-37/bharatFD.git
    cd bharatFD
    
2)Create a Virtual Environment
  
    python -m venv venv
      # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
3)Install Dependencies

    pip install -r requirements.txt
4)Apply Migrations

    python manage.py migrate

5)Run the Development Server

    python manage.py runserver


## Prerequisties

1)Python 3.6+
2)Pip
3)Virtual Environment

    python -m venv venv

4)Django
The project uses Django as the backend framework. You can install it with


    pip install django

5)Google Translate API:This project uses the Google Translate API for translations


    pip install googletrans==4.0.0-rc1

6)CKEditor:This project uses CKEditor for rich text editing


    pip install django-ckeditor

7)PostgreSQL or SQLite(You can use either PostgreSQL or SQLite for database management)


    pip install psycopg2


## Frontend Running port:

    http://127.0.0.1:8000

##  Django admin panel

    http://127.0.0.1:8000/admin

# Steps to Access Django Admin Panel:


1)Run the server

    python manage.py createsuperuser

2)Create an Admin User (if not created already)


    python manage.py createsuperuser
    ##You'll be prompted to enter a username, email, and password for the admin user.

    

3)Access Admin Panel: After successfully running the server and creating the admin user, you can access the admin panel by navigating to


    http://127.0.0.1:8000/admin
    ##Log in using the credentials you provided while creating the superuser.




    ## Author

    
Project Developed By **SADINENI MALLIKARJUN** For BharatFD Backend Developer Intern Test.

    






















