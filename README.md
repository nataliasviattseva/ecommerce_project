# Run Django web project with Docker

### Update and upgrade
`sudo apt update && apt full-upgrade
`

### Install Git:
`sudo apt-get install -y git`
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
`cd /ecommerce_project/bash_scripts`


### Build the docker image:
`docker build -t ecommerce .`


### Create and run container:
last that works: `sudo docker run -p 7000:7000 -dit ecommerce`

sudo docker run -it -p 8000:8000 ecommerce

`docker run -d -p 7000:80 --name webapp ecommerce`

### To enter to the container
`docker exec -it 2d8ab8ca11b2 /bin/bash`


### Build the project (from file docker-compose.yml):
`[sudo] docker compose run web django-admin startproject composedwebapp .`

`docker compose up`


------

# Install Postgres Docker Official Image

`docker pull postgres`

`docker run --name pgsql-dev -e POSTGRES_PASSWORD=Welcome4$ -p 5432:5432 postgres`

***

### ChatGPT:

#### 1. Run the PostgreSQL Container:

Use the following command to run a PostgreSQL container. This command also sets the PostgreSQL password for the default user (postgres).

`docker run --name my-postgres-container -e POSTGRES_PASSWORD=mysecretpassword -d -p 5432:5432 postgres`

--name: Assigns a name to the container (you can choose your own).

-e POSTGRES_PASSWORD: Sets the password for the PostgreSQL user 'postgres'.

d: Runs the container in the background.

-p 5432:5432: Maps the host machine's port 5432 to the container's port 5432.


#### 2. Access the PostgreSQL Shell:
You can access the PostgreSQL shell in the running container using the following command:
`docker exec -it my-postgres-container psql -U postgres`

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
`docker stop my-postgres-container`
`docker rm my-postgres-container`

***

<details>
  <summary>как запустить что-то работающее</summary>
  https://commandprompt.com/education/how-to-install-postgresql-using-docker-compose/
</details>

***

<details>
  <summary>Не работает</summary>

https://www.docker.com/blog/how-to-use-the-postgres-docker-official-image/

https://hub.docker.com/_/postgres


https://www.commandprompt.com/education/how-to-create-a-postgresql-database-in-docker/

(Optional - don't want to delete) Grab the latest Postgres version from Docker Hub:
`docker pull postgres`

(Optional - don't want to delete) 
`docker run --name some-postgres -e POSTGRES_PASSWORD={pw} -d postgres`


FROM HERE:

Install git: https://github.com/nataliasviattseva/myDjangoProjet/wiki/Run-Django-web-project-with-Docker#install-git

`git clone https://github.com/nataliasviattseva/postgres.git`

Install Docker: `bash /postgres/dockerInstallPierre.sh`

`cd /postgres`

`docker compose -f dbGreta78.db up` (doesn't work --> **ERROR: parsing /postgres/dbGreta78.db: yaml: control characters are not allowed)**

</details>



-------


# How to Configure Static IP Address on Ubuntu 22.04

https://tecadmin.net/how-to-configure-static-ip-address-on-ubuntu-22-04/

https://linuxize.com/post/how-to-configure-static-ip-address-on-ubuntu-20-04/


------

# from SQLITE3 to Postgres

`python3 manage.py dumpdata > datadump.json`

--------

# Ansible


sudo apt install ansible

-------

# Other commands (for Django)


pip install Django

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
