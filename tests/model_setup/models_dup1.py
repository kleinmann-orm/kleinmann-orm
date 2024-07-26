"""
This is the testing Models — Duplicate 1
"""

from kleinmann.models import Model

from kleinmann import fields


class Tournament(Model):
    id = fields.IntField(primary_key=True)


class Event(Model):
    tournament: fields.ForeignKeyRelation[Tournament] = fields.ForeignKeyField(
        "models.Tournament", related_name="events"
    )


class Party(Model):
    tournament: fields.ForeignKeyRelation[Tournament] = fields.ForeignKeyField(
        "models.Tournament", related_name="events"
    )
