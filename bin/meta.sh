#!/bin/bash

# start with a fresh environment
rm -rf /tmp/diamond-project /tmp/diamond-app /tmp/flask-diamond

# clone flask-diamond and the diamond skeletons
git clone https://github.com/iandennismiller/diamond-project /tmp/diamond-project
git clone https://github.com/iandennismiller/diamond-app /tmp/diamond-app
git clone -b task/refactor-0.2 https://github.com/iandennismiller/flask-diamond /tmp/flask-diamond

# apply the two diamond skeletons
mrbob --config .mrbob.ini -O /tmp/flask-diamond /tmp/diamond-project/skel
mrbob --config .mrbob.ini -O /tmp/flask-diamond /tmp/diamond-app/skel

# change to the working path
cd /tmp/flask-diamond

# revert files that are idiosyncratic to flask-diamond
git checkout setup.py
git checkout flask_diamond/__init__.py
git checkout flask_diamond/tests/test_models.py

# remove the schema migration that adds the Individual model, which is specific to diamond-app
rm flask_diamond/migrations/versions/13011baa608a_individual.py

# remove the simple CRUD associated with the Individual model
rm -rf flask_diamond/models \
	flask_diamond/views/administration \
	flask_diamond/views/base \
	flask_diamond/views/frontend

# now ideally there will be no diff
echo BEGIN diff
git status
echo END diff
