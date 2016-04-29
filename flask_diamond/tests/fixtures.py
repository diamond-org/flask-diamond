# -*- coding: utf-8 -*-
# Flask-Diamond (c) Ian Dennis Miller

from ..models.user import User


def typical_workflow():
    "create some example objects"

    User.register(
        email='iandennismiller@gmail.com',
        password='iandennismiller@gmail.com',
        confirmed=True,
        roles=["User"],
    )
