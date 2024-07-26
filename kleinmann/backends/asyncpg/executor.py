from typing import Optional

import asyncpg
from kleinmann.backends.base_postgres.executor import BasePostgresExecutor

from kleinmann import Model


class AsyncpgExecutor(BasePostgresExecutor):
    async def _process_insert_result(
        self, instance: Model, results: Optional[asyncpg.Record]
    ) -> None:
        return await super()._process_insert_result(instance, results)
