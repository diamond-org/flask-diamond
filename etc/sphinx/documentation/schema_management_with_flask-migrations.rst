Schema Management with Flask-Migrations
=======================================

When the Python model is changed, the database must be updated so that it has the right columns.  Any time a table or column is changed in any way, we say the data schema has changed.  For example, if you were to extend the ``Person`` model to add an email address, then you must also add an email address column to the database.

Flask-Diamond makes it easy to accomplish this during development with ``make db``, which will delete the development database and rebuild it with all new columns matching your models.  However, in production, you usually want to keep your data instead of deleting it every time you add a column.  Furthermore, it's pretty easy to manually add a column to a table without deleting the data that's already in the table.  Luckily, there's a better way.

Schema migrations, which are handled using Flask-Migrations, can be used to change in-production databases by recording the minimal set of steps will make your database schema match your model.  Migrations are versioned, so it is possible to experiment with schemas before deploying them.  It is also possible to roll back schemas in case something went wrong.
