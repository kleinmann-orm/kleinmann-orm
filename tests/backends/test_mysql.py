"""
Test some mysql-specific features
"""

import ssl

from kleinmann import Kleinmann
from kleinmann.contrib import test


class TestMySQL(test.SimpleTestCase):
    async def asyncSetUp(self):
        if Kleinmann._inited:
            await self._tearDownDB()
        self.db_config = test.getDBConfig(app_label="models", modules=["tests.testmodels"])
        if self.db_config["connections"]["models"]["engine"] != "kleinmann.backends.mysql":
            raise test.SkipTest("MySQL only")

    async def asyncTearDown(self) -> None:
        if Kleinmann._inited:
            await Kleinmann._drop_databases()
        await super().asyncTearDown()

    async def test_bad_charset(self):
        self.db_config["connections"]["models"]["credentials"]["charset"] = "terrible"
        with self.assertRaisesRegex(ConnectionError, "Unknown charset"):
            await Kleinmann.init(self.db_config, _create_db=True)

    async def test_ssl_true(self):
        self.db_config["connections"]["models"]["credentials"]["ssl"] = True
        try:
            await Kleinmann.init(self.db_config, _create_db=True)
        except (ConnectionError, ssl.SSLError):
            pass
        else:
            self.assertFalse(True, "Expected ConnectionError or SSLError")

    async def test_ssl_custom(self):
        # Expect connectionerror or pass
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        self.db_config["connections"]["models"]["credentials"]["ssl"] = ctx
        try:
            await Kleinmann.init(self.db_config, _create_db=True)
        except ConnectionError:
            pass
