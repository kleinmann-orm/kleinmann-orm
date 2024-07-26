import os

from kleinmann.exceptions import ConfigurationError

from kleinmann import Kleinmann, connections
from kleinmann.contrib import test


class TestInitErrors(test.SimpleTestCase):
    async def asyncSetUp(self):
        await super().asyncSetUp()
        try:
            Kleinmann.apps = {}
            Kleinmann._inited = False
        except ConfigurationError:
            pass
        Kleinmann._inited = False

    async def asyncTearDown(self) -> None:
        await Kleinmann._reset_apps()
        await super(TestInitErrors, self).asyncTearDown()

    async def test_basic_init(self):
        await Kleinmann.init(
            {
                "connections": {
                    "default": {
                        "engine": "kleinmann.backends.sqlite",
                        "credentials": {"file_path": ":memory:"},
                    }
                },
                "apps": {
                    "models": {"models": ["tests.testmodels"], "default_connection": "default"}
                },
            }
        )
        self.assertIn("models", Kleinmann.apps)
        self.assertIsNotNone(connections.get("default"))

    async def test_empty_modules_init(self):
        with self.assertWarnsRegex(RuntimeWarning, 'Module "tests.model_setup" has no models'):
            await Kleinmann.init(
                {
                    "connections": {
                        "default": {
                            "engine": "kleinmann.backends.sqlite",
                            "credentials": {"file_path": ":memory:"},
                        }
                    },
                    "apps": {
                        "models": {"models": ["tests.model_setup"], "default_connection": "default"}
                    },
                }
            )

    async def test_dup1_init(self):
        with self.assertRaisesRegex(
            ConfigurationError, 'backward relation "events" duplicates in model Tournament'
        ):
            await Kleinmann.init(
                {
                    "connections": {
                        "default": {
                            "engine": "kleinmann.backends.sqlite",
                            "credentials": {"file_path": ":memory:"},
                        }
                    },
                    "apps": {
                        "models": {
                            "models": ["tests.model_setup.models_dup1"],
                            "default_connection": "default",
                        }
                    },
                }
            )

    async def test_dup2_init(self):
        with self.assertRaisesRegex(
            ConfigurationError, 'backward relation "events" duplicates in model Team'
        ):
            await Kleinmann.init(
                {
                    "connections": {
                        "default": {
                            "engine": "kleinmann.backends.sqlite",
                            "credentials": {"file_path": ":memory:"},
                        }
                    },
                    "apps": {
                        "models": {
                            "models": ["tests.model_setup.models_dup2"],
                            "default_connection": "default",
                        }
                    },
                }
            )

    async def test_dup3_init(self):
        with self.assertRaisesRegex(
            ConfigurationError, 'backward relation "event" duplicates in model Tournament'
        ):
            await Kleinmann.init(
                {
                    "connections": {
                        "default": {
                            "engine": "kleinmann.backends.sqlite",
                            "credentials": {"file_path": ":memory:"},
                        }
                    },
                    "apps": {
                        "models": {
                            "models": ["tests.model_setup.models_dup3"],
                            "default_connection": "default",
                        }
                    },
                }
            )

    async def test_generated_nonint(self):
        with self.assertRaisesRegex(
            ConfigurationError, "Field 'val' \\(CharField\\) can't be DB-generated"
        ):
            await Kleinmann.init(
                {
                    "connections": {
                        "default": {
                            "engine": "kleinmann.backends.sqlite",
                            "credentials": {"file_path": ":memory:"},
                        }
                    },
                    "apps": {
                        "models": {
                            "models": ["tests.model_setup.model_generated_nonint"],
                            "default_connection": "default",
                        }
                    },
                }
            )

    async def test_multiple_pk(self):
        with self.assertRaisesRegex(
            ConfigurationError,
            "Can't create model Tournament with two primary keys, only single primary key is supported",
        ):
            await Kleinmann.init(
                {
                    "connections": {
                        "default": {
                            "engine": "kleinmann.backends.sqlite",
                            "credentials": {"file_path": ":memory:"},
                        }
                    },
                    "apps": {
                        "models": {
                            "models": ["tests.model_setup.model_multiple_pk"],
                            "default_connection": "default",
                        }
                    },
                }
            )

    async def test_nonpk_id(self):
        with self.assertRaisesRegex(
            ConfigurationError,
            "Can't create model Tournament without explicit primary key if"
            " field 'id' already present",
        ):
            await Kleinmann.init(
                {
                    "connections": {
                        "default": {
                            "engine": "kleinmann.backends.sqlite",
                            "credentials": {"file_path": ":memory:"},
                        }
                    },
                    "apps": {
                        "models": {
                            "models": ["tests.model_setup.model_nonpk_id"],
                            "default_connection": "default",
                        }
                    },
                }
            )

    async def test_unknown_connection(self):
        with self.assertRaisesRegex(
            ConfigurationError,
            "Unable to get db settings for alias 'fioop'. Please "
            "check if the config dict contains this alias and try again",
        ):
            await Kleinmann.init(
                {
                    "connections": {
                        "default": {
                            "engine": "kleinmann.backends.sqlite",
                            "credentials": {"file_path": ":memory:"},
                        }
                    },
                    "apps": {
                        "models": {"models": ["tests.testmodels"], "default_connection": "fioop"}
                    },
                }
            )

    async def test_url_without_modules(self):
        with self.assertRaisesRegex(
            ConfigurationError, 'You must specify "db_url" and "modules" together'
        ):
            await Kleinmann.init(db_url=f"sqlite://{':memory:'}")

    async def test_default_connection_init(self):
        await Kleinmann.init(
            {
                "connections": {
                    "default": {
                        "engine": "kleinmann.backends.sqlite",
                        "credentials": {"file_path": ":memory:"},
                    }
                },
                "apps": {"models": {"models": ["tests.testmodels"]}},
            }
        )
        self.assertIn("models", Kleinmann.apps)
        self.assertIsNotNone(connections.get("default"))

    async def test_db_url_init(self):
        await Kleinmann.init(
            {
                "connections": {"default": f"sqlite://{':memory:'}"},
                "apps": {
                    "models": {"models": ["tests.testmodels"], "default_connection": "default"}
                },
            }
        )
        self.assertIn("models", Kleinmann.apps)
        self.assertIsNotNone(connections.get("default"))

    async def test_shorthand_init(self):
        await Kleinmann.init(
            db_url=f"sqlite://{':memory:'}", modules={"models": ["tests.testmodels"]}
        )
        self.assertIn("models", Kleinmann.apps)
        self.assertIsNotNone(connections.get("default"))

    async def test_init_wrong_connection_engine(self):
        with self.assertRaisesRegex(ImportError, "kleinmann.backends.test"):
            await Kleinmann.init(
                {
                    "connections": {
                        "default": {
                            "engine": "kleinmann.backends.test",
                            "credentials": {"file_path": ":memory:"},
                        }
                    },
                    "apps": {
                        "models": {"models": ["tests.testmodels"], "default_connection": "default"}
                    },
                }
            )

    async def test_init_wrong_connection_engine_2(self):
        with self.assertRaisesRegex(
            ConfigurationError,
            'Backend for engine "kleinmann.backends" does not implement db client',
        ):
            await Kleinmann.init(
                {
                    "connections": {
                        "default": {
                            "engine": "kleinmann.backends",
                            "credentials": {"file_path": ":memory:"},
                        }
                    },
                    "apps": {
                        "models": {"models": ["tests.testmodels"], "default_connection": "default"}
                    },
                }
            )

    async def test_init_no_connections(self):
        with self.assertRaisesRegex(ConfigurationError, 'Config must define "connections" section'):
            await Kleinmann.init(
                {
                    "apps": {
                        "models": {"models": ["tests.testmodels"], "default_connection": "default"}
                    }
                }
            )

    async def test_init_no_apps(self):
        with self.assertRaisesRegex(ConfigurationError, 'Config must define "apps" section'):
            await Kleinmann.init(
                {
                    "connections": {
                        "default": {
                            "engine": "kleinmann.backends.sqlite",
                            "credentials": {"file_path": ":memory:"},
                        }
                    }
                }
            )

    async def test_init_config_and_config_file(self):
        with self.assertRaisesRegex(
            ConfigurationError, 'You should init either from "config", "config_file" or "db_url"'
        ):
            await Kleinmann.init(
                {
                    "connections": {
                        "default": {
                            "engine": "kleinmann.backends.sqlite",
                            "credentials": {"file_path": ":memory:"},
                        }
                    },
                    "apps": {
                        "models": {"models": ["tests.testmodels"], "default_connection": "default"}
                    },
                },
                config_file="file.json",
            )

    async def test_init_config_file_wrong_extension(self):
        with self.assertRaisesRegex(
            ConfigurationError, "Unknown config extension .ini, only .yml and .json are supported"
        ):
            await Kleinmann.init(config_file="config.ini")

    @test.skipIf(os.name == "nt", "path issue on Windows")
    async def test_init_json_file(self):
        await Kleinmann.init(config_file=os.path.dirname(__file__) + "/init.json")
        self.assertIn("models", Kleinmann.apps)
        self.assertIsNotNone(connections.get("default"))

    @test.skipIf(os.name == "nt", "path issue on Windows")
    async def test_init_yaml_file(self):
        await Kleinmann.init(config_file=os.path.dirname(__file__) + "/init.yaml")
        self.assertIn("models", Kleinmann.apps)
        self.assertIsNotNone(connections.get("default"))

    async def test_generate_schema_without_init(self):
        with self.assertRaisesRegex(
            ConfigurationError, r"You have to call \.init\(\) first before generating schemas"
        ):
            await Kleinmann.generate_schemas()

    async def test_drop_databases_without_init(self):
        with self.assertRaisesRegex(
            ConfigurationError, r"You have to call \.init\(\) first before deleting schemas"
        ):
            await Kleinmann._drop_databases()

    async def test_bad_models(self):
        with self.assertRaisesRegex(ConfigurationError, 'Module "tests.testmodels2" not found'):
            await Kleinmann.init(
                {
                    "connections": {
                        "default": {
                            "engine": "kleinmann.backends.sqlite",
                            "credentials": {"file_path": ":memory:"},
                        }
                    },
                    "apps": {
                        "models": {"models": ["tests.testmodels2"], "default_connection": "default"}
                    },
                }
            )
