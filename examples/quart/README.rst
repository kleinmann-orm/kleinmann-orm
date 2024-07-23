Kleinmann-ORM Quart example
==========================

We have a lightweight integration util ``kleinmann.contrib.quart`` which has a single function ``register_kleinmann`` which sets up Kleinmann-ORM on startup and cleans up on teardown.

Note that the modules path can not be ``__main__`` as that changes depending on the launch point. One wants to be able to launch a Quart service from the ASGI runner directly, so all paths need to be explicit.

Usage
-----

.. code-block:: sh

    QUART_APP=main quart
        ...
        Commands:
          generate-schemas  Populate DB with Kleinmann-ORM schemas.
          run               Start and run a development server.
          shell             Open a shell within the app context.

    # To generate schemas
    QUART_APP=main quart generate-schemas

    # To run
    QUART_APP=main quart run
