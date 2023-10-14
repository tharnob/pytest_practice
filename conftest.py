import pytest


@pytest.fixture(scope="function", autouse=True)
def setUp():
    print("Launch Browser")
    print("Login")
    print("Browse products")
    yield
    print("Logoff")
    print("Close browser")