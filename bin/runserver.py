#!/usr/bin/env python
# -*- coding: utf-8 -*-

import FlaskDiamond, logging
app = FlaskDiamond.create_app()
logging.getLogger("flask-diamond").info("runserver.py starting")
app.run(port=app.config['PORT'])
