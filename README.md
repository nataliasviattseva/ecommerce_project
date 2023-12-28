Pip install Django

django-admin startproject ecommerce
cd ecommerce

python manage.py startapp store

python manage.py runnserver

To make migrations
python .\manage.py makemigrations

To apply the changes
python .\manage.py migrate

To create a superuser
 python manage.py createsuperuser 
