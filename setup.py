from setuptools import setup

version = '0.2.6'

setup(version=version,
    name='Flask-Diamond',
    description="""\
        Flask-Diamond provides a path that can guide your thought and development.
        Flask-Diamond is the road that leads to other ideas.
        """,
    packages=[
        "flask_diamond",
        "flask_diamond.views",
        "flask_diamond.views.diamond",
        "flask_diamond.utils",
    ],
    scripts=[
        "bin/diamond-scaffold.sh",
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
        #('https://github.com/iandennismiller/Flask-Diamond'
        #    '/archive/0.2.3.tar.gz#egg=flask_diamond-0.2.3'),
    ],
    install_requires=[
        ### application-specific requirements

        # "jsmin==2.0.9",
        # "cssutils==1.0",
        # "SQLAlchemy-Utils==0.29.8",
        # "pymongo==2.6.3",
        # "Flask-MongoEngine>=0.1.3",
        # "psycopg2==2.6",

        ### Flask Framework

        "Werkzeug==0.9.4",
        "Jinja2==2.7.2",
        "Flask==0.10.1",
        "Flask-Migrate==1.3.0",
        "Flask-Admin==1.1.0",
        "Flask-WTF==0.9.4",
        "Flask-Login==0.2.9",
        "Flask-Security==1.7.1",
        "Flask-Script==2.0.5",
        "Flask-Mail==0.9.1",
        "Flask-Testing==0.4.2",
        "Flask-DebugToolbar==0.9.2",
        "Flask-Assets==0.10",
        "Flask-DbShell==1.0",
        "Flask-RESTful==0.3.2",
        "Flask-Markdown==0.3",
        "Flask-SQLAlchemy==2.0",
        "Flask-Marshmallow==0.4.0",
        "Flask-Celery-Helper==1.1.0",

        ### project management, documentation, testing, and deployment

        "Sphinx==1.2.3",
        "Fabric==1.10.1",
        "nose==1.3.4",
        "watchdog==0.8.3",
        "wheel==0.24.0",
        "pylint==1.4.1",
        "mr.bob==0.1.1",
        # hardcoding alembic because the latest version does not parse correctly in FlaskMigrate
        "alembic==0.7.4",
    ],
    license='MIT',
    zip_safe=False,
)
