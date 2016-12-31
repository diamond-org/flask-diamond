# -*- coding: utf-8 -*-

from flask_security import RoleMixin
from ..facets.database import db
from ..facets.marshalling import ma
from ..mixins.crud import CRUDMixin
from ..mixins.marshmallow import MarshmallowMixin


class RoleSchema(ma.Schema):
    class Meta:
        additional = (
            "id",
            "name",
            "description",
        )


class Role(db.Model, RoleMixin, CRUDMixin, MarshmallowMixin):
    """
    For the purpose of access controls, Roles can be used to create
    collections of users and give them permissions as a group.
    """

    __schema__ = RoleSchema

    id = db.Column(db.Integer(), primary_key=True)
    "integer -- primary key"

    name = db.Column(db.String(80), unique=True)
    "string -- what the role is called"

    description = db.Column(db.String(255))
    "string -- a sentence describing the role"

    def __str__(self):
        return self.name

    @classmethod
    def add_default_roles(cls):
        """
        Create a basic set of users and roles

        :returns: None
        """

        from .. import security

        # make roles
        security.user_datastore.find_or_create_role("Admin")
        security.user_datastore.find_or_create_role("User")
        db.session.commit()
