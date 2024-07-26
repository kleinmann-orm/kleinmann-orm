"""
This example to use router to implement read/write separation
"""

from typing import Type

from kleinmann.models import Model

from kleinmann import Kleinmann, fields, run_async


class Event(Model):
    id = fields.IntField(primary_key=True)
    name = fields.TextField()
    datetime = fields.DatetimeField(null=True)

    class Meta:
        table = "event"

    def __str__(self):
        return self.name


class Router:
    def db_for_read(self, model: Type[Model]):
        return "slave"

    def db_for_write(self, model: Type[Model]):
        return "master"


async def run():
    config = {
        "connections": {"master": "sqlite:///tmp/test.db", "slave": "sqlite:///tmp/test.db"},
        "apps": {
            "models": {
                "models": ["__main__"],
                "default_connection": "master",
            }
        },
        "routers": ["__main__.Router"],
        "use_tz": False,
        "timezone": "UTC",
    }
    await Kleinmann.init(config=config)
    await Kleinmann.generate_schemas()
    # this will use connection master
    event = await Event.create(name="Test")
    # this will use connection slave
    await Event.get(pk=event.pk)


if __name__ == "__main__":
    run_async(run())
