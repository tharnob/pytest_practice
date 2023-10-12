import pytest




@pytest.mark.skip
def testLogin():
    print("Login Successful")


def testLogoff():
    print("Logoff Successful")


@pytest.mark.xfail
def testCalculation():
    assert 2+2 == 5