========
Timezone
========

.. _timezone:

Introduction
============
The design of timezone is inspired by `Django` but also has differences. There are two config items `use_tz` and `timezone` affect timezone in kleinmann, which can be set when call `Kleinmann.init`. And in different DBMS there also are different behaviors.

use_tz
------
When set `use_tz = True`, `kleinmann` will always store `UTC` time in database no matter what `timezone` set. And `MySQL` use field type `DATETIME(6)`, `PostgreSQL` use `TIMESTAMPTZ`, `SQLite` use `TIMESTAMP` when generate schema.
For `TimeField`, `MySQL` use `TIME(6)`, `PostgreSQL` use `TIMETZ` and `SQLite` use `TIME`.

timezone
--------
The `timezone` determine what `timezone` is when select `DateTimeField` and `TimeField` from database, no matter what `timezone` your database is. And you should use `kleinmann.timezone.now()` get aware time instead of native time `datetime.datetime.now()`.

Reference
=========

.. automodule:: kleinmann.timezone
    :members:
    :undoc-members:
