"""
Testing Models for a bad/wrong relation reference
Wrong reference. o2o field parameter `to_field` with non unique field.
"""

from kleinmann.models import Model

from kleinmann import fields


class Tournament(Model):
    uuid = fields.UUIDField(unique=False)


class Event(Model):
    tournament: fields.OneToOneRelation[Tournament] = fields.OneToOneField(
        "models.Tournament", related_name="events", to_field="uuid"
    )
