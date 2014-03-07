# -*- coding: utf-8 -*-

import json, os, logging, string, random
from flask.ext.security import UserMixin, RoleMixin, login_required
from flask.ext.security.utils import encrypt_password
from sqlalchemy_utils import ChoiceType
from . import db, security
from .Utils.Mixins import CRUDMixin
from .Utils import id_generator, flatten

roles_users = db.Table('roles_users',
    db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def __str__(self):
        return self.name

class User(db.Model, UserMixin, CRUDMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column('password', db.String(255), nullable=False)
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))

    def __str__(self):
        return self.email

    @classmethod
    def create(cls, email, password):
        result = security.datastore.create_user(email=email, password=encrypt_password(password))
        db.session.commit()
        return result
