# -*- coding: utf-8 -*-

import string
import random
import collections


# https://stackoverflow.com/questions/2257441/python-random-string-generation-with-upper-case-letters-and-digits
def id_generator(size=8, chars=None):
    """
    Create a random sequence of letters and numbers.

    :param size: the desired length of the sequence
    :type size: integer
    :param chars: the eligible character set to draw from when picking random characters
    :type chars: string
    :returns: a string with the random sequence
    """
    if chars is None:
        chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for x in range(size))


# http://stackoverflow.com/questions/6027558/flatten-nested-python-dictionaries-compressing-keys
def flatten(d, parent_key=''):
    """
    Flatten nested python dictionaries by compressing keys

    :param d: the hierarchical dictionary to flatten
    :type d: dict
    :param parent_key: a prefix to apply to new keys (may be '')
    :type parent_key: string
    """

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
