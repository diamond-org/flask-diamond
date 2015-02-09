# -*- coding: utf-8 -*-
# Flask-Diamond (c) Ian Dennis Miller

from nose.plugins.attrib import attr
from flask_diamond import models
from flask_diamond.utils.testhelpers import GeneralTestCase


class flask_diamond_WorkflowTestCase(GeneralTestCase):
    @attr("single")
    def test_user(self):
        "user created in workflow"
        u = models.User.find(email='guest')
        assert u
        assert u.email == 'guest'
