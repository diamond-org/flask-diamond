# -*- coding: utf-8 -*-
# Flask-Diamond (c) Ian Dennis Miller

from .. import Diamond
from nose.plugins.attrib import attr
from unittest import TestCase


class MyDiamondApp(Diamond):
    def init_blueprints(self):
        self.super("blueprints")


def create_app():
    diamond = Diamond()
    diamond.facet("configuration")
    diamond.facet("logs")
    diamond.facet("database")
    diamond.facet("marshalling")
    diamond.facet("accounts")
    diamond.facet("blueprints")
    diamond.facet("signals")
    diamond.facet("forms")
    diamond.facet("error_handlers")
    diamond.facet("request_handlers")
    diamond.facet("administration")
    diamond.facet("rest")
    diamond.facet("webassets")
    diamond.facet("email")
    diamond.facet("debugger")
    diamond.facet("task_queue")
    return diamond.app


class BasicTestCase(TestCase):

    @attr("single")
    def test_create_app(self):
        from ..facets.database import db
        from ..models.role import Role
        from ..models.user import User

        app = create_app()
        with app.app_context():
            db.drop_all()
            try:
                db.create_all()

                Role.add_default_roles()

                User.register(
                    email="guest@example.com",
                    password="guest",
                    roles=["User"],
                )

                User.register(
                    email="admin@example.com",
                    password="abc",
                    roles=["Admin"],
                )

                self.assertIsNotNone(app, msg="create app")
            finally:
                db.drop_all()
