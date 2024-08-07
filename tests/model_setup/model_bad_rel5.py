"""
Testing Models for a bad/wrong relation reference
Wrong reference. App missing.
"""

from kleinmann import fields
from kleinmann.models import Model


class Tournament(Model):
    id = fields.IntField(primary_key=True)


class Event(Model):
    tournament: fields.OneToOneRelation[Tournament] = fields.OneToOneField("Tournament")
