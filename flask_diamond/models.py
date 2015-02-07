# -*- coding: utf-8 -*-

from flask.ext.security import UserMixin, RoleMixin
from flask.ext.security.utils import encrypt_password
from . import db, security
from .utils.mixins import CRUDMixin
import datetime

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

    last_login_at = db.Column(db.DateTime())
    current_login_at = db.Column(db.DateTime())
    last_login_ip = db.Column(db.String(255))
    current_login_ip = db.Column(db.String(255))
    login_count = db.Column(db.Integer(), default=0)

    roles = db.relationship('Role', secondary=roles_users,
        backref=db.backref('users', lazy='dynamic'))

    def __str__(self):
        return self.email

    def confirm(self):
        self.confirmed_at = datetime.datetime.now()
        self.active = True
        self.save()

    def add_role(self, role_name):
        new_role = security.datastore.find_or_create_role(role_name)
        security.datastore.add_role_to_user(self, new_role)
        db.session.commit()

    @classmethod
    def create(cls, email, password, confirmed=False, roles=None):
        new_user = security.datastore.create_user(
            email=email,
            password=encrypt_password(password)
        )
        db.session.commit()
        if confirmed:
            new_user.confirm()
        if roles:
            for role_name in roles:
                new_user.add_role(role_name)
        return new_user

    @classmethod
    def add_system_users(cls, security):
        "Create a basic set of users and roles"

        # make roles
        security.datastore.find_or_create_role("Admin")
        security.datastore.find_or_create_role("User")
        db.session.commit()

        User.create(
            email="admin",
            password="aaa",
            confirmed=True,
            roles=["Admin"]
        )

        User.create(
            email="guest",
            password="guest",
            confirmed=True,
            roles=["User"]
        )

        db.session.commit()

    @classmethod
    def rm_system_users(cls, security):
        "remove default system users"
        security.datastore.delete_user(email="admin")
        security.datastore.delete_user(email="guest")
        db.session.commit()
