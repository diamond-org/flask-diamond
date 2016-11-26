# -*- coding: utf-8 -*-
# Flask-Diamond (c) Ian Dennis Miller

from flask_marshmallow import Marshmallow

ma = Marshmallow()


def init_marshalling(self):
    """
    Initialize Marshmallow.

    :returns: None
    """

    ma.app = self.app
    ma.init_app(self.app)
