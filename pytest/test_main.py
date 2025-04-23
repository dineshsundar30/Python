'''
# Any pytest file should start with test_ or end with _test
#pytest method names should start with test
#Any code should be wrapped in method only
#Method name should have sense
#to run all the function file in a directory -->py.test
#you can run specific file with py.test <filename>   like py.test <filename> -v -s
# -k stands for method names execution like py.test -k <functionname> -v -s    #--->s to print all counsol logs in out put,  -v stands for verbose to provide more info metadata and here you can pass the partial name for your function name will run all the method which is having  the key word
here using this -k we can run methods from different files where that particular menthod have that keyword
# you can mark (tag) tests @pytest.mark.smoke and then run with -m which is stands for mark like py.test -m somke -v -s
#you can skip tests with @pytest.mark.skip  then run the all the test cases with <py.test -v -s> all will run except this function
#@pytest.mark.xfail  here it will run but don't show in output pass or fail
#fixtures are used as setup and tear down methods for test cases- conftest file to generalize fixt
#fixture and make it available to all test cases (fixture name into parameters of method)
# datadriven and parameterization can be done with return statements in tuple format
#when you define fixture scope to class only, it will run once before class is initiated and at the end
'''

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
---------------------------------------------------------
#Fixture

@pytest.fixture()
def setup():
    print("I will be executing first")    #this will run as prerequist steps in function
    yield                                 # you can define anything that you want to execute after your menthod like closeing browser you can define after this yield keyword
    print(" I will execute last")    
def test_fixtureDemo(setup):
        print("i will execute steps in fixtureDemo method")


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


--- if we are not declering class level we don't need to use self here and we need to pass that fixture in all methods in this ----

def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])








