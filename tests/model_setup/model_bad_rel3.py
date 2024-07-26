"""
Testing Models for a bad/wrong relation reference
Wrong reference. App missing.
"""

from kleinmann.models import Model

from kleinmann import fields


class Tournament(Model):
    id = fields.IntField(primary_key=True)


class Event(Model):
    tournament: fields.ForeignKeyRelation[Tournament] = fields.ForeignKeyField(
        "Tournament", related_name="events"
    )
