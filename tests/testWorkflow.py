# -*- coding: utf-8 -*-

from nose.plugins.attrib import attr
import os, shutil, tempfile, sys

from flask_diamond import models as Models
from flask_diamond.utils.testhelpers import GeneralTestCase

class flask_diamond_WorkflowTestCase(GeneralTestCase):
    @attr("single")
    def test_user(self):
        "user created in workflow"
        u = Models.User.find(email='guest')
        assert u
        assert u.email == 'guest'
