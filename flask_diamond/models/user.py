# -*- coding: utf-8 -*-

import flask
import datetime
from flask.ext.security import UserMixin
from flask.ext.security.utils import encrypt_password
from flask.ext.marshmallow.fields import fields
from .. import db
from .. import ma
from ..mixins.crud import CRUDMixin
from ..mixins.marshmallow import MarshmallowMixin

roles_users = db.Table('roles_users',
    db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))
"A secondary table is used for the one-to-many relationship: User has many Roles"


class UserSchema(ma.Schema):
    confirmed_at = fields.DateTime(required=False)
    last_login_at = fields.DateTime(required=False)
    current_login_at = fields.DateTime(required=False)

    # RoleSchema must be specified in role.py
    roles = fields.Nested('RoleSchema', allow_none=True, many=True)

    class Meta:
        dateformat = ("%F %T %z")
        additional = (
            "id",
            "name",
            "email",
            "password",
            "active",
            "last_login_ip",
            "current_login_ip",
            "login_count",
        )


class User(db.Model, UserMixin, CRUDMixin, MarshmallowMixin):
    __schema__ = UserSchema

    id = db.Column(db.Integer, primary_key=True)
    "integer -- primary key"

    name = db.Column(db.String(255), unique=True)
    "string -- user name"

    email = db.Column(db.String(255), unique=True)
    "string -- email address"

    password = db.Column('password', db.String(255), nullable=False)
    "password -- the users's password"

    active = db.Column(db.Boolean())
    "boolean -- whether the user account is active"

    confirmed_at = db.Column(db.DateTime())
    "datetime -- when the user account was confirmed"

    last_login_at = db.Column(db.DateTime())
    "datetime -- the time of the most recent login"

    current_login_at = db.Column(db.DateTime())
    "datetime -- the time of the current login, if any"

    last_login_ip = db.Column(db.String(255))
    "string -- the IP address of the previous login"

    current_login_ip = db.Column(db.String(255))
    "string -- the IP address of the current login"

    login_count = db.Column(db.Integer(), default=0)
    "integer -- the number of times this account been accessed"

    roles = db.relationship('Role',
        enable_typechecks=False,
        secondary=roles_users,
        # backref=db.backref('users', lazy='dynamic'),
    )

    def __str__(self):
        return self.email

    def confirm(self):
        """
        update a User account so that login is permitted

        :returns: None
        """

        self.confirmed_at = datetime.datetime.now()
        self.active = True
        self.save()

    def add_role(self, role_name):
        """
        update a User account so that it includes a new Role

        :param role_name: the name of the Role to add
        :type role_name: string
        """

        from .. import security

        new_role = security.Security.user_datastore.find_or_create_role(role_name)
        security.Security.user_datastore.add_role_to_user(self, new_role)
        db.session.commit()

    @classmethod
    def register(cls, name, email, password, confirmed=False, roles=None):
        """
        Create a new user account.

        :param name: the name of the account
        :type name: string
        :param email: the email address used to identify the account
        :type email: string
        :param password: the plaintext password for the account
        :type password: string
        :param confirmed: whether to confirm the account immediately
        :type confirmed: boolean
        :param roles: a list containing the names of the Roles for this User
        :type roles: list(string)
        """

        from .. import security

        new_user = security.Security.user_datastore.create_user(
            name=name,
            email=email,
            password=encrypt_password(password)
        )
        db.session.commit()
        if confirmed:
            new_user.confirm()
        if roles:
            for role_name in roles:
                new_user.add_role(role_name)
        flask.current_app.logger.debug("Created user {0}".format(email))
        return new_user

    @classmethod
    def add_guest_user(cls, name="guest", email="guest@example.com", password="guest"):
        cls.register(
            name=name,
            email=email,
            password=password,
            confirmed=True,
            roles=["User"]
        )

    @classmethod
    def add_admin_user(cls, name="admin", email="admin@example.com", password="aaa"):
        cls.register(
            name=name,
            email=email,
            password=password,
            confirmed=True,
            roles=["Admin"]
        )

    @classmethod
    def rm_system_users(cls):
        """
        remove default system users

        :returns: None
        """

        from .. import security

        security.Security.user_datastore.delete_user(name="admin")
        security.Security.user_datastore.delete_user(name="guest")
        db.session.commit()
