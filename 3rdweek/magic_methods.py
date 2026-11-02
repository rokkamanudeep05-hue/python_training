"""""
What are magic methods?
Magic methods are special methods provided by Python that allow you to define how your own 
objects behave with built-in functions and operators.


They are also called dunder methods because their names begin and end with two underscores. 
double underscores are often abbreviated as "dunder" in Python. 
For example, the __init__ method is a magic method that is called when an object is created, 
and the __str__ method is called when you use the str() function on an object.


You write	                                                      Python uses
print(laptop)	                                                   __str__()
len(laptop)	                                                       __len__()
laptop == mouse	                                                   __eq__()
laptop < mouse	                                                   __lt__()
laptop > mouse	                                                   __gt__()
laptop + mouse	                                                   __add__()
laptop - mouse	                                                   __sub__()




The __repr__() method is similar to __str__(), but its main purpose is to provide 
a useful representation for debugging and development.



Used for creating user-friendly output and for displaying the object as a string __str__()

Used for debugging and development purposes to get the complete information of an object __repr__()



"""


# magic_methods.py
# Demonstrating Python Magic Methods


class Product:

    # Constructor: initialize product details
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # 1. __str__ : Display user-friendly information
    def __str__(self):
        return f"{self.name} costs Rs. {self.price}"

    # 2. __repr__ : Display developer-friendly information
    def __repr__(self):
        return f"Product(name={self.name!r}, price={self.price!r})"

    # 3. __len__ : Return the length of the product name
    def __len__(self):
        return len(self.name)

    # 4. __eq__ : Compare two products by price
    def __eq__(self, other):
        return self.price == other.price

    # 5. __lt__ : Check whether one product is cheaper
    def __lt__(self, other):
        return self.price < other.price

    # 6. __gt__ : Check whether one product is more expensive
    def __gt__(self, other):
        return self.price > other.price

    # 7. __add__ : Add the prices of two products
    def __add__(self, other):
        return Product(
            self.name + " + " + other.name,
            self.price + other.price
        )

    # 8. __sub__ : Subtract the prices of two products
    def __sub__(self, other):
        return Product(
            self.name + " - " + other.name,
            self.price - other.price
        )


# Create objects
laptop = Product("Laptop", 50000)
mouse = Product("Mouse", 1000)
keyboard = Product("Keyboard", 1000)

# Test __str__
print("1. __str__")
print(laptop)

# Test __repr__
print("\n2. __repr__")
print(repr(laptop))

# Test __len__
print("\n3. __len__")
print("Length of product name:", len(laptop))

# Test __eq__
print("\n4. __eq__")
print("Mouse and keyboard have equal prices:", mouse == keyboard)
print("Laptop and mouse have equal prices:", laptop == mouse)

# Test __lt__
print("\n5. __lt__")
print("Mouse is cheaper than laptop:", mouse < laptop)

# Test __gt__
print("\n6. __gt__")
print("Laptop is more expensive than mouse:", laptop > mouse)

# Test __add__
print("\n7. __add__")
combined = laptop + mouse
print(combined)

# Test __sub__
print("\n8. __sub__")
difference = laptop - mouse
print(difference)
