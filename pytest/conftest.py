import pytest
#if you want to give a scope in class you should create a excat file name with conftest.py then this will fixture will be availabe all pytest file in the specfic folder 

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
def crossBrowser(request):
    return request.param
