To Do
=====
Hopes
-----
* Get a real ticket tracker
* Get PIL working and serving jpgs (http://djangodays.com/2008/09/03/django-imagefield-validation-error-caused-by-incorrect-pil-installation-on-mac/)
* Facebook API?? (HAH! ...not...)
* Upgrade from Django 1.5 to Django 1.7
* Improve the security of the Django Admin login panel. Research Django authentication stuff
* Save results of api calls in simple model in db that has the html to display and a hash of the html as the primary key?


Realistic
---------
* !- Restructure model.py to work with a non-relational database http://www.allbuttonspressed.com/projects/djangoappengine (Remove ManyToManyField and ImageField)
* !- DEPLOY TO GOOGLE APP ENGINE
* !- Standardize camelCase and under_score variable names (according to language being used: python: low_dash, javascript: camelCase, html/css: mid-dash)
* !- Clean up basic.css and embed.js
* !- Make a better favicon
* !- Re-opensource the project
* !- https://docs.djangoproject.com/en/1.5/howto/static-files/
* Update how imgurs are displayed with whether or not it is an album, and include the description if it exists
* Get Imgur API working: https://api.imgur.com/oauth2#auth_url
* Get the real email stuff set up and working with comments
* Make sure image serving is correctly working
* CLEAN UP CODE
* Comment Code
* Unit Test
* Design things to be more minimal?
* Add thank you to JT, Craig, Zach (dude who pointed me in the right direction for github api) and a handful of various stack overflow people for help


Done/Cancelled
==============
* Add views counter to blog posts
* Clean up javascript embed function. Break up into multiple functions
* Break layouts.css into multiple css files
* Add live typing error pages (http://livetyping.com)
* Make imgur and facebook checkboxes on front page not clickable
* Add a robots.txt file or whatever for site crawling
* On mobile, make content section not have much side padding. Have everything fill horizontally with no border around content
* Simplify background texture (Smaller with repeats?)
* Add minimal texture to navbar? (Smaller with repeats?)
* Fix console error on front page
* Include any lastfm "Now Playing" on the front page under random quote?
* Make loading gif on front page randomly select one of my favorite gifs (compress and make same height)
* Get api calls on front_page to actually weave together correctly based on time
* Combine front_page.html and ajax.html
* Weave API call line items on front_page together (http://www.w3schools.com/jsref/dom_obj_all.asp)
* Move javascript in front_page.html to js file
* Remove set_var templatetag
* Locally cache lastfm stuff every 1 minute
* Check what happens when front page is cached. Are AJAX calls still made?
* On front page, make the border of each thing the color instead of the background
* Center loading gif
* Make sure github api posts look good
* Make buttons nicer with hover-over?
* Remove SHA1 POST password generator and replace with JT's javascript one
* Make sure I only have necessary dependencies in settings.py (Don't need cucumber anymore?)
* Open source stuff and remove personal information stuff and add to settings.py
* Make navbar work with mobile (and then remove mobile warning)
* Make Readme file have correct setup instructions
* Have "This part has yet to be written" moved out into a context_processor and not hardcoded
* Add better error pages (401, 404, 500, etc.)
* Add different background color for each front page item (soundcloud = light orange, lastfm = light red, flickr = light purple, github = light gray, twitter = light blue
* Make The Front Page load information asynchronously (ajax, jquery, celery) and then locally cache it. Also, get it to automatically recache after the cache expires?
  * http://django-cacheback.readthedocs.org/en/latest/
  * http://stackoverflow.com/questions/3583534/refresh-div-element-generated-by-a-django-template
  * https://racingtadpole.com/blog/django-ajax-and-jquery/
  * http://codeinthehole.com/writing/cacheback-asynchronous-cache-refreshing-for-django/
  * http://www.celeryproject.org/tutorials/
  * http://stackoverflow.com/questions/23856259/how-to-correctly-refresh-a-div-using-jquery-ajax-in-a-django-template
  * https://racingtadpole.com/blog/django-ajax-and-jquery/
