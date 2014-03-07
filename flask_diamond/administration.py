# -*- coding: utf-8 -*-

import flask
import flask.ext.security as security
from flask.ext.admin import Admin, BaseView, expose, AdminIndexView
from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.admin.base import MenuLink
from flask_diamond import db, models as Models

class AdminView(ModelView):
    def is_accessible(self):
        return security.current_user.has_role("Admin")

class AuthenticatedMenuLink(MenuLink):
    def is_accessible(self):
        return security.current_user.is_authenticated()

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
            return flask.redirect("/history")

        return self.render("/admin/index.html")
