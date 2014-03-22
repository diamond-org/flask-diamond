# -*- coding: utf-8 -*-

# https://stackoverflow.com/questions/2257441/python-random-string-generation-with-upper-case-letters-and-digits
import string, random
def id_generator(size=8, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

# http://stackoverflow.com/questions/6027558/flatten-nested-python-dictionaries-compressing-keys
import collections
def flatten(d, parent_key=''):
    items = []
    for k, v in d.items():
        new_key = parent_key + '.' + str(k) if parent_key else str(k)
        if isinstance(v, collections.MutableMapping):
            items.extend(flatten(v, new_key).items())
        elif isinstance(v, collections.MutableSequence):
            array_as_dict = dict(zip(range(0, len(v)), v))
            items.extend(flatten(array_as_dict, new_key).items())
        else:
            items.append((new_key, v))
    return dict(items)

from flask.ext.security.utils import encrypt_password
from .. import db
def create_user(security, db, email, password):
    u = security.datastore.create_user(email=email, password=encrypt_password(password))
    db.session.commit()
    return u

def add_system_users(security):
    "Create a basic set of users and roles"
    admin_user = create_user(security, db, email="admin", password="aaa")
    guest_user = create_user(security, db, email="guest", password="guest")

    # make roles
    admin_role = security.datastore.find_or_create_role("Admin")
    user_role = security.datastore.find_or_create_role("User")

    # add roles to users
    security.datastore.add_role_to_user(admin_user, admin_role)
    security.datastore.add_role_to_user(guest_user, user_role)
    db.session.commit()

def rm_system_users(security):
    "remove default system users"
    security.datastore.delete_user(email="admin")
    security.datastore.delete_user(email="guest")
    db.session.commit()

def _u(obj, default=None):
    "ensure an object is Unicode"
    if type(obj) == str:
        try:
            obj = unicode(obj)
        except UnicodeDecodeError:
            obj = unicode(obj.decode("latin1"))
        return obj
    elif type(obj) == unicode:
        return obj
    else:
        return default

