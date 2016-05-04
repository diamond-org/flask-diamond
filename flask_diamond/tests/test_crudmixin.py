# -*- coding: utf-8 -*-
# Flask-Diamond (c) Ian Dennis Miller

from nose.plugins.attrib import attr
from .. import db
from ..mixins.crud import CRUDMixin
from ..mixins.marshmallow import MarshmallowMixin
from .mixins import DiamondTestCase


class Planet(db.Model, CRUDMixin, MarshmallowMixin):
    "A Planet is a celestial body"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    mass = db.Column(db.Float())


class CRUDMixinTestCase(DiamondTestCase):
    "Coverage for CRUD Mixin"

    def test_create(self):
        "test CRUDMixin Create and Read"
        earth = Planet.create(name="Earth")
        self.assertIsNotNone(earth)

    def test_find(self):
        "test CRUDMixin find"
        Planet.create(name="Earth")
        a_planet = Planet.find(name='Earth')
        self.assertIsNotNone(a_planet)
        self.assertEqual(a_planet.name, 'Earth')

    @attr("single")
    def test_get_by_id(self):
        "test CRUDMixin get_by_id"
        Planet.create(name="Earth")
        a_planet = Planet.get_by_id(1)
        self.assertIsNotNone(a_planet)
        self.assertEqual(a_planet.name, 'Earth')

    def test_update(self):
        "test CRUDMixin Update"
        earth = Planet.create(name="Earth")

        # set the mass of Earth
        earth_mass_kg = float(5.972*10**24)
        earth.update(mass=earth_mass_kg)

        # retrieve it from the db again
        a_planet = Planet.find(name='Earth')
        self.assertEqual(a_planet.mass, earth_mass_kg)

    def test_delete(self):
        "test CRUDMixin Delete"
        # create and immediately delete the object
        earth = Planet.create(name="Earth")
        earth.delete()

        # attempt to retrieve it and verify that it fails
        a_planet = Planet.find(name='Earth')
        self.assertIsNone(a_planet)

    @attr("skip")
    def test_create_commit_false(self):
        "ensure database commits can be deferred"
        Planet.create(name="Earth", _commit=False)

        a_planet = Planet.get_by_id(1)
        print(a_planet)
        print(a_planet.name)
        # assert a_planet is None

        db.session.commit()

        a_planet = Planet.find(name='Earth')
        self.assertIsNotNone(a_planet)
