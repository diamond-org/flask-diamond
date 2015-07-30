Welcome to Flask-Diamond's documentation!
=========================================

Flask-Diamond provides a path that can guide your thought and development; Flask-Diamond is the road that leads to other ideas.

.. image:: https://readthedocs.org/projects/flask-diamond/badge/?version=latest
    :target: http://flask-diamond.readthedocs.org/

.. image:: https://img.shields.io/pypi/v/Flask-Diamond.svg
    :target: https://pypi.python.org/pypi/Flask-Diamond/

.. image:: https://img.shields.io/github/issues/iandennismiller/flask-diamond.svg
    :target: https://github.com/iandennismiller/flask-diamond/issues

Description
-----------

Flask-Diamond is a python Flask application platform that roughly approximates a django.  Flask-Diamond imports many other Flask libraries, and then glues them all together with sensible defaults.  The end result is a model administration view, accounts and high-level account operations (e.g. password reset), testing, documentation, project management (e.g. deployment), and more.

Installation
------------

::

    pip install Flask-Diamond

Introduction
============

.. toctree::

    quick_start
    system_requirements

API
===

.. toctree::

    api/flask_diamond
    api/flask_diamond.administration
    api/flask_diamond.models.user
    api/flask_diamond.models.role
    api/flask_diamond.utils
    api/flask_diamond.utils.mixins
    api/flask_diamond.utils.testhelpers
    api/flask_diamond.utils.wtfhelpers
