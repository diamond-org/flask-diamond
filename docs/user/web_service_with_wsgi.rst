Web Services with WSGI
======================

For deploying your application in a production environment, you will probably end up using a `WSGI <https://www.python.org/dev/peps/pep-3333/>`_ application server like `uwsgi <http://uwsgi-docs.readthedocs.org/en/latest/>`_ or `gunicorn <http://gunicorn.org/>`_.  By default, Flask-Diamond will install gunicorn as a requirement.

System Start-up
---------------

Under most circumstances, you will want to automatically run the application server when the host boots.  This is going to be different for every host, but an example demonstrates launching gunicorn via Ubuntu upstart:

::

    #!upstart
    description "flask-diamond daemon"

    env USER=flask-diamond
    env SETTINGS=/etc/flask-diamond.conf

    start on runlevel [2345]
    stop on runlevel [06]

    respawn

    exec start-stop-daemon --start \
        --make-pidfile \
        --pidfile /var/run/$USER-daemon.pid \
        --chuid $USER \
        --exec /var/lib/$USER/.virtualenvs/$USER/bin/gunicorn -- \
            --workers 2 \
            --bind 0.0.0.0:5000 \
            --user $USER \
            --chdir /var/lib/$USER \
            --log-file /var/lib/$USER/gunicorn-error.log \
            --access-logfile /var/lib/$USER/gunicorn-access.log \
            --pid /var/run/$USER-daemon.pid \
            --daemon \
            flask_diamond.wsgi:app

This demonstrates several important principles:

- setting the configuration file that will control the application server
- launching the application server from inside the Python virtual environment

Reverse Proxy
-------------

You probably want to keep your application server behind a firewall, so a common pattern for deploying Flask-Diamond applications relies upon a reverse proxy.  There is `a good Digital Ocean tutorial <https://www.digitalocean.com/community/tutorials/how-to-configure-nginx-as-a-web-server-and-reverse-proxy-for-apache-on-one-ubuntu-14-04-droplet>`_ for setting up a reverse proxy with either nginx or apache.

Puppet-Diamond
--------------

For scaling up deployment, it is recommended to use an automation solution like Puppet or Chef.  Flask-Diamond is particularly easy to deploy with `Puppet-Diamond <http://puppet-diamond.readthedocs.org/en/latest/>`_, which will simplify the management of the host configurations as well as application deployment.

Embedded Server
---------------

Flask-Diamond provides an embedded web server with ``bin/manage.py`` and ``bin/runserver.py`` for simple deployments, like development and debugging.  This is not recommended for production use.  However, when paired with a reverse proxy, this is actually good enough to handle a surprising amount of traffic.
