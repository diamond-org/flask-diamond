# -*- coding: utf-8 -*-

from nose.plugins.attrib import attr
import os, shutil, tempfile, sys

from flask_diamond.utils.testhelpers import GeneralTestCase

class flask_diamond_ViewTestCase(GeneralTestCase):
    def test_login(self):
        rv = self.client.get('/login')
        assert 'Flask-Diamond' in rv.data

    def test_index(self):
        rv = self.client.get('/', follow_redirects=True)
        assert 'Flask-Diamond' in rv.data
