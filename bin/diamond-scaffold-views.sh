#!/bin/bash
# Flask-Diamond (c) Ian Dennis Miller

if [ -z "$1" ]; then
    echo "error: expected a target directory"
    echo "usage: diamond-scaffold-views.sh ~/target-project"
    exit
fi

echo "Scaffold the default Flask-Diamond views"

if [ -f $1/.mrbob.ini ]; then
    mrbob -w --config "$1/.mrbob.ini" -O "$1" $VIRTUAL_ENV/share/skels/example-views
else
    echo "ERROR: $1/.mrbob.ini does not exist."
    echo "This must be run in the root directory of a Flask-Diamond application."
fi
