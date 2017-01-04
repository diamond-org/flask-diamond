Facet: REST
===========

One of the most common ways to build an API is using a paradigm called `REST <https://en.wikipedia.org/wiki/Representational_state_transfer>`_.
`Flask-RESTful <http://flask-restful.readthedocs.org/en/latest/>`_ is a great library for Flask that simplifies the creation of a REST API.
This document describes REST and how to implement it in a Flask-Diamond project.

REST in a Nutshell
------------------

Representational State Transfer, usually abbreviated REST, can be simplified as follows:

- The web consists of documents that are referred to by URL links.
- Each URL is a "thing".  As a part of speech, it is a noun.  For example: a URL points to a picture, a document, or a person's timeline.
- The language spoken by web browsers and web servers is called HTTP.  This is the protocol for "hypertext".
- HTTP provides actions (verbs) like GET, PUT, DELETE, and POST.
- Using HTTP and URLs provides verbs and nouns that we can use to write statements, like "GET a Picture" or "DELETE a Document".

REST is a strong statement about the grammar of the web.
It tells us where the nouns are and where the verbs are.
If we learn to make APIs that are *RESTful*, then we can count on others to be able to use our APIs in natural ways to create complex expressions.

Examples of REST
^^^^^^^^^^^^^^^^

Let's say you are building an API for a solar system and you need to manage planets for observation.
Our API could then expose one URL endpoint for retrieving all planets: ``/api/planet_list``.
We could then add a planet to our solar system with an HTTP POST containing the following data:

::

    {
        'name': 'Venus',
        'mass': '90.0'
    }

Such a POST could be issued using javascript, from the command line (e.g. with ``curl``), or using any HTTP client.
That's the beauty of REST: if you work with the web, the web can work with you.

Flask-RESTful
-------------

It is easy to create RESTful APIs with `Flask-RESTful <http://flask-restful.readthedocs.org/en/latest/>`_, which is already integrated into Flask-Diamond.

The primary way to use Flask-RESTful is to create Resource objects.  A Resource is a "thing" that your API will expose.  You can easily add API Resources to your Flask-Diamond application by placing them into a function called *init_rest()*:

::

    from flask_diamond import db
    from .mixins import DiamondTestCase
    from ..models import Planet

    def init_rest():
        class PlanetResource(Resource):
            def get(self, name):
                return models.planet.find(name=name).dumps()

        rest.add_resource(PlanetResource, '/api/planet/<str:name>')

This simple example creates a resource called PlanetResource.
Then, it specifies a way to handle the GET verb, which will result in retrieving a planet.
Finally, the resource is exposed using a URL: ``/api/planet/...``.

MarshmallowMixin
----------------

:class:`flask_diamond.mixins.marshmallow.MarshmallowMixin` simplifies object marshalling, which is the process of mapping data to and from a serialization format like JSON.
This functionality is provided by `Marshmallow <http://marshmallow.readthedocs.org/en/latest/>`_ and `Flask-Marshmallow <http://flask-marshmallow.readthedocs.org/en/latest/>`_.

Marshalling is useful because applications must frequently send model data across the Internet, and in order to do so, models are commonly translated into JSON or another format.
For example, date and time objects are native Python objects that must be converted to a string in order for JSON to transmit them.
Marshalling makes serialization and deserialization into a repeatable process.

Let's look at the following line of code:

::

    return models.planet.get(id).dumps()

The *dumps()* at the end of the line will cause an ORM model object to be converted to JSON using Marshmallow.
For more information, please see the documentation for `Marshmallow <http://marshmallow.readthedocs.org/en/latest/>`_ and `Flask-Marshmallow <http://flask-marshmallow.readthedocs.org/en/latest/>`_.

How not to REST
---------------

REST says we should not create URLs that imply actions; URLs must be things.  This pattern is common in older websites.
For example, you should not build an API with a URL called ``/api/rename_planet`` because that describes an action: changing a planet's name.
REST says the only actions available are HTTP verbs, like GET and PUT.

You can think about it this way too: when a web client visits a URL, it usually issues the GET verb.
It doesn't really make sense to ``GET /api/rename_planet`` because that's actually something you want to push to the server, not get from the server.
However, early web developers tried to make this work using arguments, which resulted in operations like ``GET /api/move_piece?from=A2&to=C3``.
These became really long URLs that contained all the same information as the RESTful example, but which broke certain features of the Internet.
For example, if a web spider visited that URL, the web server would incorrectly interpret that visit as a command to move a piece.
This leads to chaos.
Don't make URLs this way.
Be RESTful, instead.
