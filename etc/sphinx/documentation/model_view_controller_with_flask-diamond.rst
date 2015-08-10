Model-View-Controller with Flask-Diamond
========================================

Model-View-Controller (MVC) is a popular architecture for designing applications that have a user interface.  At its heart

Model
^^^^^

A model is a data representation of something that exists.  To model a chess game, you'd start with a model of Players and Chess Pieces. Using nothing more than the idea of "Players" and "Chess Pieces", you can go a long way towards modeling a game of chess.

A model has two properties:

- **Entities**: An Entity is a type of object.  In the chess example, a Player is a an Entity.  There are two Players in chess and each one is an instance of the Player class.  Entities have attributes, which are characteristics of the Entity.  An attribute of Players is "color"; the player controls either white pieces or black pieces.
- **Relationships**: Entities can affect one another through relationships.  In the chess example, a Player has many Pieces and each Piece is owned by a Player.  Since a Player can have many Pieces, we call this a "one-to-many" Relationship.  There are also one-to-one and many-to-many relationships.

A model can therefore be described using an Entity-Relationship Diagram, which shows all of the types of objects, their attributes, and the way entities relate to one another.  Read more about :doc:`writing_models_with_sqlalchemy` for a more detailed discussion and code examples.

View
^^^^

A view is a way to present model data to a user.  If a view has been created for a type of object, then any object of that type can be visualized with a view.  In classic MVC, the model pushes data to the view, and the view knows how to update itself to display the data that was received from the model.  In practice, views are often written as templates that have placeholders for data.  Read more about :doc:`writing_views_with_jinja` for a more detailed discussion and code examples.

Controller
^^^^^^^^^^

A controller responds to input by changing a view or model.  A common type of controller is the Graphical User Interface, which uses things like menus, fields, and buttons so that a user can click stuff to get things done.  Read more about :doc:`writing_a_gui_with_flask-admin` for a more detailed discussion.

A different type of controller is an API, which is typically used by software to make other software do something.  Read more about :doc:`writing_an_api_with_flask-restful` for a more detailed discussion.
