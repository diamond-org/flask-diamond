# Flask-Diamond

Flask-Diamond provides a path that can guide your thought and development; Flask-Diamond is the road that leads to other ideas.

Flask-Diamond is a python Flask application platform that roughly approximates a django.  Flask-Diamond imports many other Flask libraries, and then glues them all together with sensible defaults.  The end result is a model administration view, accounts and high-level account operations (e.g. password reset), testing, documentation, project management (e.g. deployment), and more.

## Quick Start

It's simple to scaffold a Diamond application.  First make a directory to hold the application

```
mkvirtualenv my-diamond-app
mkdir /tmp/my-diamond-app
cd /tmp/my-diamond-app
```

Then scaffold a Diamond application.

```
pip install git+https://github.com/iandennismiller/Flask-Diamond.git#egg=Flask-Diamond
diamond-scaffold.sh
make db server
```

## Pre-requisites

- python 2.7
- libxml-dev
- libxslt-dev
- python-dev
- virtualenv
- virtualenvwrapper
- pip

## Further Reading

See the /docs folder for other documentation.

## License

MIT License.
