import pytest


@pytest.fixture(scope="session", autouse=True)
def setUp(browser):

    if browser == "chrome":
        print("Launch Chrome")

    elif browser == "FireFox":
        print("Launch FireFox")

    else:
        print("Provide valid browser")

    print("Login")
    print("Browse products")
    yield
    print("Logoff")
    print("Close browser")


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="session", autouse=True)
def browser(request):
    return request.config.getoption("--browser")