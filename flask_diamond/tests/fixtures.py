# -*- coding: utf-8 -*-
# Flask-Diamond (c) Ian Dennis Miller

from flask.ext.marshmallow.fields import fields
from flask.ext.diamond import db, ma
from ..models.user import User
from ..models.role import Role
from ..mixins.crud import CRUDMixin
from ..mixins.marshmallow import MarshmallowMixin


class PlanetSchema(ma.Schema):
    satellites = fields.Nested('SatelliteSchema', allow_none=True, many=True)

    class Meta:
        additional = ("id", "name", "mass")


class SatelliteSchema(ma.Schema):
    class Meta:
        additional = ("id", "name")


class Planet(db.Model, CRUDMixin, MarshmallowMixin):
    "A Planet is a celestial body"
    __schema__ = PlanetSchema
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    mass = db.Column(db.Float())


class Satellite(db.Model, CRUDMixin, MarshmallowMixin):
    "A Satellite orbits a Planet"
    __schema__ = SatelliteSchema
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    mass = db.Column(db.Float())
    planet = db.relationship('Planet', backref=db.backref('satellites', lazy='dynamic'))
    planet_id = db.Column(db.Integer(), db.ForeignKey("planet.id"))


def typical_workflow():
    "instantiate the minimal viable product"

    # create user accounts
    Role.add_default_roles()
    User.add_guest_user()

    # create data for users to manage
    earth = Planet.create(name="Earth")
    Satellite.create(name="Moon", planet=earth)
