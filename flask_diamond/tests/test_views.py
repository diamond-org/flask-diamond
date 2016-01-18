# -*- coding: utf-8 -*-
# Flask-Diamond (c) Ian Dennis Miller

from nose.plugins.attrib import attr
from flask.ext.testing import TestCase
from flask.ext.diamond.mixins.testing import DiamondTestCaseMixin


class ViewTestCase(DiamondTestCaseMixin, TestCase):
    def test_login(self):
        rv = self.client.get('/user/login')
        assert 'Flask-Diamond' in rv.data

    def test_index(self):
        rv = self.client.get('/', follow_redirects=True)
        assert 'Flask-Diamond' in rv.data
