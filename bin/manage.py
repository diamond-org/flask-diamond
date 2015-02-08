#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Flask-Diamond (c) Ian Dennis Miller

import sys
import traceback
sys.path.insert(0, '.')

from flask.ext.script import Manager, Shell, Server
from flask.ext.migrate import Migrate, MigrateCommand
import alembic
import alembic.config

from flask_diamond import create_app, db, security
app = create_app()


def _make_context():
    return dict(app=app, db=db, user_datastore=security.datastore)

migrate = Migrate(app, db, directory="flask_diamond/migrations")

manager = Manager(app)
manager.add_command("shell", Shell(make_context=_make_context))
manager.add_command("runserver", Server(port=app.config['PORT']))
manager.add_command("publicserver", Server(port=app.config['PORT'], host="0.0.0.0"))
manager.add_command('db', MigrateCommand)


@manager.option('-e', '--email', help='email address')
@manager.option('-p', '--password', help='password')
def adduser(email, password):
    "add a user to the database"
    from flask_diamond import models
    models.User.create(email=email, password=password)


@manager.command
def init_db():
    "drop all databases, instantiate schemas"
    db.drop_all()
    db.create_all()
    db.session.commit()
    cfg = alembic.config.Config("flask_diamond/migrations/alembic.ini")
    alembic.command.stamp(cfg, "head")


@manager.command
def populate_db():
    "insert a default set of objects"
    from flask_diamond import add_system_users
    add_system_users(security)

if __name__ == "__main__":
    try:
        manager.run()
    except Exception, e:
        ex_type, ex, tb = sys.exc_info()
        traceback.print_tb(tb)
        print "Error: %s" % e
        print "Line: %d" % sys.exc_traceback.tb_lineno
