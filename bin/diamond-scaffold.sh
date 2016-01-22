#!/bin/bash

# usage:
# Run diamond-scaffold.sh in the target project directory.
# It will create a minimal app.

# start with a fresh environment
rm -rf /tmp/diamond-project /tmp/diamond-app

# apply the two diamond skeletons
mrbob -w $VIRTUAL_ENV/share/skels/diamond-project/skel
mrbob --config .mrbob.ini $VIRTUAL_ENV/share/skels/diamond-app/skel
