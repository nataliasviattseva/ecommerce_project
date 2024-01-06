# Run Django web project with Docker

### Update and upgrade
`sudo apt update && apt full-upgrade
`

### Install Git:
`sudo apt-get install -y git-all`


### (Optional) Generate ssh:
`ssh-keygen`


### (Optional) Get ssh key to add to github: 
`cd /root/.ssh`
`cat id_rsa.pub`


### Clone the project:
`git clone https://github.com/nataliasviattseva/myDjangoProjet.git`


### Install Docker:
`bash /myDjangoProjet/dockerInstallPierre.sh`


### Go to the project dir:
`cd /myDjangoProjet`


### Build the docker image:
`docker build -t myDjangoProjet .`


### Create and run container (I've used 8000 port in docker files so here's also the same port, I don't know if is it possible to change it in the command...):
`docker run -d -p 8000:80 --name webapp myDjangoProjet`


### Build the project (from file docker-compose.yml):
`[sudo] docker compose run web django-admin startproject composedwebapp .`

`docker compose up`









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

Rerun server
python manage.py runserver

 admin
 Azerty123456

 To use images
 pip install pillow

 python.exe -m pip install --upgrade pip

python manage.py migrate
