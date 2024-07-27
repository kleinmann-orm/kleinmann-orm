from typing import Union

from kleinmann_core.enums import Comparator
from kleinmann_core.terms import BasicCriterion, Function, Term

from kleinmann.contrib.postgres.functions import ToTsQuery, ToTsVector


class Comp(Comparator):
    search = " @@ "


class SearchCriterion(BasicCriterion):
    def __init__(self, field: Term, expr: Union[Term, Function]):
        if isinstance(expr, Function):
            _expr = expr
        else:
            _expr = ToTsQuery(expr)
        super().__init__(Comp.search, ToTsVector(field), _expr)
