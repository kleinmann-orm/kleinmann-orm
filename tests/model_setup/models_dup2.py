"""
This is the testing Models — Duplicate 1
"""

from kleinmann import fields
from kleinmann.models import Model


class Event(Model):
    participants: fields.ManyToManyRelation["Team"] = fields.ManyToManyField(
        "models.Team", related_name="events", through="event_team"
    )


class Party(Model):
    participants: fields.ManyToManyRelation["Team"] = fields.ManyToManyField(
        "models.Team", related_name="events", through="event_team"
    )


class Team(Model):
    id = fields.IntField(primary_key=True)
