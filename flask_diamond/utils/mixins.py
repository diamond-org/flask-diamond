# -*- coding: utf-8 -*-

import os
import json
import glob
import flask
from .. import db


class CRUDMixin(object):
    """
    Convenience functions for CRUD operations.

    Adapted from `flask-kit <https://github.com/semirook/flask-kit/blob/master/base/models.py>`_.
    """

    __table_args__ = {'extend_existing': True}

    @classmethod
    def find(cls, **kwargs):
        """
        Find an object in the database with certain properties.

        :param kwargs: the values of the object to find
        :type kwargs: dict
        :returns: the object that was found, or else None
        """

        return cls.query.filter_by(**kwargs).first()

    @classmethod
    def find_or_create(cls, _commit=True, **kwargs):
        """
        Find an object or, if it does not exist, create it.

        :param kwargs: the values of the object to find or create
        :type kwargs: dict
        :returns: the object that was created
        """

        obj = cls.find(**kwargs)
        if not obj:
            obj = cls.create(_commit=_commit, **kwargs)
        return obj

    @classmethod
    def get_by_id(cls, id):
        """
        Retrieve an object of this class from the database.

        :param id: the id of the object to be retrieved
        :type id: integer
        :returns: the object that was retrieved
        """

        if any(
            (isinstance(id, basestring) and id.isdigit(),
             isinstance(id, (int, float))),
        ):
            return cls.query.get(int(id))
        return None

    @classmethod
    def create(cls, _commit=True, **kwargs):
        """
        Create a new object.

        :param commit: whether to commit the change immediately to the database
        :type commit: boolean
        :param kwargs: parameters corresponding to the new values
        :type kwargs: dict
        :returns: the object that was created
        """

        instance = cls(**kwargs)
        obj = instance.save(_commit)
        flask.current_app.logger.debug("create %s" % unicode(obj))
        return obj

    def update(self, _commit=True, **kwargs):
        """
        Update this object with new values.

        :param commit: whether to commit the change immediately to the database
        :type commit: boolean
        :param kwargs: parameters corresponding to the new values
        :type kwargs: dict
        :returns: the object that was updated
        """

        for attr, value in kwargs.iteritems():
            setattr(self, attr, value)
        return _commit and self.save() or self

    def save(self, _commit=True):
        """
        Save this object to the database.

        :param commit: whether to commit the change immediately to the database
        :type commit: boolean
        :returns: the object that was saved
        """

        db.session.add(self)
        if _commit:
            db.session.commit()
        return self

    def delete(self, _commit=True):
        """
        Delete this object.

        :param commit: whether to commit the change immediately to the database
        :type commit: boolean
        :returns: whether the delete was successful
        """

        db.session.delete(self)
        return _commit and db.session.commit()

    def __repr__(self):
        return "<{}(id={})>".format(self.__class__.__name__, self.id)

    def __str__(self):
        return self.__repr__()

    def __unicode__(self):
        return self.__repr__()


class ImportExportMixin(object):
    @classmethod
    def save_all(cls, dest_dir):
        """
        save all objs as JSON files
        """

        for obj in cls.query.all():
            filename = os.path.join(dest_dir, "%s-%s.json" % (cls.__name__, obj.id))
            obj.save_file(filename)

    def save_file(self, filename):
        """
        save an object as a file
        """

        with open(filename, "w") as f:
            json.dump(self.as_hash(), f, indent=4, sort_keys=True)
        flask.current_app.logger.info("exported %r" % self)

    @classmethod
    def load_all(cls, src_dir):
        """
        import all files in a target path as model objects
        """

        import operator
        unsorted_filenames = glob.glob(os.path.join(src_dir, "*.json"))
        sortable_pairs = [
            [
                int(os.path.splitext(os.path.basename(f))[0]), f
            ] for f in unsorted_filenames
        ]
        sorted_filenames = sorted(sortable_pairs, key=operator.itemgetter(0))
        for seq, filename in sorted_filenames:
            cls.load_file(filename)

    @classmethod
    def load_file(cls, filename):
        """
        load a JSON file as model object
        """
        with open(filename, "r") as f:
            obj_hash = json.load(f)
            instance = cls.from_hash(obj_hash)
            flask.current_app.logger.info("imported %r" % instance)
            return instance


class MarshmallowMixin(object):

    # dump

    def dump(self):
        "serialize the Model object as a python object"
        return self.__schema__().dump(self).data

    def dumps(self):
        "serialize the Model object as a JSON string"
        return self.__schema__().dumps(self).data

    def dumpf(self, file_handle):
        "write a Model object to file_handle as a JSON string"
        file_handle.write(self.dumps())

    # load

    @classmethod
    def load(cls, python_obj):
        "create a Model object from a python object"
        obj = cls.__schema__().load(python_obj)
        return cls.create(**obj.data)

    @classmethod
    def loads(cls, buf):
        "create a Model object from a JSON-encoded string"
        obj = cls.__schema__().loads(buf)
        return cls.create(**obj.data)

    @classmethod
    def loadf(cls, file_handle):
        "create a Model object from a file_handle pointing to a JSON file"
        return cls.loads(file_handle.read())

    # dump_all

    @classmethod
    def dump_all(cls):
        "write all objects of Model class to an array of python objects"
        return cls.__schema__().dump(cls.query.all(), many=True).data

    @classmethod
    def dumps_all(cls):
        "write all objects of Model class to a JSON-encoded array"
        return cls.__schema__().dumps(cls.query.all(), many=True).data

    @classmethod
    def dumpf_all(cls, file_handle):
        "write all objects of Model class to file_handle as JSON"
        file_handle.write(cls.dumps_all())

    # load_all

    @classmethod
    def load_all(cls, python_objects):
        "create objects of Model class from an array of python objects"
        objs = cls.__schema__().load(python_objects, many=True)
        for obj in objs.data:
            cls.create(**obj)

    @classmethod
    def loads_all(cls, buf):
        "create objects of Model class from a string containing an array of JSON-encoded objects"
        objs = cls.__schema__().loads(buf, many=True)
        for obj in objs.data:
            cls.create(**obj)

    @classmethod
    def loadf_all(cls, file_handle):
        "create objects of Model class from a file containing an array of JSON-encoded objects"
        cls.loads_all(file_handle.read())
