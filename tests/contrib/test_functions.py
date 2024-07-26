from kleinmann import connections
from kleinmann.contrib import test
from kleinmann.contrib.postgres.functions import Random as PostgresRandom
from kleinmann.contrib.sqlite.functions import Random as SqliteRandom
from tests.testmodels import IntFields


class TestFunction(test.TestCase):
    async def asyncSetUp(self):
        await super().asyncSetUp()
        self.intfields = [await IntFields.create(intnum=val) for val in range(10)]
        self.db = connections.get("models")

    @test.requireCapability(dialect="postgres")
    async def test_postgres_func_rand(self):
        sql = IntFields.all().annotate(randnum=PostgresRandom()).values("intnum", "randnum").sql()
        expected_sql = 'SELECT "intnum" "intnum",RANDOM() "randnum" FROM "intfields"'
        self.assertEqual(sql, expected_sql)

    @test.requireCapability(dialect="sqlite")
    async def test_sqlite_func_rand(self):
        sql = IntFields.all().annotate(randnum=SqliteRandom()).values("intnum", "randnum").sql()
        expected_sql = 'SELECT "intnum" "intnum",RANDOM() "randnum" FROM "intfields"'
        self.assertEqual(sql, expected_sql)
