"""
This is the testing Models — Generated non-int PK
"""

from kleinmann import fields
from kleinmann.models import Model


class Tournament(Model):
    val = fields.CharField(max_length=50, primary_key=True, generated=True)
