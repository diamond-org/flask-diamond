# -*- coding: utf-8 -*-

from nose.plugins.attrib import attr
import os, shutil, tempfile, sys

sys.path.insert(0, '.')
os.environ['SETTINGS'] = "../etc/testing.conf"

from flask_diamond import Models, security
from flask_diamond.Utils import TestHelpers

class ModelTestCase(TestHelpers.GeneralTestCase):
    def setUp(self):
        self.db.drop_all()
        self.db.create_all()
        # do not create default items here; i.e. only drop and create tables

class flask_diamondModelTestCase(ModelTestCase):
    def test_user(self):
        ian = Models.User.create(email='ian', password='ian')
        ian = Models.User.find(email='ian')
        assert ian
        assert ian.email == 'ian'
