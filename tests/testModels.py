# -*- coding: utf-8 -*-

from nose.plugins.attrib import attr
import os, shutil, tempfile, sys

from flask_diamond import security, models as Models
from flask_diamond.utils.testhelpers import GeneralTestCase

class flask_diamond_ModelTestCase(GeneralTestCase):
    def setUp(self):
        self.db.drop_all()
        self.db.create_all()
        # do not create default items here; i.e. only drop and create tables

    @attr("single")
    def test_user(self):
        ian = Models.User.create(email='ian', password='ian')
        ian = Models.User.find(email='ian')
        assert ian
        assert ian.email == 'ian'
