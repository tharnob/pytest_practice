import pytest


@pytest.mark.regression
def testLogin():
    print("Login Successful")



# Tagging my test case with marker
@pytest.mark.sanity
def testLogoff():
    print("Logoff Successful")

def testCalculation():
    assert 2+2 == 4