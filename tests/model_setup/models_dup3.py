"""
This is the testing Models — Duplicate 3
"""

from kleinmann import fields
from kleinmann.models import Model


class Tournament(Model):
    id = fields.IntField(primary_key=True)
    event = fields.CharField(max_length=32)


class Event(Model):
    tournament: fields.OneToOneRelation[Tournament] = fields.OneToOneField(
        "models.Tournament", related_name="event"
    )
