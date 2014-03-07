#!/usr/bin/env python
# -*- coding: utf-8 -*-

import flask_diamond, logging
app = flask_diamond.create_app()
logging.getLogger("Flask-Diamond").info("runserver.py starting")
app.run(port=app.config['PORT'])
