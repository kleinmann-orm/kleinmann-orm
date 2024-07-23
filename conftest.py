import os

import pytest

from kleinmann.contrib.test import finalizer, initializer


@pytest.fixture(scope="session", autouse=True)
def initialize_tests(request):
    # Reduce the default timeout for psycopg because the tests become very slow otherwise
    try:
        from kleinmann.backends.psycopg import PsycopgClient

        PsycopgClient.default_timeout = float(os.environ.get("KLEINMANN_POSTGRES_TIMEOUT", "15"))
    except ImportError:
        pass

    db_url = os.getenv("KLEINMANN_TEST_DB", "sqlite://:memory:")
    initializer(["tests.testmodels"], db_url=db_url)
    request.addfinalizer(finalizer)
