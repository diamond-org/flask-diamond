# -*- coding: utf-8 -*-
# Flask-Diamond (c) Ian Dennis Miller

import flask

diamond_blueprint = flask.Blueprint(
    'diamond_blueprint',
    __name__,
    static_folder='static',
    template_folder='templates',
    static_url_path='/static/diamond',
)
