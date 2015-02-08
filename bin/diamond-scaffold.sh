#!/bin/bash

# usage:
# Run diamond-scaffold.sh in the target project directory.
# It will create a minimal app.

# start with a fresh environment
rm -rf /tmp/diamond-project /tmp/diamond-app

# clone flask-diamond and the diamond skeletons
git clone https://github.com/iandennismiller/diamond-project /tmp/diamond-project
git clone https://github.com/iandennismiller/diamond-app /tmp/diamond-app

# apply the two diamond skeletons
mrbob -w /tmp/diamond-project/skel
mrbob --config .mrbob.ini -w /tmp/diamond-app/skel
