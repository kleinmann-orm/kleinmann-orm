=======
Linters
=======

.. _pylint:

PyLint plugin
=============

Since Kleinmann ORM uses MetaClasses to build the Model objects, PyLint will often not understand how the Models behave. We provided a `kleinmann.pylint` plugin that enhances PyLints understanding of Models and Fields.

Usage
-----

In your projects ``.pylintrc`` file, ensure the following is set:

.. code-block:: ini

    load-plugins=kleinmann.contrib.pylint


