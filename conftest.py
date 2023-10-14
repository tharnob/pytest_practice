import pytest


@pytest.fixture(scope="function", autouse=False)
def setUp():
    print("Launch Browser")
    print("Login")
    print("Browse products")
    yield
    print("Logoff")
    print("Close browser")