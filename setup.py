from setuptools import setup

version = '0.2.0'

setup(version=version,
    name='Flask-Diamond',
    description="""\
        Flask-Diamond provides a path that can guide your thought and development.
        Flask-Diamond is the road that leads to other ideas.
        """,
    packages=[
        "flask_diamond",
        "flask_diamond.views",
        "flask_diamond.utils",
    ],
    scripts=[
        # "bin/runserver.py",
        # "bin/manage.py",
    ],
    long_description="""\
        Flask-Diamond is a python Flask application platform that roughly approximates a django.
        Flask-Diamond imports many other Flask libraries, and then glues them all together with
        sensible defaults.  The end result is a model administration view, accounts and high-level
        account operations (e.g. password reset), testing, documentation, project management
        (e.g. deployment), and more.
        """,
    classifiers=[],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    include_package_data=True,
    keywords='',
    author='Ian Dennis Miller',
    author_email='ian@iandennismiller.com',
    url='http://www.iandennismiller.com',
    dependency_links=[
        # 'https://github.com/mrjoes/flask-admin/tarball/master#egg=flask_admin-1.0.7'
    ],
    install_requires=[
        ### app

        ### development

        "Sphinx==1.1.3",
        "Fabric==1.8.0",
        "nose==1.2.1",
        "watchdog==0.7.1",
        "alembic==0.6.0",
        "pylint==1.4.0",
        "jsmin==2.0.9",
        "cssutils==1.0",
        "wheel==0.24.0",
        "lxml==3.4.1",
        "cssselect==0.9.1",
        "requests==2.5.1",
        "argh==0.25.0",

        ### Flask Framework

        "Werkzeug==0.9.4",
        "Jinja2==2.7.2",
        "Flask==0.10.1",
        "Flask-Migrate==1.3.0",
        "Flask-Admin==1.0.8",
        "Flask-WTF==0.9.4",
        "Flask-Login==0.2.9",
        "Flask-Security==1.7.1",
        "Flask-Script==0.6.2",
        "Flask-Mail==0.9.0",
        "Flask-Testing==0.4",
        "Flask-DebugToolbar==0.9.0",
        "Flask-Assets==0.9",
        "Flask-DbShell==1.0",
        "Flask-RESTful==0.2.12",
        "Flask-Markdown==0.3",

        ### databases

        ### mongodb
        # "pymongo==2.6.3",
        # "Flask-MongoEngine>=0.1.3",
        ### sqlalchemy
        "SQLAlchemy==0.9.3",
        "SQLAlchemy-Utils==0.24.1",
        "Flask-SQLAlchemy==2.0",
    ],
    license='MIT',
    zip_safe=False,
)
