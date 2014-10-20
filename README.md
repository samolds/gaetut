SAMSITE
=======
So I'm abandoning this endeavor. I think I'm just going to deploy the pure Django site on AWS.

I'm thinking I might try to revamp this repo to just be an example of getting a simple Django app running on GAE, but my current samsite project is too complex for GAE.



---------

ABANDONED
=========
A personal website using Django, but restructured to work with Google App Engine (GAE).
(Not yet fully restructured to work with GAE. But soon.)
Been looking [here for some reference](http://djangoappengine.readthedocs.org/en/latest/installation.html)


Project Requirements
-------------------
* Python 2.7
* Pip
* VirtualEnv
* Git
* [Linkenv](http://github.com/ze-phyr-us/linkenv)
* [GAE](http://cloud.google.com/appengine/docs/python)


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
* Activate the sandbox and install dependencies with Pip and symlink them with Linkenv
```
cd samsite
source bin/activate
pip install -r sam/requirements.txt
mkdir gaenv
```
* Make sure "PIL" (without quotes) is the first line of lib/python2.7/site-packages/PIL/PIL-x.x.x-pyx.x.egg-info/top_level.txt
```
linkenv lib/python2.7/site-packages gaenv
```
* Change variable values accordingly in samsite/local_settings.py
* ------------ Haven't made it past this point... ------------------------------------
* Establish a database with a superuser (Maybe this will work. But models.py is definitely not ready to be supported by Google's nonrel db)
```
python manage.py syncdb
```

* Run the site (Haven't made it this far yet)
```
path/to/google_appengine/dev_appserver.py --port=8000 samsite
```

Suppose all of the previous commands worked, you should have a Django app running locally on GAE. At this point, you could set up a project online with Google and theoretically deploy this app and and have a Django site running on whaterrrr.appspot.com
