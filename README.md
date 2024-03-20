# Run Django web project with Docker

### Update and upgrade
`sudo apt update && sudo apt full-upgrade`

### Install Git:
`sudo apt-get install -y git`
or
`sudo apt-get install -y git-all`

### (Optional) Generate ssh:
`ssh-keygen`

### (Optional) Get ssh key to add to github: 
`cat /root/.ssh/id_rsa.pub`

### Clone the project:
`git clone https://github.com/nataliasviattseva/ecommerce_project.git`

### Install Docker:
`TBD: see docker docs`

### Go to the project dir:
`cd ./ecommerce_project`

### Build the docker image:
`docker build -t ecommerce .`

### Create and run container:
`sudo docker run -p 7000:7000 -dit ecommerce`

### (Optional) To enter to the container
`docker exec -it 2d8ab8ca11b2 /bin/bash`

### (Optional)Build the project (from file docker-compose.yml):
`[sudo] docker compose run web django-admin startproject composedwebapp .`

`docker compose up`

------
# Install Postgres with Docker

#### 1. Run the PostgreSQL Container:

Use the following command to run a PostgreSQL container. This command also sets the PostgreSQL password for the default user (postgres).

`docker run --name pgsql-dev -e POSTGRES_PASSWORD=mysecretpassword -d -p 5432:5432 postgres`

#### 2. Access the PostgreSQL Shell:
You can access the PostgreSQL shell in the running container using the following command:
`docker exec -it pgsql-dev psql -U postgres`

This will connect you to the PostgreSQL command prompt.

#### 3. Create a Database:
In the PostgreSQL shell, you can create a new database. For example:
`CREATE DATABASE mydatabase;`

#### 4. Switch to the New Database:
After creating the database, you can connect to it using:
`\c mydatabase`

#### 5. Create Tables and Perform Operations:
Now, you can create tables and perform various operations within the mydatabase.

#### 6. Exit the PostgreSQL Shell:
To exit the PostgreSQL shell, type:
`\q`

#### 7. Stop and Remove the Container:
When you're done, you can stop and remove the PostgreSQL container:
`docker stop pgsql-dev`
`docker rm pgsql-dev`

------
# Create superuser while first run the project
python manage.py createsuperuser 


------
# Commandes utiles:

pip install -r requirements.txt

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
