# Gate
Beyond this Gate is your very own personal website that you learned to code from the
ground up. This tutorial is aimed towards those with very minimal amounts of coding
background, but who are interested in coding their own personal website. Topics that
are covered include getting a development environment set up on Linux and OS X (and
kind of Windows), navigating with the command line, and using Vim as a text editor.
Python, HTML, CSS, and a small amount of Javascript will make up the bulk of the
tutorial, along with putting it all together using Google's webapp2 framework. This
will allow for the app to easily be hosted with Google App Engine with very minimal
further effort. By the end of the tutorial, you should have a simple blogging app
where you understand how all of the parts fit together and how to tweak them to make
it your own. If there is anything that is unclear or poorly documented, send me a
message or open up an Issue on GitHub.


### [Click Here To Get Started](http://samolds.github.io/gate)


### Resources
[Guides](http://samolds.github.io/gate) | [Checkpoints](checkpoints) | [References](http://samolds.github.io/gate)
--- | --- | ---
[Overview](http://samolds.github.io/gate) | [Barebone](checkpoints/barebone) | [Python](http://samolds.github.io/gate)
[Getting Started](http://samolds.github.io/gate) | [Scaffolded](checkpoints/scaffolded) | [HTML](http://samolds.github.io/gate)
[MVC Pattern](http://samolds.github.io/gate) | [Bootstrapped](checkpoints/bootstrapped) | [CSS](http://samolds.github.io/gate)
[Controllers](http://samolds.github.io/gate) | [Interactive](checkpoints/interactive) | [Javascript](http://samolds.github.io/gate)
[Views](http://samolds.github.io/gate) | [Admin](checkpoints/admin) | [Vim](http://samolds.github.io/gate)
[Models](http://samolds.github.io/gate) | [Built Out](checkpoints) | [Useful Command Line Tools](http://samolds.github.io/gate)


### External Resources
* [Python Tutorial](#)
* [HTML Tutorial](#)
* [Jinja Documentation](http://jinja.pocoo.org/docs/dev/templates)
* [CSS Tutorial](#)
* [Bootstrap Documentation](http://getbootstrap.com/css)
* [Javascript Tutorial](#)
* [Vim Tutorial](#)
* [HTML Tutorial](#)


### System Requirements
* [Google App Engine SDK](http://developers.google.com/appengine/downloads)
* Python 2.7
* VirtualEnv


### Setup Instructions
The following will set up the final checkpoint as an example for what can be
acheived with this tutorial:

* Change variable values accordingly in app/settings.py

```
git clone http://github.com/samolds/gate.git
cd gate
virtualenv --no-site-packages env
source env/bin/activate
cd app
mkdir lib
pip install -t lib -r requirements.txt
cd ..
/usr/local/google_appengine/dev_appserver.py app
```

You should now have a skeleton of the site up and running on localhost:8080.
Thanks for playing!
