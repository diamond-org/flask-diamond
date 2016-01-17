#!/bin/bash

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

# remove the schema migration that adds the Individual model, which is specific to diamond-app
rm flask_diamond/migrations/versions/13011baa608a_individual.py

# remove the simple CRUD associated with the Individual model
rm -rf flask_diamond/models \
    flask_diamond/views/administration \
    flask_diamond/views/base \
    flask_diamond/views/frontend

# revert files that are idiosyncratic to flask-diamond
git checkout \
    setup.py \
    requirements.txt \
    docs/conf.py \
    docs/index.rst \
    flask_diamond/__init__.py \
    flask_diamond/models/__init__.py \
    flask_diamond/models/role.py \
    flask_diamond/models/user.py \
    flask_diamond/tests/test_models.py

# now ideally there will be no diff
echo BEGIN diff
git status
echo END diff
