# -*- coding: utf-8 -*-
# Flask-Diamond (c) Ian Dennis Miller

import logging


def init_logs(self):
    """
    Initialize a log file to collect messages.

    :returns: None

    This file may be written to using

    >>> flask.current_app.logger.info("message")
    """

    handler = logging.FileHandler(self.app.config['LOG'])
    handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s'))
    self.app.logger.addHandler(handler)
    if self.app.config.get("LOG_LEVEL") == "DEBUG":
        self.app.logger.setLevel(logging.DEBUG)
    elif self.app.config.get("LOG_LEVEL") == "WARN":
        self.app.logger.setLevel(logging.WARN)
    else:
        self.app.logger.setLevel(logging.INFO)
    self.app.logger.info('Startup with log: %s' % self.app.config['LOG'])
