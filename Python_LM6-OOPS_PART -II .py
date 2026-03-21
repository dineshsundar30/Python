# 01_simple_class.py

class Chai:
    pass  # empty class, just a blueprint with no attributes or methods

class ChaiTime:
    pass

# type() returns the class that the object belongs to
print(type(Chai))         # <class 'type'>  → Chai itself is an object of type 'type'

ginger_tea = Chai()       # creating an instance (object) from the Chai class
print(type(ginger_tea))   # <class '__main__.Chai'>
print(type(ginger_tea) is Chai)      # True
print(type(ginger_tea) is ChaiTime)  # False

# -------

# 02_namespace.py

class Chai:
    origin = "India"  # class attribute → shared by ALL instances

print(Chai.origin)

# you can add new attributes to a class even after defining it
Chai.is_hot = True
print(Chai.is_hot)

# creating objects from class Chai

masala = Chai()
print(f"Masala {masala.origin}")   # instance inherits class attribute
print(f"Masala {masala.is_hot}")

# setting is_hot on the instance creates an INSTANCE attribute
# it does NOT change the class attribute
masala.is_hot = False

print("Class: ", Chai.is_hot)      # still True  → class attribute unchanged
print(f"Masala {masala.is_hot}")   # False        → instance has its own copy now

masala.flavor = "Masala"  # new attribute added only to this instance
print(masala.flavor)

# -------

# 03_attribute_shadowing.py

class Chai:
    temperature = "hot"  # class attribute
    strength = "Strong"


cutting = Chai()
print(cutting.temperature)  # reads from class → "hot"

# setting temperature on the instance SHADOWS the class attribute
# the class attribute is NOT modified, a new instance attribute is created
cutting.temperature = "Mild"
cutting.cup = "small"
print("After changing ",cutting.temperature)   # "Mild"  → instance attribute
print("cup size is  ",cutting.cup)
print("Direct look into the class ", Chai.temperature)  # "hot" → class unchanged

# del removes the INSTANCE attribute, not the class attribute
# after deleting, the instance falls back to reading from the class
del cutting.temperature
del cutting.cup
print(cutting.temperature)  # "hot" → back to class attribute
print(cutting.cup)          # AttributeError! cup never existed on the class

# -------

# 04_self_args.py

class Chaicup:
    size = 150 #ml

    def describe(self):
        """self refers to the instance that called the method.
        Python passes it automatically when you use dot notation."""
        return f"A {self.size}ml chai cup"
    

cup = Chaicup()
print(cup.describe())              # Python auto-passes cup as self
print(Chaicup.describe(cup))       # same thing, but passing self manually

cup_two = Chaicup()
cup_two.size = 100                 # instance attribute shadows class attribute
print(Chaicup.describe(cup_two))   # uses cup_two.size = 100

# -------

# 05_init_objects.py

class ChaiOrder:
    
    def __init__(self, type_, size):
        """__init__ is the constructor — runs automatically when an object is created.
        self.type and self.size are instance attributes set per object.
        Note: type_ is used instead of type to avoid shadowing Python's built-in type()"""
        self.type = type_
        self.size = size

    def summary(self):
        return f"{self.size}ml of {self.type} chai"
    
order = ChaiOrder("Masala", 200)
print(order.summary())

order_two = ChaiOrder("Ginger", 220)
print(order_two.summary())

# -------

# 06_inheritance_composition.py

class BaseChai:
    def __init__(self, type_):
        self.type = type_

    def prepare(self):
        print(f"Preparing {self.type} chai....")

class MasalaChai(BaseChai):
    # MasalaChai INHERITS everything from BaseChai and adds its own method
    def add_spices(self):
        print("Adding cardamom, ginger, cloves.")


class ChaiShop:
    # chai_cls is a class attribute pointing to which chai class to use
    # this is COMPOSITION → ChaiShop "has a" Chai inside it
    chai_cls = BaseChai

    def __init__(self):
        self.chai = self.chai_cls("Regular")  # creates a Chai object inside the shop

    def serve(self):
        print(f"Serving {self.chai.type} chai in the shop")
        self.chai.prepare()

class FancyChaiShop(ChaiShop):
    # overrides chai_cls → now uses MasalaChai instead of BaseChai
    # __init__ and serve() are inherited from ChaiShop, no need to rewrite them
    chai_cls = MasalaChai


