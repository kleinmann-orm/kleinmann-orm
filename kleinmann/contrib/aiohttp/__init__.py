from types import ModuleType
from typing import Dict, Iterable, Optional, Union

from aiohttp import web  # pylint: disable=E0401

from kleinmann import Kleinmann, connections
from kleinmann.log import logger


def register_kleinmann(
    app: web.Application,
    config: Optional[dict] = None,
    config_file: Optional[str] = None,
    db_url: Optional[str] = None,
    modules: Optional[Dict[str, Iterable[Union[str, ModuleType]]]] = None,
    generate_schemas: bool = False,
) -> None:
    """
    Registers ``on_startup`` and ``on_shutdown`` hooks to set-up and tear-down
    Kleinmann-ORM inside a Aiohttp webserver.

    You can configure using only one of ``config``, ``config_file``
    and ``(db_url, modules)``.

    Parameters
    ----------
    app:
        Aiohttp app.
    config:
        Dict containing config:

        Example
        -------

        .. code-block:: python3

            {
                'connections': {
                    # Dict format for connection
                    'default': {
                        'engine': 'kleinmann.backends.asyncpg',
                        'credentials': {
                            'host': 'localhost',
                            'port': '5432',
                            'user': 'kleinmann',
                            'password': 'qwerty123',
                            'database': 'test',
                        }
                    },
                    # Using a DB_URL string
                    'default': 'postgres://postgres:qwerty123@localhost:5432/events'
                },
                'apps': {
                    'models': {
                        'models': ['__main__'],
                        # If no default_connection specified, defaults to 'default'
                        'default_connection': 'default',
                    }
                }
            }

    config_file:
        Path to .json or .yml (if PyYAML installed) file containing config with
        same format as above.
    db_url:
        Use a DB_URL string. See :ref:`db_url`
    modules:
        Dictionary of ``key``: [``list_of_modules``] that defined "apps" and modules that
        should be discovered for models.
    generate_schemas:
        True to generate schema immediately. Only useful for dev environments
        or SQLite ``:memory:`` databases

    Raises
    ------
    ConfigurationError
        For any configuration error
    """

    async def init_orm(app):  # pylint: disable=W0612
        await Kleinmann.init(config=config, config_file=config_file, db_url=db_url, modules=modules)
        logger.info(f"Kleinmann-ORM started, {connections._get_storage()}, {Kleinmann.apps}")
        if generate_schemas:
            logger.info("Kleinmann-ORM generating schema")
            await Kleinmann.generate_schemas()

    async def close_orm(app):  # pylint: disable=W0612
        await connections.close_all()
        logger.info("Kleinmann-ORM shutdown")

    app.on_startup.append(init_orm)
    app.on_cleanup.append(close_orm)
