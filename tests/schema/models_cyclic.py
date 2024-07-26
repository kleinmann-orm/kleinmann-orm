"""
This is the testing Models — Cyclic
"""

from kleinmann.models import Model

from kleinmann import fields


class One(Model):
    tournament: fields.ForeignKeyRelation["Two"] = fields.ForeignKeyField(
        "models.Two", related_name="events"
    )


class Two(Model):
    tournament: fields.ForeignKeyRelation["Three"] = fields.ForeignKeyField(
        "models.Three", related_name="events"
    )


class Three(Model):
    tournament: fields.ForeignKeyRelation[One] = fields.ForeignKeyField(
        "models.One", related_name="events"
    )
