### For publishing webapp2 project to Google App Engine:
* Sign onto the [Google developer console](http://console.developers.google.com)
  * Click `Create Project` and give it a <project-name>
  * Click `Try App Engine`
  * Select `Python`
  * Install the Google Cloud SDK
    * `curl https://sdk.cloud.google.com/ | bash`
      * If using OSX, store the Cloud SDK in `/usr/local`
    * Restart the shell
    * `gcloud auth login`
      * The Google Account you allow access will become the only Google Account that can log into the "Admin" portion
    * `gcloud components update gae-python`
  * `appcfg.py -A <project-name> update gate/app`
* Go to [<project-name>.appspot.com](http://<project-name>.appspot.com) to use your project
