# -*- coding: utf-8 -*-

import flask
import flask.ext.security as security
from flask.ext.admin import Admin, BaseView, expose, AdminIndexView
from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.admin.base import MenuLink
from flask_diamond import db, models as Models

class AuthHelper(object):
    def is_accessible(self):
        return security.current_user.is_authenticated()

class AdminHelper(object):
    def is_accessible(self):
        return security.current_user.has_role("Admin")

class AuthView(BaseView, AuthHelper):
    pass

class AdminView(ModelView, AdminHelper):
    pass

class AuthModelView(ModelView, AuthHelper):
    pass

class AdminModelView(ModelView, AdminHelper):
    pass

class AuthenticatedMenuLink(MenuLink, AuthHelper):
    pass

class UserView(AdminView):
    column_filters = ['email']
    column_exclude_list = ('password', 'active', '_password', 'confirmed_at')
    column_searchable_list = ('email', 'password')

class ForceLoginView(AdminIndexView):
    def is_accessible(self):
        return security.current_user.is_authenticated()

    @expose('/')
    def index(self):
        # if user has User role, redirect them to the tree builder
        if security.current_user.has_role("User"):
            return flask.redirect("/")

        return self.render("/admin/index.html")
