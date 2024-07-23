Kleinmann-ORM FastAPI example
============================

We have a lightweight integration util ``kleinmann.contrib.fastapi`` which has a class ``RegisterKleinmann`` that can be used to set/clean up Kleinmann-ORM in lifespan context.

Usage
-----

.. code-block:: sh

    uvicorn main:app --reload
