IT Operations with Fabric
=========================

There is frequently a split between the application development environment and the live deployment environment.  When the application ends up running on a remote host while you are doing your work on a workstation, it can be helpful to simplify remote system operations.  Flask-Diamond uses `Fabric <http://www.fabfile.org/>`_ to make it pretty easy to invoke system functions from the command line.

Using Fabric
------------

To use the Flask-Diamond Fabric functionality, navigate to the root directory of the project and issue the following command:

::

    fab help

This will list all of the available commands.

Flask-Diamond Fabric Commands
-----------------------------

By default, Flask-Diamond provides a ``fabfile.py`` with the scaffold with the following functionality:

- **rsync**: copy files directly from the working directory to the remote host
- **pull**: on the remote host, execute ``git pull`` in the application directory
- **setup**: run ``make install`` on the remote host
- **ipython**: enter an ipython shell on the remote host
- **shell**: open a bash shell on the remote host
- **restart**: restart the remote application server
- **nginx_restart**: restert the remote web server
- **logs**: view the application logs

Customizing Fabric
------------------

Because all systems are different, it is not too likely that all of the commands in ``fabfily.py`` will work.  However, this at least provides a starting point.
