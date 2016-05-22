#!/bin/bash
# Flask-Diamond (c) Ian Dennis Miller

if [ -z "$1" ]; then
    echo "error: expected a target directory"
    echo "usage: diamond-scaffold-model.sh ~/target-project"
    exit
fi

echo "Scaffold a Flask-Diamond model"

if [ -f $1/.mrbob.ini ]; then
    mrbob -w --config "$1/.mrbob.ini" -O "$1" $VIRTUAL_ENV/share/skels/example-model
else
    echo "ERROR: $1/.mrbob.ini does not exist."
    echo "This must be run in the root directory of a Flask-Diamond application."
fi
