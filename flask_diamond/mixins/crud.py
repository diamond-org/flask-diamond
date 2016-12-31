# -*- coding: utf-8 -*-
# Flask-Diamond (c) Ian Dennis Miller

import flask
from builtins import str
from ..facets.database import db


class CRUDMixin:
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
            (isinstance(id, str) and id.isdigit(),
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
        flask.current_app.logger.debug("create %s" % str(obj))
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

        for attr, value in kwargs.items():
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
