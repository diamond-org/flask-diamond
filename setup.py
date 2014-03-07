from setuptools import setup
import os, shutil

version = '0.1'

setup(version=version,
      name='flask-diamond',
      description = "flask-diamond provides a path that can guide your thought and development; flask-diamond is the road that leads to other ideas.",
      packages = [
            "FlaskDiamond",
            "FlaskDiamond.Views",
            "FlaskDiamond.Utils",
            ],
      scripts = [
      #      "bin/runserver.py",
      #      "bin/manage.py",
      ],
      long_description="""flask-diamond is a python Flask application platform that roughly approximates a django.  flask-diamond imports many other Flask libraries, and then glues them all together with sensible defaults.  The end result is a model administration view, accounts and high-level account operations (e.g. password reset), testing, documentation, project management (e.g. deployment), and more.""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      include_package_data = True,
      keywords='',
      author='Ian Dennis Miller',
      author_email='ian@iandennismiller.com',
      url='http://www.iandennismiller.com',
      install_requires = [
            ### app

            ### development

            "Sphinx==1.1.3",
            "Fabric==1.8.0",
            "nose==1.2.1",
            "watchdog==0.6.0",
            "alembic==0.6.0",
            "Flask-Migrate==0.1.4",
            "distribute>=0.6.35",
            "ipython>=1.2.1",
            "pylint==0.26.0",

            ### Flask Framework

            "Werkzeug==0.9.4",
            "Jinja2==2.7.2",
            "Flask==0.10.1",
            "Flask-Admin==1.0.7",
            "Flask-WTF==0.9.4",
            "Flask-Login==0.2.9",
            "Flask-Security==1.7.1",
            "Flask-Script==0.6.2",
            "Flask-Mail==0.9.0",
            "Flask-Misaka==0.2.0",
            "Flask-Testing==0.4",
            "Flask-DebugToolbar==0.9.0",

            ### databases

            ### mongodb
            # "pymongo==2.6.3",
            # "Flask-MongoEngine>=0.1.3",
            ### sqlalchemy
            "SQLAlchemy==0.9.3",
            "SQLAlchemy-Utils==0.24.1",
            "Flask-SQLAlchemy>=1.0",
      ],
      license='MIT',
      zip_safe=False,
)
