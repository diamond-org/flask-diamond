# -*- coding: utf-8 -*-

import string
import random
import collections


# https://stackoverflow.com/questions/2257441/python-random-string-generation-with-upper-case-letters-and-digits
def id_generator(size=8, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


# http://stackoverflow.com/questions/6027558/flatten-nested-python-dictionaries-compressing-keys
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
