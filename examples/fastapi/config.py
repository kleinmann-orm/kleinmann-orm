import os
from functools import partial

from kleinmann.contrib.fastapi import RegisterKleinmann

register_orm = partial(
    RegisterKleinmann,
    db_url=os.getenv("DB_URL", "sqlite://db.sqlite3"),
    modules={"models": ["models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
