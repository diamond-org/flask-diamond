# -*- coding: utf-8 -*-

from nose.plugins.attrib import attr
import os, shutil, tempfile, sys

from flask_diamond.Utils import TestHelpers

class flask_diamondViewTestCase(TestHelpers.GeneralTestCase):
    def test_login(self):
        rv = self.client.get('/login')
        assert 'flask-diamond' in rv.data

    def test_index(self):
        rv = self.client.get('/', follow_redirects=True)
        assert 'flask-diamond' in rv.data
