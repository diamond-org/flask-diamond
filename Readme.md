# Flask-Diamond

Flask-Diamond provides a path that can guide your thought and development; Flask-Diamond is the road that leads to other ideas.

Flask-Diamond is a python Flask application platform that roughly approximates a django.  Flask-Diamond imports many other Flask libraries, and then glues them all together with sensible defaults.  The end result is a model administration view, accounts and high-level account operations (e.g. password reset), testing, documentation, project management (e.g. deployment), and more.

## Quick Start

### 1. Make a directory to hold the application.

```
mkdir /tmp/my-diamond-app
cd /tmp/my-diamond-app
```

### 2. Install Flask-Diamond.

```
mkvirtualenv my-diamond-app
pip install git+https://github.com/iandennismiller/Flask-Diamond.git#egg=Flask-Diamond
```

### 3. Scaffold a new Diamond application with default options and start the server.

```
diamond-scaffold.sh
make db server
```

### 4. Finished!

You now have a server running at http://127.0.0.1:5000/admin

## Pre-requisites

- python 2.7
- libxml-dev
- libxslt-dev
- python-dev
- virtualenv
- virtualenvwrapper
- pip

## Further Reading

[Read the API documentation](http://iandennismiller.github.io/flask-diamond/api/)

See the /docs folder for other documentation.

## License

MIT License.