shop = ChaiShop()
fancy = FancyChaiShop()
shop.serve()          # uses BaseChai
fancy.serve()         # uses MasalaChai (because chai_cls was overridden)
fancy.chai.add_spices()

# -------

# 07_base_class.py

class Chai:
    def __init__(self, type_, strength):
        self.type = type_
        self.strength = strength


# class GingerChai(Chai):
#     def __init__(self, type_, strength, spice_level):
#         self.type = type_
#         self.strength = strength
#         self.spice_level = spice_level
        # ↑ BAD: manually repeating parent's __init__ logic (code duplication)

# class GingerChai(Chai):
#     def __init__(self, type_, strength, spice_level):
#         Chai.__init__(self, type_, strength)
#         self.spice_level = spice_level
        # ↑ WORKS but tightly coupled to the parent class name

class GingerChai(Chai):
    def __init__(self, type_, strength, spice_level):
        super().__init__(type_, strength)  # BEST: super() calls the parent's __init__
        self.spice_level = spice_level     # then add the child's own attribute

# -------

# 08_mro.py

# MRO = Method Resolution Order
# Defines the order Python searches for attributes/methods in a class hierarchy
# Python uses the C3 Linearization algorithm to compute this order

class A:
    label = "A: Base class"

class B(A):
    label = "B: Masala blend"

class C(A):
    label = "C: Herbal blend"

class D(C, B):
    # D inherits from both C and B (multiple inheritance)
    # MRO order: D → C → B → A
    # So D().label will come from C, not B or A
    pass

cup = D()
print(cup.label)    # "C: Herbal blend" → found in C first
print(D.__mro__)    # shows the full lookup chain as a tuple of classes

# -------

# 09_static_methods.py

class ChaiUtils:
    @staticmethod
    def clean_ingredients(text):
        """A static method does NOT receive self or cls.
        It behaves like a regular function but lives inside the class
        because it's logically related to it.
        Use it when you don't need access to instance or class data."""
        return [item.strip() for item in text.split(",")]
    

raw = " water , milk , ginger , honey "

cleaned = ChaiUtils.clean_ingredients(raw)
print(cleaned)  # ['water', 'milk', 'ginger', 'honey']

# -------

# 10_classmethod.py

class ChaiOrder:
    def __init__(self, tea_type, sweetness, size):
        self.tea_type = tea_type
        self.sweetness = sweetness
        self.size = size

    @classmethod
    def from_dict(cls, order_data):
        """cls refers to the class itself (like self refers to the instance).
        classmethods are often used as ALTERNATIVE CONSTRUCTORS —
        different ways to create an object without changing __init__."""
        return cls(
            order_data["tea_type"],
            order_data["sweetness"],
            order_data["size"],
        )
    
    @classmethod
    def from_string(cls, order_string):
        # parses a string like "Ginger-Low-Small" into separate values
        tea_type, sweetness, size = order_string.split("-")
        return cls(tea_type, sweetness, size)
    
class ChaiUtils:
    @staticmethod
    def is_valid_size(size):
        return size in ["Small", "Medium", "Large"]


print(ChaiUtils.is_valid_size("Medium"))  # True

order1 = ChaiOrder.from_dict({"tea_type": "masala", "sweetness": "medium", "size":"Large"})
order2 = ChaiOrder.from_string("Ginger-Low-Small")
order3 = ChaiOrder("Large", "Low", "Large")

# __dict__ shows all instance attributes as a dictionary
print(order1.__dict__)
print(order2.__dict__)
print(order3.__dict__)

# -------

# 11_propert_decorators.py

class TeaLeaf:
    def __init__(self, age):
        self._age = age  # _age convention means "intended to be private, don't touch directly"

    @property
    def age(self):
        """@property lets you access a method like an attribute (no parentheses).
        leaf.age  instead of  leaf.age()
        Here it also adds 2 to the stored age before returning it."""
        return self._age + 2
    
    @age.setter
    def age(self, age):
        """@age.setter runs when you do  leaf.age = value
        It lets you add validation logic before storing the value."""
        if 1 <= age <= 5:
            self._age = age
        else:
            raise ValueError("Tea leaf age must be between 1 and 5 years")
        
leaf = TeaLeaf(2)
print(leaf.age)   # 4  (2 + 2 from the property getter)
leaf.age = 6      # triggers the setter → raises ValueError because 6 > 5
print(leaf.age)

# -------
