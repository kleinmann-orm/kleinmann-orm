from typing import Any, Optional, Type, Union

from pypika import Query

from kleinmann import Model, fields
from kleinmann.backends.odbc.executor import ODBCExecutor
from kleinmann.exceptions import UnSupportedError
from kleinmann.fields import BooleanField


def to_db_bool(
    self: BooleanField, value: Optional[Union[bool, int]], instance: Union[Type[Model], Model]
) -> Optional[int]:
    if value is None:
        return None
    return int(bool(value))


class MSSQLExecutor(ODBCExecutor):
    TO_DB_OVERRIDE = {
        fields.BooleanField: to_db_bool,
    }

    async def execute_explain(self, query: Query) -> Any:
        raise UnSupportedError("MSSQL does not support explain")
