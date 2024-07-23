.. _cli:

===========
KleinmannCLI
===========

This document describes how to use `kleinmann-cli`, a cli tool for kleinmann-orm, build on top of click and ptpython.

You can see `https://github.com/kleinmann/kleinmann-cli <https://github.com/kleinmann/kleinmann-cli>`_ for more details.


Quick Start
===========

.. code-block:: shell

    > kleinmann-cli -h                                                                                                                                                                 23:59:38
    Usage: kleinmann-cli [OPTIONS] COMMAND [ARGS]...

    Options:
      -V, --version      Show the version and exit.
      -c, --config TEXT  KleinmannORM config dictionary path, like settings.KLEINMANN_ORM
      -h, --help         Show this message and exit.

    Commands:
      shell  Start an interactive shell.

Usage
=====

First, you need make a KleinmannORM config object, assuming that in `settings.py`.

.. code-block:: shell

    KLEINMANN_ORM = {
        "connections": {
            "default": "sqlite://:memory:",
        },
        "apps": {
            "models": {"models": ["examples.models"], "default_connection": "default"},
        },
    }


Interactive shell
=================

Then you can start an interactive shell for KleinmannORM.

.. code-block:: shell

    kleinmann-cli -c settings.KLEINMANN_ORM shell


Or you can set config by set environment variable.

.. code-block:: shell

    export KLEINMANN_ORM=settings.KLEINMANN_ORM

Then just run:

.. code-block:: shell

    kleinmann-cli shell
