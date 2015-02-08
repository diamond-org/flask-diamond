#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Flask-Diamond (c) Ian Dennis Miller

from flask_diamond import create_app
app = create_app()
app.run(port=app.config['PORT'])
