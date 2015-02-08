# Flask-Diamond

Flask-Diamond provides a path that can guide your thought and development; Flask-Diamond is the road that leads to other ideas.

Flask-Diamond is a python Flask application platform that roughly approximates a django.  Flask-Diamond imports many other Flask libraries, and then glues them all together with sensible defaults.  The end result is a model administration view, accounts and high-level account operations (e.g. password reset), testing, documentation, project management (e.g. deployment), and more.

## Quick Start

```
mkvirtualenv my-diamond-app
pip install git+https://github.com/iandennismiller/Flask-Diamond.git#egg=Flask-Diamond
mkdir /tmp/my-diamond-app
cd /tmp/my-diamond-app
diamond-scaffold.sh
```

## Pre-requisites

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
