#!/bin/bash
# Flask-Diamond (c) Ian Dennis Miller

# usage:
# this script detects skew with the skeleton

# start with a fresh environment
rm -rf /tmp/flask-diamond

# clone flask-diamond
git clone -b 0.3 . /tmp/flask-diamond

# apply the two diamond skeletons
mrbob --non-interactive --config .mrbob.ini -O /tmp/flask-diamond ./skels/flask-diamond-app

# change to the working path
cd /tmp/flask-diamond

# remove the views
rm -rf flask_diamond/views/administration \
    flask_diamond/views/base \
    flask_diamond/views/frontend

# revert files that are idiosyncratic to flask-diamond
git checkout \
    setup.py \
    requirements.txt \
    docs/conf.py \
    docs/index.rst \
    flask_diamond/__init__.py \
    flask_diamond/models/__init__.py

# now ideally there will be no diff
echo BEGIN diff
git status
echo END diff
