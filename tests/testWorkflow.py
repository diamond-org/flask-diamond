# -*- coding: utf-8 -*-

from nose.plugins.attrib import attr
import os, shutil, tempfile, sys

from flask_diamond import Models
from flask_diamond.Utils import TestHelpers

class flask_diamondWorkflowTestCase(TestHelpers.GeneralTestCase):
    @attr("single")
    def test_user(self):
        "user created in workflow"
        u = Models.User.find(email='guest')
        assert u
        assert u.email == 'guest'
