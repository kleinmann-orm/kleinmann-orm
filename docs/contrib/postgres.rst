.. _contrib_postgre:

========
Postgres
========

Indexes
=======

Postgres specific indexes.

.. autoclass:: kleinmann.contrib.postgres.indexes.BloomIndex
.. autoclass:: kleinmann.contrib.postgres.indexes.BrinIndex
.. autoclass:: kleinmann.contrib.postgres.indexes.GinIndex
.. autoclass:: kleinmann.contrib.postgres.indexes.GistIndex
.. autoclass:: kleinmann.contrib.postgres.indexes.HashIndex
.. autoclass:: kleinmann.contrib.postgres.indexes.SpGistIndex

Fields
======

Postgres specific fields.

.. autoclass:: kleinmann.contrib.postgres.fields.TSVectorField

Functions
=========

.. autoclass:: kleinmann.contrib.postgres.functions.ToTsVector
.. autoclass:: kleinmann.contrib.postgres.functions.ToTsQuery
.. autoclass:: kleinmann.contrib.postgres.functions.PlainToTsQuery

Search
======

Postgres full text search.

.. autoclass:: kleinmann.contrib.postgres.search.SearchCriterion
