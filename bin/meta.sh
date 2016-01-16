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

# remove the schema migration that adds the Individual model, which is specific to diamond-app
rm flask_diamond/migrations/versions/13011baa608a_individual.py

# remove the simple CRUD associated with the Individual model
rm -rf flask_diamond/models \
    flask_diamond/views/administration \
    flask_diamond/views/base \
    flask_diamond/views/frontend

# revert files that are idiosyncratic to flask-diamond
#git checkout flask_diamond/tests/test_models.py
git checkout \
    setup.py \
    MANIFEST.in \
    Readme.rst \
    requirements.txt \
    flask_diamond/__init__.py \
    docs/conf.py \
    docs/index.rst \
    flask_diamond/models/__init__.py \
    flask_diamond/models/role.py \
    flask_diamond/models/user.py

# now ideally there will be no diff
echo BEGIN diff
git status
echo END diff
