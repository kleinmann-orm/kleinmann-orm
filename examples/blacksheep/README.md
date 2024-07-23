Kleinmann-ORM BlackSheep example
============================

We have a lightweight integration util ``kleinmann.contrib.blacksheep`` which has a single function ``register_kleinmann`` which sets up Kleinmann-ORM on startup and cleans up on teardown.

Usage
-----

.. code-block:: sh

    uvicorn server:app --reload
