.. _index:

=======
Indexes
=======

Default kleinmann use `BTree` index when define index use `db_index=True` in field, or define indexes use in `Meta` class, but if you want use other index types, like `FullTextIndex` in `MySQL`, or `GinIndex` in `Postgres`, you should use `kleinmann.indexes.Index` and its subclasses.

Usage
=====

Following is example which use `FullTextIndex` and `SpatialIndex` of `MySQL`:

.. code-block:: python3

    from kleinmann import Model, fields
    from kleinmann.contrib.mysql.fields import GeometryField
    from kleinmann.contrib.mysql.indexes import FullTextIndex, SpatialIndex


    class Index(Model):
        full_text = fields.TextField()
        geometry = GeometryField()

        class Meta:
            indexes = [
                FullTextIndex(fields={"full_text"}, parser_name="ngram"),
                SpatialIndex(fields={"geometry"}),
            ]

Some built-in indexes can be found in `kleinmann.contrib.mysql.indexes` and `kleinmann.contrib.postgres.indexes`.

Extending Index
===============

Extending index is simply, you just need to inherit the `kleinmann.indexes.Index`, following is example how to create `FullTextIndex`:

.. code-block:: python3

    from typing import Optional, Set
    from pypika.terms import Term
    from kleinmann.indexes import Index

    class FullTextIndex(Index):
        INDEX_TYPE = "FULLTEXT"

        def __init__(
            self,
            *expressions: Term,
            fields: Optional[Set[str]] = None,
            name: Optional[str] = None,
            parser_name: Optional[str] = None,
        ):
            super().__init__(*expressions, fields=fields, name=name)
            if parser_name:
                self.extra = f" WITH PARSER {parser_name}"

Differently for `Postgres`, you should inherit `kleinmann.contrib.postgres.indexes.PostgresIndex`:

.. code-block:: python3

    class BloomIndex(PostgreSQLIndex):
        INDEX_TYPE = "BLOOM"
