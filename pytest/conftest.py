import pytest
#if you want to declear fixture, create a excat file name with conftest.py then this will fixture will be availabe all pytest file in the specfic folder 
#if you used scope="class" it will run only one before and after the class:
@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")    #this will run as prerequist steps in function
    yield                                 # you can define anything that you want to execute after your menthod like closeing browser you can define after this yield keyword
    print(" I will execute last")


@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ["Rahul","Shetty","rahulshettyacademy.com"]


@pytest.fixture(params=[("chrome","Rahul","shetty"), ("Firefox","shetty"), ("IE","SS")])
def crossBrowser(request):   # we need to use request in Parameterizing test with multiple data sets using Fixtures
    return request.param
