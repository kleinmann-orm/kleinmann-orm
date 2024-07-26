"""
This is the testing Models — Multiple PK
"""

from kleinmann import fields
from kleinmann.models import Model


class Tournament(Model):
    id = fields.IntField(primary_key=True)
    id2 = fields.IntField(primary_key=True)
