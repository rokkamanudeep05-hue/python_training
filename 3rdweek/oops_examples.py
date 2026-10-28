""""
Why do we use encapsulation?
Encapsulation is useful for:
1. Data protection: Prevents accidental or invalid changes to data.
2. Validation: Checks data before updating it.
3. Controlled access: Allows users to interact with data through methods.
4. Maintainability: Makes code easier to manage and update.
5. Security: Reduces unintended access to internal implementation details, 
although Python encapsulation alone is not a security boundary.

define :

It combines data and methods within a class and controls how the data is accessed or modified.

What is Polymorphism?
Polymorphism means “one name, many forms.”

In Python, polymorphism allows the same method name or operation to behave differently 
depending on the object using it.

Method Overloading Using Default Arguments in Python
method overloading using default arguments means defining a method with parameters that  default values, 
allowing it to work with different numbers of arguments.

Aggregation

It is a relationship in which one class contains a reference to an object of another class,
 while the contained object can also exist independently.

 example: A department has employees. Employees can still exist 
 if the department is removed or reorganized.

"""

"""
oop_examples.py

Practical demonstrations of the main Object-Oriented Programming (OOP)
concepts in Python.

Topics:
1. Encapsulation
2. Inheritance: single, multiple, multilevel, and hierarchical
3. Polymorphism and method overriding
4. Method overloading using default arguments
5. Composition and aggregation

Run:
    python oop_examples.py
"""


# ---------------------------------------------------------------------
# 1. ENCAPSULATION
# ---------------------------------------------------------------------
# Encapsulation combines data and the methods that operate on that data
# inside a class. The double underscore makes __balance name-mangled,
# discouraging direct access and helping prevent accidental changes.


class BankAccount:
    def __init__(self, owner: str, opening_balance: float = 0):
        self.owner = owner
        self.__balance = opening_balance

    def deposit(self, amount: float) -> None:
        """Add money only when the amount is positive."""
        if amount <= 0:
            print("Deposit rejected: amount must be positive.")
            return

        self.__balance += amount
        print(f"Deposited Rs. {amount:.2f}")

    def withdraw(self, amount: float) -> None:
        """Withdraw money only when funds are sufficient."""
        if amount <= 0:
            print("Withdrawal rejected: amount must be positive.")
        elif amount > self.__balance:
            print("Withdrawal rejected: insufficient balance.")
        else:
            self.__balance -= amount
            print(f"Withdrawn Rs. {amount:.2f}")

    def get_balance(self) -> float:
        """Provide controlled read access to the balance."""
        return self.__balance


# ---------------------------------------------------------------------
# 2. INHERITANCE
# ---------------------------------------------------------------------

# 2A. Single inheritance: one child class inherits from one parent class.


class Employee:
    def __init__(self, name: str):
        self.name = name

    def show_name(self) -> None:
        print(f"Employee name: {self.name}")


class Developer(Employee):
    def write_code(self) -> None:
        print(f"{self.name} is writing Python code.")


# 2B. Multiple inheritance: one child inherits from multiple parent classes.


class Camera:
    def take_photo(self) -> None:
        print("Photo captured.")


class Phone:
    def make_call(self) -> None:
        print("Making a phone call.")


class Smartphone(Camera, Phone):
    """A smartphone can use methods inherited from both parents."""
    pass


# 2C. Multilevel inheritance: inheritance forms a chain.
# LivingBeing -> Animal -> Dog

class LivingBeing:
    def breathe(self) -> None:
        print("Living being breathes.")


class Animal(LivingBeing):
    def eat(self) -> None:
        print("Animal eats food.")


class Dog(Animal):
    def bark(self) -> None:
        print("Dog barks.")


# 2D. Hierarchical inheritance: multiple child classes share one parent.


class Vehicle:
    def start(self) -> None:
        print("Vehicle starts.")


class Car(Vehicle):
    def drive(self) -> None:
        print("Car is driving.")


class Bike(Vehicle):
    def ride(self) -> None:
        print("Bike is being ridden.")


# ---------------------------------------------------------------------
# 3. POLYMORPHISM AND METHOD OVERRIDING
# ---------------------------------------------------------------------

# Polymorphism: different object types respond to the same method call
# in their own way. This function does not need to know the exact type.


class PDFReport:
    def generate(self) -> None:
        print("Generating a PDF report.")


class ExcelReport:
    def generate(self) -> None:
        print("Generating an Excel report.")


def create_report(report) -> None:
    """Call the common interface provided by each report object."""
    report.generate()


# Method overriding: child classes replace a method inherited from a parent.


class Notification:
    def send(self) -> None:
        print("Sending a general notification.")


class EmailNotification(Notification):
    def send(self) -> None:
        print("Sending an email notification.")


class SMSNotification(Notification):
    def send(self) -> None:
        print("Sending an SMS notification.")

# ---------------------------------------------------------------------
# 4. METHOD OVERLOADING USING DEFAULT ARGUMENTS
# ---------------------------------------------------------------------
# Python does not support traditional signature-based method overloading
# by defining multiple methods with the same name in one class. Default
# arguments can provide similar flexibility for different argument counts.


class Calculator:
    def add(self, a: float, b: float = 0, c: float = 0) -> float:
        """Add one, two, or three numbers using one method."""
        return a + b + c


# -----------------------------------
# # 5. COMPOSITION AND AGGREGATION
# ---------------------------------------------------------------------

# Composition: a strong ownership-style HAS-A relationship.
# In this example, ComposedCar creates its own Engine object.


class Engine:
    def start(self) -> None:
        print("Engine started.")


class ComposedCar:
    def __init__(self):
        # The car constructs and holds its engine as an internal component.
        self.engine = Engine()

    def start_car(self) -> None:  
        self.engine.start()
        print("Car is ready to drive.")   



   # Aggregation: a weaker HAS-A relationship. The related object is created
# independently and passed in, so it can exist without the Department.


class StaffMember:
    def __init__(self, name: str):
        self.name = name


class Department:
    def __init__(self, employee: StaffMember):
        # Department uses an existing StaffMember; it did not create it.
        self.employee = employee

    def show_employee(self) -> None:
        print(f"Department employee: {self.employee.name}")