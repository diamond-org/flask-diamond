#!/bin/bash
# Flask-Diamond (c) Ian Dennis Miller

# scaffold the app
mkdir test-app
cd test-app
flask-diamond app .

# install and test the app
make install test
