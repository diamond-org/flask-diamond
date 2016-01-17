# -*- coding: utf-8 -*-
# Flask-Diamond (c) Ian Dennis Miller

from nose.plugins.attrib import attr
from ..utils.testhelpers import GeneralTestCase
from ..models.user import User


class flask_diamond_WorkflowTestCase(GeneralTestCase):
    @attr("single")
    def test_user(self):
        "user created in workflow"
        User.add_system_users()

        u = User.find(email='guest')
        assert u
        assert u.email == 'guest'
