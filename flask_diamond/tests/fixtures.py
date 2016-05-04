# -*- coding: utf-8 -*-
# Flask-Diamond (c) Ian Dennis Miller

from .. import db
from ..models.user import User
from ..models.role import Role
from ..mixins.crud import CRUDMixin
from ..mixins.marshmallow import MarshmallowMixin


class Planet(db.Model, CRUDMixin, MarshmallowMixin):
    "A Planet is a celestial body"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    mass = db.Column(db.Float())


class Satellite(db.Model, CRUDMixin, MarshmallowMixin):
    "A Satellite orbits a Planet"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    mass = db.Column(db.Float())
    planet = db.relationship('Planet', backref=db.backref('satellites', lazy='dynamic'))
    planet_id = db.Column(db.Integer(), db.ForeignKey("planet.id"))


def typical_workflow():
    "create some example objects"
    Role.add_default_roles()
    User.add_guest_user()
    earth = Planet.create(name="Earth")
    Satellite.create(name="Moon", planet=earth)
