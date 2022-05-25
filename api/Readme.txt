				API SETUP
---------------------------------------------------------------------------------
#Database setUp and requirements settings Up

1- Create a new database like `prediction`, And specified in the.env file your database name and database config, .env file locate in market directory(market/.env)

2- install all requirements in the file requirements.txt 

To install requirements.txt file, you can use pip by running commande line below:
	pip install -r requirements.txt

To install pip, download get-pip.py file in the link below:
https://www.activestate.com/resources/quick-reads/how-to-install-pip-on-windows/

Next, move into directory containning the get-pip.py file and run commande line below:
	-python get-pip.py if you are using Linux OS
	-py get-pip.py if you are using Windows OS



3-Make migrations to create table in the new database 
You are in the projet folder

Linux OS:

#Create migration to the database
python manage.py makemigrations
python manage.py migrate

#run server in the project root
python manage.py runserver

Windows OS:

#Create migration to the database
py manage.py makemigrations
py manage.py migrate

#run server in the project root
py manage.py runserver
