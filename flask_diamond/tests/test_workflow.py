# -*- coding: utf-8 -*-
# Flask-Diamond (c) Ian Dennis Miller

from nose.plugins.attrib import attr
from flask.ext.testing import TestCase
from flask.ext.diamond.mixins.testing import DiamondTestCaseMixin
from ..models.user import User
from .fixtures import typical_workflow


class WorkflowTestCase(DiamondTestCaseMixin, TestCase):
    def setUp(self):
        super(WorkflowTestCase, self).setUp()
        typical_workflow()

    @attr("single")
    def test_user(self):
        "user created in workflow"
        User.add_system_users()

        u = User.find(email='guest')
        assert u
        assert u.email == 'guest'
