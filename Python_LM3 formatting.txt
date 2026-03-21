string formating

name = "dinesh"
like1 = "banana"
like2 = "apples"

test = '{} likes {} and {} ' 
print(text.format(name,like1,like2))

-----------------------------------------


print('{} likes {} and {}'.format(name,like1,like2))

----------------------------------------------------

test = '{0} likes {1} and {2} ' 
print(text.format(name,like1,like2))

or

test = '{0} likes {2} and {1} ' 
print(text.format(name,like1,like2))

------------------------------------------------------

test = '{name} likes {like1} and {like22}' 
print(text.format(name="dinesh",like1="apple",like2="banana"))
print(text.format(name="dinesh",like2="apple",like1="banana"))



******************************************************************

padding


print("********{msg}*********".format(msg="welcome"))

print("********{msg:20}*********".format(msg="welcome"))

left align
print("********{msg:<20}*********".format(msg="welcome"))

right align
print("********{msg:>20}*********".format(msg="welcome"))

center align
print("********{msg:^20}*********".format(msg="welcome"))

------------
print("********{:^20}*********".format("welcome"))


-------------------------------------------------------------------------------------

formatting number

pi = 3.14159

print("this val of pi is {:.2f}".format(pi))

print("this val of pi is {:.3f}".format(pi))
--------------------------------------------------

num = 1000000000
print("the num is{:,}".format(num))


And B for binary, o for octal, x or X for hexa, E for scientific 

num = 1000000000
print("the num is{:b}".format(num)) 

----------------------------------Patterns-----------------------------------------------
n=5 
for i in range(n):  
    for j in range(i+1):
        print('*',end='') 

    print() 


O/P:
*
**
***
****
***** 
or
rows = 5
for i in range(1, rows + 1): 
    for j in range(1, i + 1): 
        print("*", end=" ")  
    print()
----------------------------------

n=5 
for i in range(n):  
    for j in range(n-i):
        print('*',end='') 

    print()
    
O/P
*****
****
***
**
*

or

rows = 5
for i in range(rows,0, -1): 
    for j in range(1, i + 1): 
        print("*", end=" ")  
    print()
----------------------------------


n=5 
for i in range(n):  
    for j in range(n-i):
        print(' ',end='') 
    for j in range(i):
        print('*',end='')
    for j in range(i+1):
        print('*',end='') 
    
    print() 

O/p:
     *
    ***
   *****
  *******
 *********

or 
rows = 5
for i in range(1, rows + 1):  
    for j in range(rows  - i):  
        print(" ", end=" ")
    for k in range(1, 2 * i):
        print("*", end=" ")
    print()
----------------------------------

n=5 
for i in range(n):  
    for j in range(i):
        print(' ',end='') 
    for j in range(n-i-1):
        print('*',end='')
    for j in range(n-i):
        print('*',end='') 
    
    print()

O/P
*********
 *******
  *****
   ***
    *

or 
rows = 5
for i in range(rows , 0, -1): 
    for j in range(rows  - i):
        print(" ", end=" ")
    for k in range(1, 2 * i):  
        print("*", end=" ")
    print()    
--------------------------------------------
n=5
count=1
for i in range(n):
         print('*'*count) 
         count+=2
o/p:
*
***
*****
*******
*********

------------------encoding and decoding --------------------------


label_text = "Chai Spécial"

ecoded_label = label_text.encode("utf-8")

print(f"Non Encoded label: {label_text}")

print(f"Encoded label: {ecoded_label}")

decoded_label = ecoded_label.decode("utf-8")

print(f"Decoded label: {decoded_label}")

====================================================================================================================================================

# 01_basics.py

from functools import wraps

# A decorator is a function that takes another function as input,
# wraps it with extra behavior, and returns the new wrapped function

def my_decorator(func):
    # func is the original function being decorated (greet in this case)

    @wraps(func)
    # @wraps copies the original function's metadata (__name__, __doc__ etc.)
    # Without @wraps, greet.__name__ would return "wrapper" instead of "greet"
    def wrapper():
        print("Before function runs")
        func()   # calls the original function in the middle
        print("After function runs")
    return wrapper  # returns the wrapper, NOT the result of calling it

@my_decorator
# This is shorthand for:  greet = my_decorator(greet)
# From this point, greet points to wrapper, not the original greet
def greet():
    print("Hello from decorators class from chaicode")


greet()
print(greet.__name__)  # "greet" → preserved because of @wraps

# -------

# 02_logging_decorator.py

from functools import wraps

def log_activity(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # *args   → catches any positional arguments  (e.g. "Masala")
        # **kwargs → catches any keyword arguments    (e.g. milk="yes")
        # Using both makes the decorator work with ANY function signature
        print(f"🚀 Calling: {func.__name__}")
        result = func(*args, **kwargs)  # passes all arguments through to the original function
        print(f"✅ Finished: {func.__name__}")
        return result  # important: always return the result so the caller can use it
    return wrapper

@log_activity
def brew_chai(type, milk="no"):
    print(f"Brewing {type} chai and milk status {milk}")

brew_chai("Masala")
# Output:
# 🚀 Calling: brew_chai
# Brewing Masala chai and milk status no
# ✅ Finished: brew_chai

# -------

# 03_auth_decorator.py

from functools import wraps

def require_admin(func):
    """A practical decorator that acts as a GATE —
    it checks a condition before deciding whether to run the original function."""
    @wraps(func)
    def wrapper(user_role):
        if user_role != "admin":
            print("Access denied: Admins only")
            return None  # stops here, original function never runs
        else:
            return func(user_role)  # condition passed → run the original function
    return wrapper

@require_admin
def acess_tea_inventory(role):
    print("Access granted to tea inventory")

acess_tea_inventory("user")   # blocked → "Access denied: Admins only"
acess_tea_inventory("admin")  # allowed → "Access granted to tea inventory"

# -------

# 04_clean_input.py

from functools import wraps

def clean_input(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Clean positional arguments
        # isinstance(arg, str) → checks if the argument is a string before calling .strip()
        # this prevents errors if a non-string (int, bool, etc.) is passed
        new_args = tuple(arg.strip() if isinstance(arg, str) else arg for arg in args)

        # Clean keyword arguments (same logic but for key=value pairs)
        # kwargs.items() gives us each (key, value) pair to loop over
        new_kwargs = {  k: v.strip() if isinstance(v, str) else v for k, v in kwargs.items() }

        print("Cleaned data:", new_args, new_kwargs)

        # pass the cleaned versions to the original function
        return func(*new_args, **new_kwargs)
    return wrapper

@clean_input
def place_order(customer_name, item, address):
    print(f"Order placed by {customer_name}")
    print(f"Item: {item}")
    print(f"Shipping to: {address}")

# "  John Doe  " and "  Coffee Mug  " are positional → go into *args → cleaned via new_args
# address="  Chennai  " is a keyword argument → goes into **kwargs → cleaned via new_kwargs
place_order("  John Doe  ", "  Coffee Mug  ", address="  Chennai  ")

# -------
