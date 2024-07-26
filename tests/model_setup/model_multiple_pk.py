"""
This is the testing Models — Multiple PK
"""

from kleinmann.models import Model

from kleinmann import fields


class Tournament(Model):
    id = fields.IntField(primary_key=True)
    id2 = fields.IntField(primary_key=True)
