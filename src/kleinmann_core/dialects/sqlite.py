from typing import Any

from kleinmann_core.enums import Dialects
from kleinmann_core.queries import Query, QueryBuilder
from kleinmann_core.terms import ValueWrapper


class SQLiteValueWrapper(ValueWrapper):
    def get_value_sql(self, **kwargs: Any) -> str:
        if isinstance(self.value, bool):
            return "1" if self.value else "0"
        return super().get_value_sql(**kwargs)


class SQLiteQuery(Query):
    """
    Defines a query class for use with Microsoft SQL Server.
    """

    @classmethod
    def _builder(cls, **kwargs: Any) -> "SQLiteQueryBuilder":
        return SQLiteQueryBuilder(**kwargs)  # type: ignore[no-untyped-call]


class SQLiteQueryBuilder(QueryBuilder):
    QUERY_CLS = SQLiteQuery

    def __init__(self, **kwargs):
        super(SQLiteQueryBuilder, self).__init__(
            dialect=Dialects.SQLITE, wrapper_cls=SQLiteValueWrapper, **kwargs
        )

    def get_sql(self, **kwargs: Any) -> str:  # type: ignore[override]
        self._set_kwargs_defaults(kwargs)
        if not (self._selects or self._insert_table or self._delete_from or self._update_table):
            return ""
        if self._insert_table and not (self._selects or self._values):  # type: ignore[unreachable]
            return ""  # type: ignore[unreachable]
        if self._update_table and not self._updates:  # type: ignore[unreachable]
            return ""  # type: ignore[unreachable]

        has_joins = bool(self._joins)
        has_multiple_from_clauses = 1 < len(self._from)
        has_subquery_from_clause = 0 < len(self._from) and isinstance(self._from[0], QueryBuilder)
        has_reference_to_foreign_table = self._foreign_table
        has_update_from = self._update_table and self._from  # type: ignore[unreachable]

        kwargs["with_namespace"] = any(
            [
                has_joins,
                has_multiple_from_clauses,
                has_subquery_from_clause,
                has_reference_to_foreign_table,
                has_update_from,
            ]
        )
        if self._update_table:
            if self._with:  # type: ignore[unreachable]
                querystring = self._with_sql(**kwargs)
            else:
                querystring = ""

            querystring += self._update_sql(**kwargs)

            querystring += self._set_sql(**kwargs)

            if self._joins:
                self._from.append(self._update_table.as_(self._update_table.get_table_name() + "_"))

            if self._from:
                querystring += self._from_sql(**kwargs)
            if self._joins:
                querystring += " " + " ".join(join.get_sql(**kwargs) for join in self._joins)

            if self._wheres:
                querystring += self._where_sql(**kwargs)

            if self._orderbys:
                querystring += self._orderby_sql(**kwargs)
            if self._limit:
                querystring += self._limit_sql()
        else:
            querystring = super(SQLiteQueryBuilder, self).get_sql(**kwargs)
        return querystring
