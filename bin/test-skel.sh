#!/bin/bash
# Flask-Diamond (c) Ian Dennis Miller

source "$(which virtualenvwrapper.sh)"

# clean out old environment
rmvirtualenv "test-app"
rm -rf /tmp/test-app

# scaffold fresh from flask-diamond
echo
echo "instructions"
echo
echo "1. call application 'test-app'"
echo "2. call module 'test_app'"
echo "3. accept all other defaults with ENTER"
echo
workon flask-diamond && flask-diamond app /tmp/test-app

# create virtualenv
pushd /tmp/test-app
mkvirtualenv -a . "test-app"

# install test app
source "$(which virtualenvwrapper.sh)" && workon "test-app" && make install
popd
