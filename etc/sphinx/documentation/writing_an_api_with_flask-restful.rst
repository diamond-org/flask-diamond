Writing an API with Flask-RESTful
=================================

This document is a work in progress.

MarshmallowMixin
----------------

``MarshmallowMixin`` simplifies object marshalling, which is the process of mapping data to and from a serialization format like JSON.  This is useful because applications must frequently send model data across the Internet, and in order to do so, models are commonly translated into JSON or another format.  Marshalling makes serialization and deserialization into a repeatable process.
