MVC: Model, View, Controller
============================

Model-View-Controller (MVC) is a popular architecture for designing applications that have a user interface.
At its heart, MVC is a collection of `software design patterns <https://en.wikipedia.org/wiki/Software_design_pattern>`_ that provide a vocabulary for designing your application.
When you "speak MVC," other people who also know MVC will understand what you are saying.

The MVC vocabulary consists of:

- **Models**: a way for talking about data
- **Views**: a way for talking about user interfaces
- **Controllers**: a way for talking about program logic

This document presents an overview of Model-View-Controller and links to more detailed documentation that discusses these ideas in greater detail.

Model
-----

A model is usually named after a noun.
A model is a data representation of something that exists, and just about anything that exists can be modeled.

Entities and Relationships
^^^^^^^^^^^^^^^^^^^^^^^^^^

To model a solar system, you'd start with a model of Planets and Satellites, which are the *entities* we will be dealing with.
A planet can have many satellites, so there is a relationship between our entities.
Using nothing more than the idea of "Planets" and "Satellites", you can go a long way towards modeling a solar system.

A complete data model consists of entities and the relationships between those entities.

- **Entities**: An Entity is a type of object.  Entities have attributes, which are characteristics of the Entity.
In :doc:`tutorial-planets`, a Planet is a an Entity and so is a Satellite.
An attribute of a Planet is its "mass"; the mass of a planet is stored in the data model alongside the name of the planet.
Since a planet can have a name, *name* is therefore also an attribute of a Planet.
- **Relationships**: Entities can affect one another through relationships.
In :doc:`tutorial-planet`, a Planet can have many Satellites.
Since a Planet can have many Satellites, we call this a "one-to-many" Relationship.
There are also one-to-one and many-to-many relationships.

A model can therefore be described using an Entity-Relationship Diagram, which shows all of the types of objects, their attributes, and the way entities relate to one another.
Read more about :doc:`models` for a more detailed discussion and code examples.

A Philosophy of Models
^^^^^^^^^^^^^^^^^^^^^^

A model might be a very simple representation of a real thing, or the model might be very detailed.
A model of an entire country's economy might require lots of detail, whereas a model of a school district might be relatively simpler.

A model is in some ways a platonic ideal of the actual domain being modeled.  While things in the "real world" are irregular in an uncountable number of ways, our models are perfectly regular.  Since models are stored in a database, all of the model attributes can be lined up nicely into rows and columns.  Tidy!

Paradoxically, a model is always an imperfect representation of the thing it is modeling.  The irregularities of the real world are difficult to capture using a model.  The goal for good model creation is to isolate the parts of the model that are regular so as to reduce the number of exceptions to your model.

Sometimes, we talk about "domains" when we talk about models, because our models might be thematically related to one another.  A domain might be something like *finance*, *gaming*, *email*, or any other broad category that people build applications for.  To properly model a domain, we might talk to a "domain expert" to learn more about the kinds of models we are building.

View
----

A view is a user interface that can present data that comes from a model.  In classic MVC, the model pushes data to the view, and the view knows how to update itself to display the data that was received from the model.  Views can also contain input elements like buttons, fields, and sliders.  When these input elements are activated, the Controller must decide how to respond.  Views are often written as templates that have placeholders for data. For web programming, a View template is frequently written using HTML [#f1]_.  Read more about :doc:`blueprints` for a more detailed discussion and code examples.

Controller
----------

A controller responds to input by changing a view or model.  A common type of controller is driven with a Graphical User Interface, which uses things like menus, fields, and buttons so that a human can click stuff to get things done.  Read more about :doc:`administration` for a more detailed discussion.

A different type of controller is an API, which is typically used by other software (rather than a human) to make the application do something.  Read more about :doc:`rest` for a more detailed discussion.

.. rubric:: Footnotes

.. [#f1] There's nothing inherently special about HTML templates for constructing Views.  For example, Android Views can be constructed using Java.  The point is that the idea of *views* can be generalized to any platform.