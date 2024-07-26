"""
'Failure' tests for __models__
"""

from kleinmann.models import Model

from kleinmann import fields


class BadTournament(Model):
    id = fields.IntField(primary_key=True)
    name = fields.TextField()
    created = fields.DatetimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return self.name


class GoodTournament(Model):
    id = fields.IntField(primary_key=True)
    name = fields.TextField()
    created = fields.DatetimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return self.name


class Tmp:
    class InAClassTournament(Model):
        id = fields.IntField(primary_key=True)
        name = fields.TextField()
        created = fields.DatetimeField(auto_now_add=True, db_index=True)

        def __str__(self):
            return self.name


__models__ = [BadTournament]
