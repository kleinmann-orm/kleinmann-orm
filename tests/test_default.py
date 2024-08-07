import datetime
from decimal import Decimal

import pytz

from kleinmann.backends.asyncpg import AsyncpgDBClient
from kleinmann.backends.sqlite import SqliteClient
from kleinmann.contrib import test
from tests.testmodels import DefaultModel


class TestDefault(test.TestCase):
    async def asyncSetUp(self) -> None:
        await super(TestDefault, self).asyncSetUp()
        db = self._db
        if isinstance(db, SqliteClient):
            await db.execute_query(
                "insert into defaultmodel default values",
            )
        elif isinstance(db, AsyncpgDBClient):
            await db.execute_query(
                'insert into defaultmodel ("int_default","float_default","decimal_default","bool_default","char_default","date_default","datetime_default") values (DEFAULT,DEFAULT,DEFAULT,DEFAULT,DEFAULT,DEFAULT,DEFAULT)',
            )

    async def test_default(self):
        default_model = await DefaultModel.first()
        self.assertEqual(default_model.int_default, 1)
        self.assertEqual(default_model.float_default, 1.5)
        self.assertEqual(default_model.decimal_default, Decimal(1))
        self.assertTrue(default_model.bool_default)
        self.assertEqual(default_model.char_default, "kleinmann")
        self.assertEqual(default_model.date_default, datetime.date(year=2020, month=5, day=21))
        self.assertEqual(
            default_model.datetime_default,
            datetime.datetime(year=2020, month=5, day=20, tzinfo=pytz.utc),
        )
