import os

import pytest

from kleinmann.contrib.test import finalizer, initializer


@pytest.fixture(scope="session", autouse=True)
def initialize_tests(request):
    db_url = os.getenv("KLEINMANN_TEST_DB", "sqlite://:memory:")
    initializer(["tests.testmodels"], db_url=db_url)
    request.addfinalizer(finalizer)
