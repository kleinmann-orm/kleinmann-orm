from kleinmann.contrib.postgres.fields import ArrayField

from kleinmann import Model, fields


class ArrayFields(Model):
    id = fields.IntField(primary_key=True)
    array = ArrayField()
    array_null = ArrayField(null=True)
