# -*- coding: utf-8 -*-
# Flask-Diamond (c) Ian Dennis Miller

from nose.plugins.attrib import attr
# from .. import db
from .mixins import DiamondTestCase
from .fixtures import Planet, Satellite


class MarshmallowMixinTestCase(DiamondTestCase):
    "Coverage for CRUD Mixin"

    def setUp(self):
        super(DiamondTestCase, self).setUp()
        self.earth = Planet.create(name="Earth")
        self.moon = Satellite.create(name="Moon", planet=self.earth)

    @attr("skip")
    def test_dump(self):
        "test Marshmallow Mixin dump()"
        earth = Planet.find(name="Earth")
        result = earth.dumps()
        self.assertEqual(result, "{}")
