Testing with Nose
=================

Writing tests is an important part of building an application.  Especially with dynamically typed languages such as Python, testing is one of the only ways to determine the correctness of your implementation.  Python has built the concept of `Unit Tests <https://docs.python.org/2/library/unittest.html>`_ into the core library.  *Unit Testing* is a technique for validating units of your program by making assertions about the behaviour of that code.  If any assertions turn out to be false, then you know your code isn't correct.

Nose
----

In the interest of making test as automatic as possible, Flask-Diamond uses `Nose <https://nose.readthedocs.org/en/latest/>`_ for *test discovery*, which will find and run all your tests without having to create a test harness.  As an application becomes more developed, it may become necessary to build a test harness for the application.  However, at the start of application development, it is usually easier to use test discovery in order to iterate faster.

Nose will automatically search through the ``/tests`` folder for any files starting with the name "test" that have functions in them that also start with "test".

Running Tests
-------------

It is possible to invoke the testing subsystem from the command line.  The following different testing methods are available in Flask-Diamond:

Run every test
^^^^^^^^^^^^^^

Find every test and run it.

::

    make test

Run individual tests
^^^^^^^^^^^^^^^^^^^^

Run tests identified with decorator ``@attr("single")``.  These "single" tests can be used to make testing much faster by skipping all of the other tests.

::

    make single

The following code snippet contains a simple test with the *single* attribute decorator applied to it.

::

    from nose.plugins.attrib import attr
    from flask.ext.testing import TestCase
    from flask.ext.diamond.mixins.testing import DiamondTestCaseMixin

    class BasicTestCase(DiamondTestCaseMixin, TestCase):
        @attr("single")
        def test_basic(self):
            assert True

Automatically run individual tests
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This functionality will watch the project folder for files to change.  When a file has changed, it will re-run tests identified with ``@attr("single")``.  This feature is designed to make it very quick to get feedback on the performance of your code.

::

    make watch

xUnit
-----

It is possible to automatically interpret the results of testing using the `xUnit framework <https://en.wikipedia.org/wiki/XUnit>`_.  `Nose xUnit <http://nose.readthedocs.org/en/latest/plugins/xunit.html>`_ output can permit tools like `Jenkins CI <http://jenkins-ci.org/>`_, `Travis CI <https://travis-ci.org/>`_, or `Atlassian Bamboo <https://www.atlassian.com/software/bamboo>`_ to capture the results of testing.
