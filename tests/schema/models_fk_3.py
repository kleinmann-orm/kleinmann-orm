"""
This is the testing Models — on_delete SET_NULL without null=True
"""

from kleinmann.models import Model

from kleinmann import fields
from tests.schema.models_cyclic import Two


class One(Model):
    tournament: fields.ForeignKeyRelation[Two] = fields.ForeignKeyField(
        "models.Two", on_delete=fields.SET_NULL
    )
