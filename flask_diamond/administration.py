# -*- coding: utf-8 -*-

import flask.ext.security as security
from flask.ext.admin import BaseView, expose, AdminIndexView
from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.admin.base import MenuLink


class AuthMixin(object):
    """
    Require user authentication to be accessible
    """

    def is_accessible(self):
        """
        the View is accessible if the User is authenticated
        """

        return security.current_user.is_authenticated()


class AdminMixin(object):
    """
    Require admin Role to be accessible
    """

    def is_accessible(self):
        """
        the View is accessible if the User has the Admin Role
        """

        return security.current_user.has_role("Admin")


class AuthView(AuthMixin, BaseView):
    """
    A View that requires authentication
    """
    pass


class AdminView(AdminMixin, BaseView):
    """
    A View that requires the Admin Role
    """
    pass


class AuthModelView(AuthMixin, ModelView):
    """
    A ModelView that requires authentication
    """
    pass


class AdminModelView(AdminMixin, ModelView):
    """
    A ModelView that requires the Admin Role
    """
    pass


class AuthenticatedMenuLink(AuthMixin, MenuLink):
    """
    A MenuLink that requires authentication
    """
    pass


class UserView(AdminModelView):
    """
    Manage the User Model
    """

    column_filters = ['email']
    column_exclude_list = ('password', 'active', '_password', 'confirmed_at')
    column_searchable_list = ('email', 'password')


class ForceLoginView(AdminIndexView):
    """
    Allocate the root URL and require authentication
    """

    def is_accessible(self):
        """
        the View is accessible if the User is authenticated
        """

        return security.current_user.is_authenticated()

    @expose('/')
    def index(self):
        return self.render("/admin/index.html")
