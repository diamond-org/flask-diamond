# -*- coding: utf-8 -*-
# Flask-Diamond (c) Ian Dennis Miller


def init_configuration(self):
    """
    Load the application configuration from the ``SETTINGS`` environment variable.

    :returns: None

    ``SETTINGS`` must contain a filename that points to the configuration file.
    """

    self.app.config.from_envvar('SETTINGS')
