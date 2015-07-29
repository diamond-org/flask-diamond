# -*- coding: utf-8 -*-

from flask.ext.security import RoleMixin
#import flask.ext.security as security
from .. import db


class Role(db.Model, RoleMixin):
    """
    For the purpose of access controls, Roles can be used to create
    collections of users and give them permissions as a group.
    """

    id = db.Column(db.Integer(), primary_key=True)
    "integer -- primary key"

    name = db.Column(db.String(80), unique=True)
    "string -- what the role is called"

    description = db.Column(db.String(255))
    "string -- a sentence describing the role"

    def __str__(self):
        return self.name
