# Any pytest file should start with test_ or end with _test
#pytest method names should start with test
#Any code should be wrapped in method only
#Method name should have sense
# -k stands for method names execution like py.test -k <functionname> -v -s, -s logs in out put  -v stands for more info metadata
#you can run specific file with py.test <filename>   like py.test <filename> -v -s 
# you can mark (tag) tests @pytest.mark.smoke and then run with -m  like py.test -m somke -v -s
#you can skip tests with @pytest.mark.skip
#@pytest.mark.xfail  here it will run but don't show in output
#fixtures are used as setup and tear down methods for test cases- conftest file to generalize fixt
#fixture and make it available to all test cases (fixture name into parameters of method)
# datadriven and parameterization can be done with return statements in tuple format
#when you define fixture scope to class only, it will run once before class is initiated and at the end


import pytest


@pytest.mark.smoke  #insted of somke we can use any name and can run like py.test -m somke -v -s
#@pytest.mark.skip
def test_firstProgram():
    msg = "Hello" #operations
    assert msg == "Hi", "Test failed because strings do not match"

@pytest.mark.xfail   # it will run but not to be reported anyware
def test_SecondGreetCreditCard():
    print("Good Morning")


def test_SecondCreditCard():
    a = 4
    b = 6
    assert a+2 == 6, "Addition do not match"


--------using usefixtures from conftest--------

import pytest

@pytest.mark.usefixtures("dataLoad")    
class TestExample2:

    def test_editProfile(self, dataLoad):   #if we are returing anything from method we should use this fixture name here even thoug we set it globally
        print(dataLoad[0])
        print(dataLoad[2])
        print(dataLoad)



--------using usefixtures in the class level and in conftest we need to set this @pytest.fixture(scope="class") and it will run only one in the starting of class and end of class--------
import pytest


@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixtureDemo(self):
        print("i will execute steps in fixtureDemo method")

    def test_fixtureDemo1(self):
        print("i will execute steps in fixtureDemo1 method")

    def test_fixtureDemo2(self):
        print("i will execute steps in fixtureDemo2 method")

    def test_fixtureDemo3(self):
        print("i will execute steps in fixtureDemo3 method")


--- if we are not declering class level we don't need to use self here----

def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])








