from typing import Any, Union

from kleinmann_core.enums import Dialects
from kleinmann_core.queries import Query, QueryBuilder
from kleinmann_core.utils import QueryException, builder


class MSSQLQuery(Query):
    """
    Defines a query class for use with Microsoft SQL Server.
    """

    @classmethod
    def _builder(cls, **kwargs: Any) -> "MSSQLQueryBuilder":
        return MSSQLQueryBuilder(**kwargs)


class MSSQLQueryBuilder(QueryBuilder):
    QUERY_CLS = MSSQLQuery

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(dialect=Dialects.MSSQL, **kwargs)
        self._top = None

    @builder
    def top(self, value: Union[str, int]) -> "MSSQLQueryBuilder":  # type: ignore[return]
        """
        Implements support for simple TOP clauses.

        Does not include support for PERCENT or WITH TIES.

        https://docs.microsoft.com/en-us/sql/t-sql/queries/top-transact-sql?view=sql-server-2017
        """
        try:
            self._top = int(value)  # type: ignore[assignment]
        except ValueError:
            raise QueryException("TOP value must be an integer")

    @builder
    def fetch_next(self, limit: int) -> "MSSQLQueryBuilder":  # type: ignore[return]
        # Overridden to provide a more domain-specific API for T-SQL users
        self._limit = limit  # type: ignore[assignment]

    def _offset_sql(self) -> str:
        order_by = ""
        if not self._orderbys:
            order_by = "ORDER BY (SELECT 0)"
        return order_by + " OFFSET {offset} ROWS".format(offset=self._offset or 0)

    def _limit_sql(self) -> str:
        return " FETCH NEXT {limit} ROWS ONLY".format(limit=self._limit)

    def _apply_pagination(self, querystring: str) -> str:
        # Note: Overridden as MSSQL specifies offset before the fetch next limit
        if self._limit is not None or self._offset:
            # Offset has to be present if fetch next is specified in a MSSQL query
            querystring += self._offset_sql()  # type: ignore[unreachable]

        if self._limit is not None:
            querystring += self._limit_sql()  # type: ignore[unreachable]

        return querystring

    def get_sql(self, *args: Any, **kwargs: Any) -> str:
        # MSSQL does not support group by a field alias.
        # Note: set directly in kwargs as they are re-used down the tree in the case of subqueries!
        kwargs["groupby_alias"] = False
        return super().get_sql(*args, **kwargs)

    def _top_sql(self) -> str:
        if self._top:
            return "TOP ({}) ".format(self._top)  # type: ignore[unreachable]
        else:
            return ""

    def _select_sql(self, **kwargs: Any) -> str:
        return "SELECT {distinct}{top}{select}".format(
            top=self._top_sql(),
            distinct="DISTINCT " if self._distinct else "",
            select=",".join(
                term.get_sql(with_alias=True, subquery=True, **kwargs) for term in self._selects
            ),
        )
