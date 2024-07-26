from kleinmann.exceptions import ConfigurationError

from kleinmann import Kleinmann
from kleinmann.contrib import test


class TestBadRelationReferenceErrors(test.SimpleTestCase):
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
        await super(TestBadRelationReferenceErrors, self).asyncTearDown()

    async def test_wrong_app_init(self):
        with self.assertRaisesRegex(ConfigurationError, "No app with name 'app' registered."):
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
                            "models": ["tests.model_setup.model_bad_rel1"],
                            "default_connection": "default",
                        }
                    },
                }
            )

    async def test_wrong_model_init(self):
        with self.assertRaisesRegex(
            ConfigurationError, "No model with name 'Tour' registered in app 'models'."
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
                            "models": ["tests.model_setup.model_bad_rel2"],
                            "default_connection": "default",
                        }
                    },
                }
            )

    async def test_no_app_in_reference_init(self):
        with self.assertRaisesRegex(
            ConfigurationError, 'ForeignKeyField accepts model name in format "app.Model"'
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
                            "models": ["tests.model_setup.model_bad_rel3"],
                            "default_connection": "default",
                        }
                    },
                }
            )

    async def test_more_than_two_dots_in_reference_init(self):
        with self.assertRaisesRegex(
            ConfigurationError, 'ForeignKeyField accepts model name in format "app.Model"'
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
                            "models": ["tests.model_setup.model_bad_rel4"],
                            "default_connection": "default",
                        }
                    },
                }
            )

    async def test_no_app_in_o2o_reference_init(self):
        with self.assertRaisesRegex(
            ConfigurationError, 'OneToOneField accepts model name in format "app.Model"'
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
                            "models": ["tests.model_setup.model_bad_rel5"],
                            "default_connection": "default",
                        }
                    },
                }
            )

    async def test_non_unique_field_in_fk_reference_init(self):
        with self.assertRaisesRegex(
            ConfigurationError, 'field "uuid" in model "Tournament" is not unique'
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
                            "models": ["tests.model_setup.model_bad_rel6"],
                            "default_connection": "default",
                        }
                    },
                }
            )

    async def test_non_exist_field_in_fk_reference_init(self):
        with self.assertRaisesRegex(
            ConfigurationError, 'there is no field named "uuids" in model "Tournament"'
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
                            "models": ["tests.model_setup.model_bad_rel7"],
                            "default_connection": "default",
                        }
                    },
                }
            )

    async def test_non_unique_field_in_o2o_reference_init(self):
        with self.assertRaisesRegex(
            ConfigurationError, 'field "uuid" in model "Tournament" is not unique'
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
                            "models": ["tests.model_setup.model_bad_rel8"],
                            "default_connection": "default",
                        }
                    },
                }
            )

    async def test_non_exist_field_in_o2o_reference_init(self):
        with self.assertRaisesRegex(
            ConfigurationError, 'there is no field named "uuids" in model "Tournament"'
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
                            "models": ["tests.model_setup.model_bad_rel9"],
                            "default_connection": "default",
                        }
                    },
                }
            )
