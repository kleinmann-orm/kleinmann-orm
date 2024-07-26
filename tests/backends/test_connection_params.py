from unittest.mock import AsyncMock, patch

import asyncpg

from kleinmann import connections
from kleinmann.contrib import test


class TestConnectionParams(test.SimpleTestCase):
    async def asyncSetUp(self) -> None:
        await super().asyncSetUp()

    async def asyncTearDown(self) -> None:
        await super().asyncTearDown()

    async def test_asyncpg_connection_params(self):
        try:
            with patch(
                "kleinmann.backends.asyncpg.client.asyncpg.create_pool", new=AsyncMock()
            ) as asyncpg_connect:
                await connections._init(
                    {
                        "models": {
                            "engine": "kleinmann.backends.asyncpg",
                            "credentials": {
                                "database": "test",
                                "host": "127.0.0.1",
                                "password": "foomip",
                                "port": 5432,
                                "user": "root",
                                "timeout": 30,
                                "ssl": True,
                            },
                        }
                    },
                    False,
                )
                await connections.get("models").create_connection(with_db=True)

                asyncpg_connect.assert_awaited_once_with(  # nosec
                    None,
                    database="test",
                    host="127.0.0.1",
                    password="foomip",
                    port=5432,
                    ssl=True,
                    timeout=30,
                    user="root",
                    max_size=5,
                    min_size=1,
                    connection_class=asyncpg.connection.Connection,
                    loop=None,
                    server_settings={},
                )
        except ImportError:
            self.skipTest("asyncpg not installed")
