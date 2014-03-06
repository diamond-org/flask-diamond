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
