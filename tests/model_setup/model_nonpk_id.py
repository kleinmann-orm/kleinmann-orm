"""
This is the testing Models — Model with field id, but NO PK
"""

from kleinmann.models import Model

from kleinmann import fields


class Tournament(Model):
    id = fields.CharField(max_length=50)
