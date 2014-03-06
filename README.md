# flask-diamond

flask-diamond is a python Flask application platform that roughly approximates a django.  flask-diamond imports many other Flask libraries, and then glues them all together with sensible defaults.  The end result is a model administration view, accounts and high-level account operations (e.g. password reset), testing, documentation, project management (e.g. deployment), and more.

flask-diamond provides a path that can guide your thought and development; flask-diamond is the road that leads to other ideas.

## installation

1. First clone flask-diamond

    git clone https://github.com:iandennismiller/flask-diamond.git
    cd flask-diamond

2. Install libraries and dependencies

    sudo mkdir /var/lib/flask-diamond
    sudo chown $USER /var/lib/flask-diamond
    mkvirtualenv flask-diamond
    make dep install doc test

3. Set up the application database

    make db

4. Finally, run the server locally

    make server

## Developing with flask-diamond

fabfile.py: runs on dev machine, coordinates deployment
Makefile: direct action on the working directory
setup.py: python package management, including installation
runserver.py: spawn the daemon (usually not called directly)

## Makefile: local development

### to start the dev server locally

    make server

### to test the package locally

    make test

### to watch files for changes and repeatedly re-run tests

    make watch

## fabfile.py: deployment

### to deploy

    fab -H example.com rsync setup restart

### to launch an interactive session

    fab -H example.com ipython

## License

MIT.

