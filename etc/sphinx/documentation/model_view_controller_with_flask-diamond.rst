Model-View-Controller with Flask-Diamond
========================================

Model-View-Controller (MVC) is a popular architecture for designing applications that have a user interface.  At its heart, MVC is a collection of `software design patterns <https://en.wikipedia.org/wiki/Software_design_pattern>`_ that provide a vocabulary for designing your application.  When you "speak MVC," other people who also know MVC will understand what you are saying.

The MVC vocabulary consists of:

- **Models**: a way for talking about data
- **Views**: a way for talking about user interfaces
- **Controllers**: a way for talking about program logic

This document presents an overview of Model-View-Controller and links to more detailed documentation that discusses these ideas in greater detail.

Model
-----

A model is usually named after a noun.  A model is a data representation of something that exists, and just about anything that exists can be modeled.

Entities and Relationships
^^^^^^^^^^^^^^^^^^^^^^^^^^

To model a chess game, you'd start with a model of Players and Chess Pieces, which are entities. A player has many chess pieces, so there is a relationship between our entities.  Using nothing more than the idea of "Players" and "Chess Pieces", you can go a long way towards modeling the game of chess.

All models have two properties:

- **Entities**: An Entity is a type of object.  Entities have attributes, which are characteristics of the Entity.  In the chess example, a Player is a an Entity; there are two Players in chess and each one is an instance of the Player class.  An attribute of Players is "color"; the player controls either white pieces or black pieces, so the player's color can be white or black.  Since a player can have a name, *name* is therefore also an attribute of a Player.
- **Relationships**: Entities can affect one another through relationships.  In the chess example, a Player has many Pieces and each Piece is owned by a Player.  Since a Player can have many Pieces, we call this a "one-to-many" Relationship.  There are also one-to-one and many-to-many relationships.

A model can therefore be described using an Entity-Relationship Diagram, which shows all of the types of objects, their attributes, and the way entities relate to one another.  Read more about :doc:`writing_models_with_sqlalchemy` for a more detailed discussion and code examples.

A Philosophy of Models
^^^^^^^^^^^^^^^^^^^^^^

A model might be a very simple representation of a real thing, or the model might be very detailed.  A model of an entire country's economy might require lots of detail, whereas a model of a school district might be relatively simpler.

A model is in some ways a platonic ideal of the actual domain being modeled.  While things in the "real world" are irregular in an uncountable number of ways, our models are perfectly regular.  Since models are stored in a database, all of the model attributes can be lined up nicely into rows and columns.  Tidy!

Paradoxically, a model is always an imperfect representation of the thing it is modeling.  The irregularities of the real world are difficult to capture using a model.  The goal for good model creation is to isolate the parts of the model that are regular so as to reduce the number of exceptions to your model.

Sometimes, we talk about "domains" when we talk about models, because our models might be thematically related to one another.  A domain might be something like *finance*, *gaming*, *email*, or any other broad category that people build applications for.  To properly model a domain, we might talk to a "domain expert" to learn more about the kinds of models we are building.

View
----

A view is a user interface that can present data that comes from a model.  In classic MVC, the model pushes data to the view, and the view knows how to update itself to display the data that was received from the model.  Views can also contain input elements like buttons, fields, and sliders.  When these input elements are activated, the Controller must decide how to respond.  Views are often written as templates that have placeholders for data. For web programming, a View template is frequently written using HTML [#f1]_.  Read more about :doc:`writing_views_with_jinja` for a more detailed discussion and code examples.

Controller
----------

A controller responds to input by changing a view or model.  A common type of controller is driven with a Graphical User Interface, which uses things like menus, fields, and buttons so that a human can click stuff to get things done.  Read more about :doc:`writing_a_gui_with_flask-admin` for a more detailed discussion.

A different type of controller is an API, which is typically used by other software (rather than a human) to make the application do something.  Read more about :doc:`writing_an_api_with_flask-restful` for a more detailed discussion.

.. rubric:: Footnotes

.. [#f1] There's nothing inherently special about HTML templates for constructing Views.  For example, Android Views can be constructed using Java.  The point is that the idea of *views* can be generalized to any platform.