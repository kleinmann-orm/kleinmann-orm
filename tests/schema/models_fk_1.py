"""
This is the testing Models — FK bad model name
"""

from typing import Any

from kleinmann import fields
from kleinmann.models import Model


class One(Model):
    tournament: fields.ForeignKeyRelation[Any] = fields.ForeignKeyField("moo")
