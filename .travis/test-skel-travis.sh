#!/bin/bash
# Flask-Diamond (c) Ian Dennis Miller

# scaffold the app
mkdir test-app
mrbob --config .travis/.mrbob.ini -O test-app skels/flask-diamond-app

# install and test the app
cd test-app
make install test
