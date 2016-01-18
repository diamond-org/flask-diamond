# -*- coding: utf-8 -*-
# Flask-Diamond (c) Ian Dennis Miller

from nose.plugins.attrib import attr

from flask.ext.diamond.utils.testhelpers import GeneralTestCase


class flask_diamondBasicTestCase(GeneralTestCase):
    def test_basic(self):
        assert True

    @attr("skip")
    def test_skip(self):
        assert False
