# -*- coding: utf-8 -*-

import flask.ext.security as security
from flask.ext.admin import BaseView, expose, AdminIndexView
from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.admin.base import MenuLink
from flask.ext.security.utils import encrypt_password
import flask


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
    column_exclude_list = ('password', 'active', 'confirmed_at')
    column_searchable_list = ('email', )
    can_delete = False

    create_template = 'admin/create_user.html'

    def create_model(self, form):
        self.model.register(
            email=form.data["email"],
            password=form.data["password"],
            confirmed=True,
            roles=["User"],
        )
        return flask.redirect(flask.url_for("user.index_view"))

    def update_model(self, form, model):
        original_password = model.password
        model.update(**form.data)
        if form.data["password"] != original_password:
            model.password = encrypt_password(form.data["password"])
            model.save()
        return flask.redirect(flask.url_for("user.index_view"))


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
