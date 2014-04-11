# -*- coding: utf-8 -*-

import flask
import flask.ext.security as security
from flask.ext.admin import Admin, BaseView, expose, AdminIndexView
from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.admin.base import MenuLink
from flask_diamond import db, models as Models

class AuthMixin(object):
    def is_accessible(self):
        return security.current_user.is_authenticated()

class AdminMixin(object):
    def is_accessible(self):
        return security.current_user.has_role("Admin")

class AuthView(AuthMixin, BaseView):
    pass

class AdminView(AdminMixin, BaseView):
    pass

class AuthModelView(AuthMixin, ModelView):
    pass

class AdminModelView(AdminMixin, ModelView):
    pass

class AuthenticatedMenuLink(AuthMixin, MenuLink):
    pass

class UserView(AdminModelView):
    column_filters = ['email']
    column_exclude_list = ('password', 'active', '_password', 'confirmed_at')
    column_searchable_list = ('email', 'password')

class ForceLoginView(AdminIndexView):
    def is_accessible(self):
        return security.current_user.is_authenticated()

    @expose('/')
    def index(self):
        return self.render("/admin/index.html")
