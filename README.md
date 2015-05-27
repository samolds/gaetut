# GAETut
A very barebones app designed to be used as a tutorial for getting a simple site
hosted on [Google App Engine](http://cloud.google.com/appengine/docs/python). If
there is anything that is unclear or poorly documented, send me a message or
open up an Issue on GitHub.


### System Requirements
* Python 2.7
* VirtualEnv
* [Google App Engine SDK](http://developers.google.com/appengine/downloads)


### Guides
* [Overview](guide/overview.md)
* [Getting Started](guide/getting_started.md)
* [MVC Pattern](guide/mvc.md)
* [Controllers](guide/controllers.md)
* [Views](guide/views.md)
* [Models](guide/models.md)


### Checkpoints
1. [Barebones](checkpoints/barebone)
2. [Scaffolded](checkpoints/scaffolded)
3. [Bootstrapped](checkpoints/bootstrapped)
4. [Final](checkpoints/final)


### References
* [Python Reference](guide/python_ref.md)
* [HTML Reference](guide/html_ref.md)
* [CSS Reference](guide/css_ref.md)
* [Javascript Reference](guide/js_ref.md)


### Setup Instructions
The following will set up the final checkpoint as an example for what can be
acheived with this tutorial:

* Change variable values accordingly in app/settings.py

```
git clone http://github.com/samolds/gaetut.git
cd gaetut
virtualenv --no-site-packages env
source env/bin/activate
cd app
mkdir lib
pip install -t lib -r requirements.txt
cd ..
/usr/local/google_appengine/dev_appserver.py app
```

You should now have a skeleton of the site up and running on localhost:8080.


