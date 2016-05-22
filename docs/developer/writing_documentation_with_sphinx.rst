Documentation with Sphinx
=========================

As projects grow in size, the need to create documentation increases.  The `Sphinx Project <http://www.sphinx-doc.org/en/stable/contents.html>`_ has put forth a very robust Python documentation solution.  As a result, Flask-Diamond provides a starter template for creating your own documentation using Sphinx.

Where are the files
-------------------

You will find a starter set of documentation in the ``/docs`` folder of your project.  The first file you need to edit is called ``/docs/index.rst``, and from there build the table of contents to describe your project. Images and media may be placed in ``/docs/_static``.  These source files will be transformed into a documentation website that can be browsed online.

Sphinx
------

Sphinx is a structured document generator application.  As a project author, you create documents that describe your project, and Sphinx will take care of the Table of Contents, links between documents, and all of the other parts that make it easy for somebody to navigate the documentation.  Sphinx is particularly well suited to creating documentation websites, in which case Sphinx will automatically apply a theme to every page.  The end result of using Sphinx is that your project will have an extremely functional online documentation website.

Restructured Text
^^^^^^^^^^^^^^^^^

Documentation in Sphinx is written using a markup language called `ReStructured Text <http://www.sphinx-doc.org/en/stable/rest.html>`_ (`quickref <http://docutils.sourceforge.net/docs/user/rst/quickref.html>`_).  While this language has some similarities to `Markdown <http://daringfireball.net/projects/markdown/basics>`_, it has many extensions that are suited to document structuring.  As a result, Restructured Text makes it easy enough to manage links between pages, make references to specific Python classes, and add footnotes.

In my experience, the learning curve on Restructured Text is steeper than I expected.  As a result, you need to persevere, but the payoff is totally worth it.  The best place to start is with the `ReStructured Text <http://www.sphinx-doc.org/en/stable/rest.html>`_ documentation from the Sphinx website.

autodoc
^^^^^^^

Sphinx can use the `autodoc extension <http://www.sphinx-doc.org/en/stable/ext/autodoc.html>`_ to look at your project's file structure and determine all of the classes in your project.  This can be extremely useful for generating API documentation.  Sphinx can also extract method and object signatures, which makes it easy to describe all of the parameters for everything.

docstrings
^^^^^^^^^^

Sphinx autodoc is also able to scan your source code for comments that have been formatted for Sphinx using Restructured Text.  Here is an example taken from the :func:`flask_diamond.facets.accounts.init_accounts` Flask-Diamond source code:

::

    def init_accounts(self, app_models=None):
        """
        Initialize Security for application.

        :param kwargs: parameters that will be passed through to Flask-Security
        :type kwargs: dict
        :returns: None

        >>> def ext_security(self):
        >>>    super(MyApp, self).ext_security(confirm_register_form=CaptchaRegisterForm)
        """

The comment above will be used to create documentation by Sphinx.  Special directives like ``:param:`` are used to specify details about the documentation that *autodoc* cannot determine on its own.

Building the documentation
--------------------------

In the project on the command line:

::

    make docs

Output
^^^^^^

The results of ``make docs`` will end up in ``var/sphinx/build``.  You can open that folder in your web browser to view the documentation.

ReadTheDocs
^^^^^^^^^^^

It is easy to integrate Flask-Diamond applications with readthedocs.org due to the use of Sphinx.  A special file called ``.readthedocs.txt`` is included with the project scaffold.  This file contains a reduced set of Python requirements that may make it easier for RTD to build your project.
