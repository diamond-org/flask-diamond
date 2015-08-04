Philosophy of Flask-Diamond
===========================

*Flask-Diamond provides a path that can guide your thought and development. Flask-Diamond is the road that leads to other ideas.*

The following principles serve to guide the development of Flask-Diamond.

Inheritance
-----------

Flask-Diamond is primarily configured via Pythonic Inheritance.  Your main application object will inherit from Flask-Diamond, and any functions you wish to customize must be overridden in order to change their behavior.

Economy
-------

There are tons of libraries wrapped up in Flask-Diamond.  If something has been done well by somebody else, then it is always preferable to leverage that work instead of re-building an unnecessary component.

Stable
------

Flask-Diamond versions are tied closely to specific versions of third-party libraries.  When you stick with a specific version of Flask-Diamond, you can lock the version of third-party libraries too.  The goal is to prevent any requirements from changing accidentally so that your application will be more resistant to code rot and API breakage.

Decomposable
------------

Because third-party libraries are constantly changing, it is sometimes desirable to upgrade just one library without upgrading anything else.  Flask-Diamond is built atop the Flask ecosystem, which is architecturally decomposable.  Thus, extensions may be upgraded individually.

Data-centric
------------

Flask-Diamond was originally built to support the research objectives of `Ian Dennis Miller <http://imiller.utsc.utoronto.ca/>`_.  Through his work on memes and social networks, Ian regularly needed to build lightweight API access to big data sets.  Due to the precise nature of the SQL queries needed, a powerful standalone ORM like SQLAlchemy was preferred over the Django approach of bundling the ORM with the web platform.  Thus, Flask-Diamond is suitable for projects that require raw access to SQL queries.

Sensible
--------

Flask-Diamond is pretty sensible about the defaults it presents.  A lot of decisions have already been made in the service of delivering a functioning application out-of-the-box.  The goal is to enable a focus upon the unique parts of your application, rather than the common tasks that most applications need anyway.
