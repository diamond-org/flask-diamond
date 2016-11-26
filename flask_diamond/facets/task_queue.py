# -*- coding: utf-8 -*-
# Flask-Diamond (c) Ian Dennis Miller

from flask_celery import Celery

celery = Celery()


def init_task_queue(self):
    """
    Initialize celery.
    """

    celery.init_app(self.app)
