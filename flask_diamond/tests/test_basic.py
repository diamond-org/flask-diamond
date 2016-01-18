# -*- coding: utf-8 -*-
# Flask-Diamond (c) Ian Dennis Miller

from nose.plugins.attrib import attr
from flask.ext.testing import TestCase
from flask.ext.diamond.mixins.testing import DiamondTestCaseMixin


class BasicTestCase(DiamondTestCaseMixin, TestCase):
    def test_basic(self):
        "ensure the minimum test works"
        assert True

    @attr("skip")
    def test_skip(self):
        assert False
