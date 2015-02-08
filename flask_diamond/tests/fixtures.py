# -*- coding: utf-8 -*-
# Flask-Diamond (c) Ian Dennis Miller

from flask_diamond import models


def typical_workflow():
    "create some example objects"

    ian = models.User.register(
        email='ian',
        password='aaa',
        confirmed=True,
        roles=["User"],
    )
