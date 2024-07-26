"""
This example demonstrates how you can use transactions with kleinmann
"""

from kleinmann.exceptions import OperationalError
from kleinmann.models import Model
from kleinmann.transactions import atomic, in_transaction

from kleinmann import Kleinmann, fields, run_async


class Event(Model):
    id = fields.IntField(primary_key=True)
    name = fields.TextField()

    class Meta:
        table = "event"

    def __str__(self):
        return self.name


async def run():
    await Kleinmann.init(db_url="sqlite://:memory:", modules={"models": ["__main__"]})
    await Kleinmann.generate_schemas()

    try:
        async with in_transaction() as connection:
            event = Event(name="Test")
            await event.save(using_db=connection)
            await Event.filter(id=event.id).using_db(connection).update(name="Updated name")
            saved_event = await Event.filter(name="Updated name").using_db(connection).first()
            await connection.execute_query("SELECT * FROM non_existent_table")
    except OperationalError:
        pass
    saved_event = await Event.filter(name="Updated name").first()
    print(saved_event)

    @atomic()
    async def bound_to_fall():
        event = await Event.create(name="Test")
        await Event.filter(id=event.id).update(name="Updated name")
        saved_event = await Event.filter(name="Updated name").first()
        print(saved_event.name)
        raise OperationalError()

    try:
        await bound_to_fall()
    except OperationalError:
        pass
    saved_event = await Event.filter(name="Updated name").first()
    print(saved_event)


if __name__ == "__main__":
    run_async(run())
