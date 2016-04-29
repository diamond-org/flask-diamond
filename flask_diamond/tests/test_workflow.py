# -*- coding: utf-8 -*-
# Flask-Diamond (c) Ian Dennis Miller

from nose.plugins.attrib import attr
from ..mixins.testing import DiamondTestCase
from ..models.user import User
from ..models.role import Role
from .fixtures import typical_workflow


class WorkflowTestCase(DiamondTestCase):
    def setUp(self):
        super(WorkflowTestCase, self).setUp()
        typical_workflow()

    @attr("single")
    def test_user(self):
        "user created in workflow"
        Role.add_default_roles()
        User.add_guest_user()

        u = User.find(email='guest')
        assert u
        assert u.email == 'guest'
