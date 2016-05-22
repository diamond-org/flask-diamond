#!/bin/bash
# Flask-Diamond (c) Ian Dennis Miller

# create folder
mkdir -p build/test-app
cd build/test-app

# scaffold the app
mrbob --config ../../skels/test-app/.mrbob.ini ../../skels/flask-diamond-app
make install test

# views
mrbob --config ../../skels/test-app/.mrbob.ini ../../skels/example-views
make install test

# models
mrbob --config ../../skels/test-app/.mrbob.ini ../../skels/example-models
make install test

cd ../..
rm -rf build/test-app
