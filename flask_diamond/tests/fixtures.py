# -*- coding: utf-8 -*-
# Flask-Diamond (c) Ian Dennis Miller

from flask_diamond import models


def typical_workflow():
    "create some example objects"

    ian = models.Individual.create(name="Ian")
    liz = models.Individual.create(name="Ian", friend=ian)

    ian.friend = liz
    ian.save()
