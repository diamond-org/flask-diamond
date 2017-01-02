Tutorial: Planets
=================

The Planets Tutorial will introduce Flask-Diamond by demonstrating a simple web application that manages Planets and Satellites in a database.
This tutorial assumes you have already installed the :doc:`system_requirements`.

The Planets Tutorial consists of two parts:

1. This document, which contains instructions and explanations
2. The Planets code scaffold, which is available from the command line


The following commands will prepare you to begin the tutorial:

::

    mkdir planets
    cd planets
    mkvirtualenv -a . planets
    pip install Flask-Diamond
    flask-diamond scaffold app
    flask-diamond scaffold tutorial-planets

When you run ``flask-diamond scaffold app``, you will be prompted to answer some questions.
You can accept the default answers by pressing Enter for each question.

