# -*- coding: utf-8 -*-

from flask.ext.testing import TestCase

class GeneralTestCase(TestCase):
    def create_app(self):
        from FlaskDiamond import create_app, db
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['WTF_CSRF_ENABLED'] = False
        self.db = db
        return self.app

    def setUp(self):
        from FlaskDiamond import Models
        self.db.drop_all()
        self.db.create_all()
        Models.add_system_users()

    def tearDown(self):
        self.db.session.remove()
        self.db.drop_all()
