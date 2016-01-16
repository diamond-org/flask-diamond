#!/bin/bash

# usage:
# this script detects skew with diamond-app and diamond-project

# start with a fresh environment
rm -rf /tmp/flask-diamond

# clone flask-diamond
git clone -b 0.3 https://github.com/diamond-org/flask-diamond /tmp/flask-diamond

# apply the two diamond skeletons
mrbob --non-interactive --config .mrbob.ini -O /tmp/flask-diamond ./skels/flask-diamond-app

# change to the working path
cd /tmp/flask-diamond

# revert files that are idiosyncratic to flask-diamond
#git checkout setup.py
#git checkout flask_diamond/__init__.py
#git checkout flask_diamond/tests/test_models.py
git checkout MANIFEST.in
git checkout Readme.rst

# remove the schema migration that adds the Individual model, which is specific to diamond-app
rm flask_diamond/migrations/versions/13011baa608a_individual.py
rm Readme.md

# remove the simple CRUD associated with the Individual model
rm -rf flask_diamond/models \
    flask_diamond/views/administration \
    flask_diamond/views/base \
    flask_diamond/views/frontend

# now ideally there will be no diff
echo BEGIN diff
git status
echo END diff
