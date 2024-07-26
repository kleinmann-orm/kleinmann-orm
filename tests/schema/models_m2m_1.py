"""
This is the testing Models — Cyclic
"""

from kleinmann.models import Model

from kleinmann import fields
from tests.schema.models_cyclic import Two


class One(Model):
    tournament: fields.ManyToManyRelation[Two] = fields.ManyToManyField("Two")
