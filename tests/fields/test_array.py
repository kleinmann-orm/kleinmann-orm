from kleinmann.contrib import test
from kleinmann.exceptions import IntegrityError, OperationalError
from tests import testmodels_postgres as testmodels


@test.requireCapability(dialect="postgres")
class TestArrayFields(test.IsolatedTestCase):
    kleinmann_test_modules = ["tests.testmodels_postgres"]

    async def _setUpDB(self) -> None:
        try:
            await super()._setUpDB()
        except OperationalError:
            raise test.SkipTest("Works only with PostgreSQL")

    async def test_empty(self):
        with self.assertRaises(IntegrityError):
            await testmodels.ArrayFields.create()

    async def test_create(self):
        obj0 = await testmodels.ArrayFields.create(array=[0])
        obj = await testmodels.ArrayFields.get(id=obj0.id)
        self.assertEqual(obj.array, [0])
        self.assertIs(obj.array_null, None)
        await obj.save()
        obj2 = await testmodels.ArrayFields.get(id=obj.id)
        self.assertEqual(obj, obj2)

    async def test_update(self):
        obj0 = await testmodels.ArrayFields.create(array=[0])
        await testmodels.ArrayFields.filter(id=obj0.id).update(array=[1])
        obj = await testmodels.ArrayFields.get(id=obj0.id)
        self.assertEqual(obj.array, [1])
        self.assertIs(obj.array_null, None)

    async def test_values(self):
        obj0 = await testmodels.ArrayFields.create(array=[0])
        values = await testmodels.ArrayFields.get(id=obj0.id).values("array")
        self.assertEqual(values["array"], [0])

    async def test_values_list(self):
        obj0 = await testmodels.ArrayFields.create(array=[0])
        values = await testmodels.ArrayFields.get(id=obj0.id).values_list("array", flat=True)
        self.assertEqual(values, [0])
