# -*- coding: utf-8 -*-

from wtforms.fields import HiddenField, BooleanField


def add_helpers(app):
    """
    Create any Jinja2 helpers needed.
    """

    def is_hidden_field_filter(field):
        return isinstance(field, HiddenField)

    def is_boolean_field_filter(field):
        return isinstance(field, BooleanField)

    app.jinja_env.filters['is_hidden_field'] = is_hidden_field_filter
    app.jinja_env.filters['is_boolean_field'] = is_boolean_field_filter
