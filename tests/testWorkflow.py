# -*- coding: utf-8 -*-

from nose.plugins.attrib import attr
import os, shutil, tempfile, sys

sys.path.insert(0, '.')
os.environ['SETTINGS'] = "../etc/testing.conf"

from FlaskDiamond import Models
from FlaskDiamond.Utils import TestHelpers

class FlaskDiamondWorkflowTestCase(TestHelpers.GeneralTestCase):
    @attr("single")
    def test_user(self):
        "user created in workflow"
        u = Models.User.find(email='guest')
        assert u
        assert u.email == 'guest'
