# -*- coding: utf-8 -*-
# Flask-Diamond (c) Ian Dennis Miller

from nose.plugins.attrib import attr

from flask_diamond import models
from flask_diamond.utils.testhelpers import GeneralTestCase


class flask_diamond_ModelTestCase(GeneralTestCase):

    @attr("single")
    def test_user(self):
        ian = models.user.User.create(email='ian', password='ian')
        ian = models.user.User.find(email='ian')
        assert ian
        assert ian.email == 'ian'
