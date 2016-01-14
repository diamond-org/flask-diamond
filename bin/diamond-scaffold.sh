#!/bin/bash

# usage:
# Run diamond-scaffold.sh in the target project directory.
# It will create a minimal app.

# apply the two diamond skeletons
mrbob -w $VIRTUAL_ENV/share/skels/basic-project
mrbob --config .mrbob.ini -w $VIRTUAL_ENV/share/skels/flask-diamond-app
