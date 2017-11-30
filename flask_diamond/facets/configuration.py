# -*- coding: utf-8 -*-
# Flask-Diamond (c) Ian Dennis Miller

import os
import json


def init_configuration(self):
    """
    Load the application configuration from the ``SETTINGS`` environment variable.

    :returns: None

    ``SETTINGS`` must contain a filename that points to the configuration file.
    """
    if "SETTINGS" in os.environ and os.path.isfile(os.environ["SETTINGS"]):
        self.app.config.from_envvar('SETTINGS')
    elif "SETTINGS_JSON" in os.environ:
        h = json.loads(os.environ["SETTINGS_JSON"])
        self.app.config.update(**h)
