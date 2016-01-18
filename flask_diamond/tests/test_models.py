# -*- coding: utf-8 -*-
# Flask-Diamond (c) Ian Dennis Miller

from nose.plugins.attrib import attr

from flask.ext.diamond.utils.testhelpers import GeneralTestCase
from flask_diamond import models, create_app, db


class UserTestCase(GeneralTestCase):
    "Coverage for User Model"

    def test_create(self):
        "ensure an account can be created"
        models.User.create(email='an_account', password='a_password')
        an_account = models.User.find(email='an_account')
        assert an_account
        assert an_account.email == 'an_account'
