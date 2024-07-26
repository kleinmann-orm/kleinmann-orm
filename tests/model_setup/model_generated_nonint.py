"""
This is the testing Models — Generated non-int PK
"""

from kleinmann.models import Model

from kleinmann import fields


class Tournament(Model):
    val = fields.CharField(max_length=50, primary_key=True, generated=True)
