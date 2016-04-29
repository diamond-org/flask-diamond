#!/bin/bash
# Flask-Diamond (c) Ian Dennis Miller

# usage:
# Run diamond-scaffold.sh in the target project directory.
# It will create a minimal app.

echo "Scan environment"
rm -f /tmp/mrbob.ini
echo "[defaults]" > /tmp/mrbob.ini
echo "home_directory = ${HOME}" >> /tmp/mrbob.ini
echo "secret = $(python -c 'import os; print(repr(os.urandom(24)).replace("%", "%%"))' )" >> /tmp/mrbob.ini
echo "hash_salt = $(python -c 'import string as s, random as r; print(repr("".join(r.choice(s.ascii_letters+s.digits) for _ in range(16))))')" >> /tmp/mrbob.ini
echo "simple_password = $(python -c 'import string as s, random as r; print(repr("".join(r.choice(s.ascii_lowercase) for _ in range(3))))')" >> /tmp/mrbob.ini
echo "OK"

echo "Apply Flask-Diamond Scaffold"
mrbob -w --config /tmp/mrbob.ini -O "$1" $VIRTUAL_ENV/share/skels/flask-diamond-app

echo "Cleaning up..."
rm /tmp/mrbob.ini
