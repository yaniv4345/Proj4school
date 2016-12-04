# Proj4school
Project for python class in school, simple website.

Install:

Install ptyhon-virtualenv and git from your package manager.

Create virtual enviroment:

   virtualenv DIR_NAME

Clone this project:

   git clone https://github.com/yaniv4345/Proj4school.git

Copy everything from Proj4school into virtualenv dir:

   cp -r Proj4school/* DIR_NAME/

Activate virtualenv:

   source DIR_NAME/bin/activate

Install requirements:

   pip install -r requirements.txt

Create database:

   python manage.py makemigrations
 
 Migrate database:
 
    python manage.py migrate
   
 Create superuser:
 
    python manage.py createsuperuser
 
 Run server:
 
    python manage.py runserver 0.0.0.0:8000
   
