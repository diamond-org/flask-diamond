# -*- coding: utf-8 -*-
# Flask-Diamond (c) Ian Dennis Miller

from ..models.user import User
from ..models.role import Role


def typical_workflow():
    "create some example objects"

    Role.add_default_roles()
    User.add_guest_user()
