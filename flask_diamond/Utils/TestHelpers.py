# -*- coding: utf-8 -*-

from flask.ext.testing import TestCase
from flask import current_app

class GeneralTestCase(TestCase):
    def create_app(self):
        from flask_diamond import create_app, db
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['WTF_CSRF_ENABLED'] = False
        self.db = db
        return self.app

    def setUp(self):
        from flask_diamond import Models, security
        from flask_diamond.Utils import add_system_users
        self.db.drop_all()
        self.db.create_all()
        add_system_users(security)

    def tearDown(self):
        self.db.session.remove()
        self.db.drop_all()
