import pytest

# Tagging my test case with marker
@pytest.mark.sanity
def testLogin():
    print("Login Successful")

def testLogoff():
    print("Logoff Successful")

def testCalculation():
    assert 2+2 == 4