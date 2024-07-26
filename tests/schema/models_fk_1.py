"""
This is the testing Models — FK bad model name
"""

from typing import Any

from kleinmann.models import Model

from kleinmann import fields


class One(Model):
    tournament: fields.ForeignKeyRelation[Any] = fields.ForeignKeyField("moo")
