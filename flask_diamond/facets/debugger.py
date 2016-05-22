# -*- coding: utf-8 -*-
# Flask-Diamond (c) Ian Dennis Miller

from flask.ext.debugtoolbar import DebugToolbarExtension

toolbar = DebugToolbarExtension()


def init_debugger(self):
    """
    Initialize the DebugToolbar

    :returns: None

    The `DebugToolbar <http://flask-
    debugtoolbar.readthedocs.org/en/latest/>`_ is a handy utility for
    debugging your application during development.

    This function obeys the ``DEBUG_TOOLBAR`` configuration setting.  Only
    if this value is explicitly set to True will the Debug Toolbarr run.
    """

    if 'DEBUG_TOOLBAR' in self.app.config and self.app.config['DEBUG_TOOLBAR']:
        toolbar.init_app(self.app)
