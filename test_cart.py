import pytest


@pytest.fixture
def setUp():
    print("Launch Browser")
    print("Login")
    print("Browse products")
    yield
    print("Logoff")
    print("Close browser")


def testAddItemCart(setUp):
    print("Add Item Successful")

def testRemoveItemFromCart(setUp):
    print("Remove Item Successful")