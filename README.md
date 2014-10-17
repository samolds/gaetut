SAMSITE
=======
A personal website using Django, but restructured to work with Google App Engine (GAE).
(Not yet fully restructured to work with GAE. But soon.)


Project Requirements
-------------------
* Python 2.7
* Pip
* VirtualEnv
* Linkenv (Maybe? Still figuring out how to get dependencies working with GAE)
* GAE


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
* Activate the sandbox and install dependencies with Pip (Not fully fleshed out... GAE doesn't play nicely with VirtualEnv and dependencies in requirements.txt...)
```
cd samsite
source bin/activate
pip install -r sam/requirements.txt
```
* Change variable values accordingly in samsite/local_settings.py
* Establish a database with a superuser (Maybe this will work. But models.py is definitely not ready to be supported by Google's nonrel db)
```
python manage.py syncdb
```

* Run the site (Haven't made it this far yet)
```
path/to/google_appengine/dev_appserver.py --port=8000 samsite
```

Suppose all of the previous commands worked, you should have a Django app running locally on GAE. At this point, you could set up a project online with Google and theoretically deploy this app and and have a Django site running on whaterrrr.appspot.com
