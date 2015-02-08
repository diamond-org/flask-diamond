#!/bin/bash

rm -rf /tmp/diamond-scaffold /tmp/diamond-app /tmp/flask-diamond

git clone https://github.com/iandennismiller/diamond-project /tmp/diamond-project
git clone https://github.com/iandennismiller/diamond-app /tmp/diamond-app
git clone https://github.com/iandennismiller/flask-diamond /tmp/flask-diamond

mrbob --config .mrbob.ini -O /tmp/flask-diamond /tmp/diamond-project/skel
mrbob --config .mrbob.ini -O /tmp/flask-diamond /tmp/diamond-app/skel

cd /tmp/flask-diamond
git checkout setup.py
git checkout flask_diamond/__init__.py
rm -rf flask_diamond/models views/administration views/base views/frontend
