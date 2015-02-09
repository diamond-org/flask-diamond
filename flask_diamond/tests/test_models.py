# -*- coding: utf-8 -*-
# Flask-Diamond (c) Ian Dennis Miller

from nose.plugins.attrib import attr

from flask_diamond import models
from flask_diamond.utils.testhelpers import GeneralTestCase


class flask_diamond_ModelTestCase(GeneralTestCase):
    def setUp(self):
        self.db.drop_all()
        self.db.create_all()
        # do not create default items here; i.e. only drop and create tables

    @attr("single")
    def test_user(self):
        ian = models.User.create(email='ian', password='ian')
        ian = models.User.find(email='ian')
        assert ian
        assert ian.email == 'ian'
