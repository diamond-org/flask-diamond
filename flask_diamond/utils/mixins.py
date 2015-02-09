# -*- coding: utf-8 -*-

import os
import json
import glob
from .. import db
import flask


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
    def find_or_create(cls, **kwargs):
        """
        Find an object or, if it does not exist, create it.

        :param kwargs: the values of the object to find or create
        :type kwargs: dict
        :returns: the object that was created
        """

        obj = cls.find(**kwargs)
        if not obj:
            obj = cls.create(**kwargs)
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
        flask.current_app.logger.debug("create %r: %r" % (instance, obj))
        return obj

    def update(self, commit=True, **kwargs):
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
        return commit and self.save() or self

    def save(self, commit=True):
        """
        Save this object to the database.

        :param commit: whether to commit the change immediately to the database
        :type commit: boolean
        :returns: the object that was saved
        """

        db.session.add(self)
        if commit:
            db.session.commit()
        return self

    def delete(self, commit=True):
        """
        Delete this object.

        :param commit: whether to commit the change immediately to the database
        :type commit: boolean
        :returns: whether the delete was successful
        """

        db.session.delete(self)
        return commit and db.session.commit()


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
