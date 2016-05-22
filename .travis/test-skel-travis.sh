#!/bin/bash
# Flask-Diamond (c) Ian Dennis Miller

# create folder
mkdir test-app
cd test-app

# scaffold the app
mrbob --config ../.travis/.mrbob.ini ../skels/flask-diamond-app
make install test

# views
mrbob --config ../.travis/.mrbob.ini ../skels/example-views
make install test

# models
mrbob --config ../.travis/.mrbob.ini ../skels/example-models
make install test
