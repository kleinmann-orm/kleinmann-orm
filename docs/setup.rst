======
Set up
======

.. _init_app:

Init app
========

After you defined all your models, kleinmann needs you to init them, in order to create backward relations between models and match your db client with appropriate models.

You can do it like this:

.. code-block:: python3

    from kleinmann import Kleinmann

    async def init():
        # Here we create a SQLite DB using file "db.sqlite3"
        #  also specify the app name of "models"
        #  which contain models from "app.models"
        await Kleinmann.init(
            db_url='sqlite://db.sqlite3',
            modules={'models': ['app.models']}
        )
        # Generate the schema
        await Kleinmann.generate_schemas()
    
    
Here we create connection to SQLite database client and then we discover & initialize models.

``generate_schema`` generates schema on empty database, you shouldn't run it on every app init, run it just once, maybe out of your main code.
There is also the option when generating the schemas to set the ``safe`` parameter to ``True`` which will only insert the tables if they don't already exist.

If you define the variable ``__models__`` in the ``app.models`` module (or wherever you specify to load your models from), ``generate_schema`` will use that list, rather than automatically finding models for you.

.. _cleaningup:

The Importance of cleaning up
=============================

Kleinmann ORM will keep connections open to external Databases. As an ``asyncio`` Python library, it needs to have the connections closed properly or the Python interpreter may still wait for the completion of said connections.

To ensure connections are closed please ensure that ``Kleinmann.close_connections()`` is called:

.. code-block:: python3

    await Kleinmann.close_connections()

The small helper function ``kleinmann.run_async()`` will ensure that connections are closed.

Reference
=========

.. automodule:: kleinmann
    :members:
    :undoc-members:

