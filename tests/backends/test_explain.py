from kleinmann.contrib import test
from kleinmann.contrib.test.condition import NotEQ
from tests.testmodels import Tournament


class TestExplain(test.TestCase):
    @test.requireCapability(dialect=NotEQ("mssql"))
    async def test_explain(self):
        # NOTE: we do not provide any guarantee on the format of the value
        # returned by `.explain()`, as it heavily depends on the database.
        # This test merely checks that one is able to run `.explain()`
        # without errors for each backend.
        plan = await Tournament.all().explain()
        # This should have returned *some* information.
        self.assertGreater(len(str(plan)), 20)
