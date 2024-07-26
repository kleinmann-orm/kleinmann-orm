"""
Testing Models for a bad/wrong relation reference
Wrong reference. fk field parameter `to_field` with non exist field.
"""

from kleinmann.models import Model

from kleinmann import fields


class Tournament(Model):
    uuid = fields.UUIDField(unique=True)


class Event(Model):
    tournament: fields.ForeignKeyRelation[Tournament] = fields.ForeignKeyField(
        "models.Tournament", related_name="events", to_field="uuids"
    )
