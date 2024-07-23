"""
Testing Models for a bad/wrong relation reference
The model 'Tour' does not exist
"""

from typing import Any

from kleinmann import fields
from kleinmann.models import Model


class Tournament(Model):
    id = fields.IntField(primary_key=True)


class Event(Model):
    tournament: fields.ForeignKeyRelation["Any"] = fields.ForeignKeyField(
        "models.Tour", related_name="events"
    )
