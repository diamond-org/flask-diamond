# -*- coding: utf-8 -*-
# Flask-Diamond (c) Ian Dennis Miller

from nose.plugins.attrib import attr
from ..models.user import User
from .mixins import DiamondTestCase
from .fixtures import typical_workflow


class WorkflowTestCase(DiamondTestCase):
    def setUp(self):
        super(WorkflowTestCase, self).setUp()
        typical_workflow()

    @attr("single")
    def test_user(self):
        "user created in workflow"
        u = User.find(email='guest')
        assert u
        assert u.email == 'guest'
