# -*- coding: utf-8 -*-
# Flask-Diamond (c) Ian Dennis Miller

from .. import models


def typical_workflow():
    "create some example objects"

    a_user = models.User.register(
        email='iandennismiller@gmail.com',
        password='iandennismiller@gmail.com',
        confirmed=True,
        roles=["User"],
    )
