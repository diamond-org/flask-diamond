Managing Users with Flask-Security
==================================

*User* accounts are a common requirement for many applications.  Another common requirement is *Roles*, which can be used to grant certain users access to specific functions.  Both Users and Roles are provided in Flask-Diamond by `Flask-Security <http://pythonhosted.org/Flask-Security/>`_, which provides a nice interface for controlling these models.

User and Role Models
--------------------

Flask-Diamond is already set up with :class:`flask_diamond.models.user` and :class:`flask_diamond.models.role`, which provide everything needed for a simple setup.  You will notice in your application that ``models/__init__.py`` then imports these classes from Flask-Diamond.  In this manner, your application will incorporate these models into its own schema.

Overloading the User Model
--------------------------

With an application of moderate complexity, it may be necessary to store additional user data, and certain data may just be simple to put in the User model directly.  The following code snippet describes an ``init_security()`` function that can be used to implement your own User model.

::

    def init_security(self):
        self.super(app_models=models)

With that in place, ensure ``models__init__.py`` imports your own User model instead of importing from Flask-Diamond.

Flask-Admin Integration
-----------------------

You can use user accounts in lots of ways, but one common pattern for Users is to create a password-protected user interface.  To make this easier, the Flask-Diamond scaffold includes templates in ``views/administration/templates/security`` that permit you to customize the look of login, password maintenance, account registration, and password reset.  The templates already inherit from Flask-Admin, but by editing the templates in your project, you can customize them to other scenarios too.
