"""
Tests for __models__
"""

import re
from unittest.mock import AsyncMock, patch

from kleinmann.exceptions import ConfigurationError
from kleinmann.utils import get_schema_sql

from kleinmann import Kleinmann, connections
from kleinmann.contrib import test


class TestGenerateSchema(test.SimpleTestCase):
    async def asyncSetUp(self):
        await super().asyncSetUp()
        try:
            Kleinmann.apps = {}
            Kleinmann._inited = False
        except ConfigurationError:
            pass
        Kleinmann._inited = False
        self.sqls = ""
        self.post_sqls = ""
        self.engine = test.getDBConfig(app_label="models", modules=[])["connections"]["models"][
            "engine"
        ]

    async def asyncTearDown(self) -> None:
        await Kleinmann._reset_apps()

    async def init_for(self, module: str, safe=False) -> None:
        if self.engine != "kleinmann.backends.sqlite":
            raise test.SkipTest("sqlite only")
        with patch(
            "kleinmann.backends.sqlite.client.SqliteClient.create_connection", new=AsyncMock()
        ):
            await Kleinmann.init(
                {
                    "connections": {
                        "default": {
                            "engine": "kleinmann.backends.sqlite",
                            "credentials": {"file_path": ":memory:"},
                        }
                    },
                    "apps": {"models": {"models": [module], "default_connection": "default"}},
                }
            )
            self.sqls = get_schema_sql(connections.get("default"), safe).split(";\n")

    def get_sql(self, text: str) -> str:
        return str(re.sub(r"[ \t\n\r]+", " ", [sql for sql in self.sqls if text in sql][0]))

    async def test_good(self):
        await self.init_for("tests.model_setup.models__models__good")
        self.assertIn("goodtournament", "; ".join(self.sqls))
        self.assertIn("inaclasstournament", "; ".join(self.sqls))
        self.assertNotIn("badtournament", "; ".join(self.sqls))

    async def test_bad(self):
        await self.init_for("tests.model_setup.models__models__bad")
        self.assertNotIn("goodtournament", "; ".join(self.sqls))
        self.assertNotIn("inaclasstournament", "; ".join(self.sqls))
        self.assertIn("badtournament", "; ".join(self.sqls))
