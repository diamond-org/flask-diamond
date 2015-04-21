# Diamond

Diamond provides a path that can guide your thought and development; Diamond is the road that leads to other ideas.

Diamond is a python Flask application platform that roughly approximates a django.  Diamond imports many other Flask libraries, and then glues them all together with sensible defaults.  The end result is a model administration view, accounts and high-level account operations (e.g. password reset), testing, documentation, project management (e.g. deployment), and more.

[View the API documentation](http://iandennismiller.github.io/flask-diamond/api/)

## Quick Start

### 1. Install Diamond in a Python environment.

```
mkvirtualenv my-diamond-app
pip install git+https://github.com/iandennismiller/flask-diamond
```

### 2. Scaffold a new Diamond application with default options and start the server.

```
diamond-scaffold.sh
make db server
```

### 3. Finished!

You now have a server running at http://127.0.0.1:5000/admin

## Pre-requisites

- python 2.7.x
- python development libraries (e.g. python-dev or python-devel)
- virtualenv
- virtualenvwrapper
- pip

## Further Reading

See the /docs folder for other documentation.

## License

MIT License.
