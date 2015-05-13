The River
=========
A very simple blogging example app using Django and Google App Engine.
Contains a page called The River, which collects your activity streams from Twitter, Flickr, GitHub, Last.fm, Soundcloud, and this Blogging app

System Requirements
-------------------
* Python 2.7
* VirtualEnv
* [GAE](http://cloud.google.com/appengine/docs/python)

Setup Instructions
------------------
* Clone the repository
```
git clone https://github.com/samolds/theriver.git
```
* Sandbox the app with VirtualEnv
```
virtualenv --no-site-packages theriver
```
* Activate the sandbox and install dependencies with Pip
```
cd theriver
source bin/activate
pip install -r env/requirements.txt
mkdir theriver/gaenv
linkenv lib/python2.7/site-packages theriver/gaenv
```
* Change variable values accordingly in theriver/local_settings.py to get The River working
* Establish a database with a superuser
```
python manage.py syncdb
```
* Run the site
```
path/to/google_appengine/dev_appserver.py --port=8000 theriver
```

You should now have a skeleton of the site up and running on localhost:8000. Go to 'localhost:8000/admin', log in with the user established with the 'syncdb' command, and add posts to see content appear.


Useful Links
------------
* [Django-nonrel](https://cloud.google.com/appengine/articles/django-nonrel)
