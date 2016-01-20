Testing with Nose
=================

Writing tests is an important part of building an application.  Especially with dynamically typed languages such as Python, testing is one of the only ways to determine the correctness of your implementation.

In the interest of making test as automatic as possible, Flask-Diamond uses `Nose <https://nose.readthedocs.org/en/latest/>`_ for *test discovery*.  As an application becomes more developed, it may become necessary to build a test harness for the application.  However, when just beginning, it is usually easier to use test discovery in order to iterate faster.

Running Tests
-------------

It is possible to invoke the testing subsystem from the command line.

::

    make test

::

    make single

::

    make watch

It is also possible to automatically execute Nose Tests.  In particular, Nose's Xunit output can permit tools like Atlassian Bamboo to capture the results of testing.

Test Example
------------

::

    from nose.plugins.attrib import attr
    from flask.ext.testing import TestCase
    from flask.ext.diamond.mixins.testing import DiamondTestCaseMixin

    class BasicTestCase(DiamondTestCaseMixin, TestCase):
        def test_basic(self):
            assert True

Using Attributes
----------------

::

    from nose.plugins.attrib import attr
    from flask.ext.testing import TestCase
    from flask.ext.diamond.mixins.testing import DiamondTestCaseMixin

    class BasicTestCase(DiamondTestCaseMixin, TestCase):
        @attr("single")
        def test_basic(self):
            assert True

Test Driven Development
-----------------------

It is basically magical to write the tests, then use ``make watch`` to get real-time feedback on whether you've accomplished the task.
