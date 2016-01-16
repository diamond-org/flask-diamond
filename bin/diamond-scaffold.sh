#!/bin/bash

# usage:
# Run diamond-scaffold.sh in the target project directory.
# It will create a minimal app.

echo "Scan environment"
rm -f /tmp/mrbob.ini
echo "[variables]" > /tmp/mrbob.ini
echo "home_directory = ${HOME}" >> /tmp/mrbob.ini
echo "secret_key = `python -c 'import os; print(repr(os.urandom(24)))'`"  >> /tmp/mrbob.ini
echo "hash_salt = `python -c 'import string as s, random as r; print repr("".join(r.choice(s.letters+s.digits) for _ in range(16)))'`"  >> /tmp/mrbob.ini
echo "OK"

echo "Apply Flask-Diamond Scaffold"
mrbob --config /tmp/mrbob.ini $VIRTUAL_ENV/share/skels/flask-diamond-app

echo "Cleaning up..."
rm /tmp/mrbob.ini
