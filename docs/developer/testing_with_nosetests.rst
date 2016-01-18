Writing
=======

This document is a work in progress.

Heading
-------

::

    # from .fixtures import typical_workflow

    class UserTestCase(GeneralTestCase):
        "Coverage for User Model"

        def setUp(self):
            super(UserTestCase, self).setUp()
            typical_workflow()

