"""
This example showcases postgres features
"""

from kleinmann.models import Model

from kleinmann import Kleinmann, fields, run_async


class Report(Model):
    id = fields.IntField(primary_key=True)
    content = fields.JSONField()

    def __str__(self):
        return str(self.id)


async def run():
    await Kleinmann.init(
        {
            "connections": {
                "default": {
                    "engine": "kleinmann.backends.asyncpg",
                    "credentials": {
                        "host": "localhost",
                        "port": "5432",
                        "user": "kleinmann",
                        "password": "qwerty123",
                        "database": "test",
                    },
                }
            },
            "apps": {"models": {"models": ["__main__"], "default_connection": "default"}},
        },
        _create_db=True,
    )
    await Kleinmann.generate_schemas()

    report_data = {"foo": "bar"}
    print(await Report.create(content=report_data))
    print(await Report.filter(content=report_data).first())
    await Kleinmann._drop_databases()


if __name__ == "__main__":
    run_async(run())
