# -*- coding: utf-8 -*-

import logging, os, json
from .. import db

# adapted from https://github.com/semirook/flask-kit/blob/master/base/models.py
class CRUDMixin(object):
    __table_args__ = {'extend_existing': True}

    @classmethod
    def find(cls, **kwargs):
        return cls.query.filter_by(**kwargs).first()

    @classmethod
    def find_or_create(cls, **kwargs):
        obj = cls.find(**kwargs)
        if not obj:
            obj = cls.create(**kwargs)
        return obj

    @classmethod
    def get_by_id(cls, id):
        if any(
            (isinstance(id, basestring) and id.isdigit(),
             isinstance(id, (int, float))),
        ):
            return cls.query.get(int(id))
        return None

    @classmethod
    def create(cls, _commit=True, **kwargs):
        instance = cls(**kwargs)
        result = instance.save(_commit)
        logging.getLogger("flask-diamond").debug("create %r: %r" % (instance, result))
        return result

    def update(self, commit=True, **kwargs):
        for attr, value in kwargs.iteritems():
            setattr(self, attr, value)
        return commit and self.save() or self

    def save(self, commit=True):
        db.session.add(self)
        if commit:
            db.session.commit()
        return self

    def delete(self, commit=True):
        db.session.delete(self)
        return commit and db.session.commit()

class ImportExportMixin(object):
    @classmethod
    def save_all(cls, dest_dir):
        "save all objs as JSON files"
        for obj in cls.query.all():
            filename = os.path.join(dest_dir, "%s-%s.json" % (cls.__name__, obj.id))
            obj.save_file(filename)

    def save_file(self, filename):
        "save an object as a file"
        with open(filename, "w") as f:
            json.dump(self.as_hash(), f, indent=4, sort_keys=True)
        logging.info("exported %r" % self)

    @classmethod
    def load_all(cls, src_dir):
        "import all files in a target path as model objects"
        import operator
        unsorted_filenames = glob.glob(os.path.join(src_dir, "*.json"))
        sortable_pairs = [[int(os.path.splitext(os.path.basename(f))[0]), f] for f in unsorted_filenames]
        sorted_filenames = sorted(sortable_pairs, key=operator.itemgetter(0))
        for seq, filename in sorted_filenames:
            cls.load_file(filename)

    @classmethod
    def load_file(cls, filename):
        "load a JSON file as model object"
        with open(filename, "r") as f:
            obj_hash = json.load(f)
            instance = cls.from_hash(obj_hash)
            logging.info("imported %r" % instance)
            return instance
