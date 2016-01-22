#!/bin/bash
# Flask-Diamond (c) Ian Dennis Miller

source "$(which virtualenvwrapper.sh)"

# clean out old environment
rmvirtualenv "test-app"
rm -rf /tmp/test-app

# scaffold fresh from flask-diamond
workon flask-diamond && diamond-scaffold.sh /tmp/test-app

# create virtualenv
pushd /tmp/test-app
mkvirtualenv -a . "test-app"

# install test app
source "$(which virtualenvwrapper.sh)" && workon "test-app" && make install
popd
