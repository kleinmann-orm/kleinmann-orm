"""
This is the testing Models — Cyclic
"""

from kleinmann import fields
from kleinmann.models import Model
from tests.schema.models_cyclic import Two


class One(Model):
    tournament: fields.ManyToManyRelation[Two] = fields.ManyToManyField("Two")
