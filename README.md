SAMSITE
=======
A personal website using Django, but restructured to work with Google App Engine.

System Requirements
-------------------
* Python 2.7
* Pip
* VirtualEnv


Setup Instructions
------------------
* Clone the repository
```
git clone https://github.com/samolds/samsite-nonrel.git samsite
```
* Sandbox the app with VirtualEnv
```
virtualenv --no-site-packages samsite
```
* Activate the sandbox and install dependencies with Pip
```
cd samsite
source bin/activate
pip install -r sam/requirements.txt
```
* Change variable values accordingly in samsite/local_settings.py
* Establish a database with a superuser
```
python manage.py syncdb
```
* Run the site
```
python manage.py runserver 8000
```


You should now have a skeleton of the site up and running on localhost:8000. Go to 'localhost:8000/admin', log in with the user established with the 'syncdb' command, and add posts to see content appear.
