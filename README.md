# OnlineFeedbackSystem Mini Project (Django Web Framework)
Install following  packages in command prompt :

Django : 2.2.5
sqlparse
Pillow
Faker
bcrypt
argon2-cffi
certifi
cffi
pycparser
python-dateutil
pytz
setuptools
six
text-unidecode
wheel
wincertstore

To install the packages....

Run the command :  pip install package_name (except for Django)
For Django : pip install Django == 2.2.5

After installing above packages : Downnload the zip file...Go to location of "MiniProject" directory using (cd) command
Run the following 3 commands :

1)  python manage.py migrate
2)  python manage.py makemigrations
3)  python manage.py migrate

Now you've set up the database...Time to Run the Application...
Run the command :

python manage.py runserver

Go to the url specified by the terminal(http://127.0.0.1:8000/) in general.
Copy the url specified by terminal and paste it in your Browser...
