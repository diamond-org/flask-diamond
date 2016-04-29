# -*- coding: utf-8 -*-
# Flask-Diamond (c) Ian Dennis Miller

from nose.plugins.attrib import attr
from ..models.user import User
from .mixins import DiamondTestCase


class UserTestCase(DiamondTestCase):
    "Coverage for User Model"

    def test_create(self):
        "ensure an account can be created"
        User.create(email='an_account', password='a_password')
        an_account = User.find(email='an_account')
        assert an_account
        assert an_account.email == 'an_account'
