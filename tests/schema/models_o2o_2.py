"""
This is the testing Models — Bad on_delete parameter
"""

from kleinmann import fields
from kleinmann.models import Model
from tests.schema.models_cyclic import Two


class One(Model):
    tournament: fields.OneToOneRelation[Two] = fields.OneToOneField(
        "models.Two", on_delete="WABOOM"  # type:ignore
    )
