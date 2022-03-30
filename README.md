# flash-flask-app #
Host flash files using a web app made with Flask.

Flash is already dead but I made this app in 2019 to at least view them easily in an old web browser that still supports the last flash plugin.
This app is slightly modified from the original one I made.


## How to Use ##
Add files to the static/flash folder with the following format: 

    creator/title/file.swf

Using flask, initialize the database using the command <pre><code>flask init-db</code></pre> then host the folder to a server of your choice.

Flask's deployment options can be found [here](https://flask.palletsprojects.com/en/2.1.x/deploying/)