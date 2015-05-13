# Riv
A very barebones Django app designed to be used as a tutorial for getting a simple site
hosted on [Google App Engine](http://cloud.google.com/appengine/docs/python). Uses the
[Django-nonrel](http://django-nonrel.org) project, and includes a page called The River.
See The River in action [here](http://samolds.com/river). If there is anything that is
unclear or poorly documented, send me a message or open up an Issue on GitHub.


### System Requirements
* Python 2.7
* [Google App Engine SDK](http://developers.google.com/appengine/downloads)


### Setup Instructions
```
git clone https://github.com/samolds/riv.git
cd riv
python manage.py syncdb
```
* Change variable values accordingly in theriver/local_settings.py to get The River working
```
python manage.py runserver
```
--- OR ---
```
path/to/google_appengine/dev_appserver.py .
```

You should now have a skeleton of the site up and running on localhost:8080. Go to 'localhost:8080/admin', log in with the user established with the 'syncdb' command, and add posts to see content appear.


### Useful Links
* [Django-nonrel](https://cloud.google.com/appengine/articles/django-nonrel)
