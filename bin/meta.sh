#!/bin/bash
# Flask-Diamond (c) Ian Dennis Miller

# usage:
# this script detects skew with the skeleton

# start with a fresh environment
rm -rf /tmp/flask-diamond

# clone flask-diamond
git clone . /tmp/flask-diamond

# apply the diamond skeletons
mrbob --non-interactive --config .mrbob.ini -O /tmp/flask-diamond ./skels/flask-diamond-app

# change to the working path
pushd /tmp/flask-diamond

# remove the views
rm -rf flask_diamond/views/administration

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

popd
