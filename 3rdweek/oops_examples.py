"""
Practical OOP Concepts in Python
=================================

This file demonstrates:
1. Encapsulation
2. Inheritance:
   - Single inheritance
   - Multiple inheritance
   - Multilevel inheritance
   - Hierarchical inheritance
3. Polymorphism and method overriding
4. Method overloading using default arguments
5. Composition
6. Aggregation

Run:
    python oop_examples.py
"""


# ---------------------------------------------------------------------------
# 1. ENCAPSULATION
# ---------------------------------------------------------------------------
# Encapsulation combines data and the methods that operate on it.
# A double underscore makes an attribute harder to access directly.
# Public methods provide controlled access to the private data.


class BankAccount:
    def __init__(self, account_holder: str, balance: float = 0.0) -> None:
        self.account_holder = account_holder
        self.__balance = balance  # Private attribute

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
            return

        self.__balance += amount
        print(f"Deposited Rs.{amount:.2f}.")

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        elif amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            print(f"Withdrawn Rs.{amount:.2f}.")

    def get_balance(self) -> float:
        return self.__balance


def demonstrate_encapsulation() -> None:
    print("\n1. ENCAPSULATION")
    account = BankAccount("Anudeep", 5000)
    account.deposit(1500)
    account.withdraw(1000)
    print(f"Account holder: {account.account_holder}")
    print(f"Available balance: Rs.{account.get_balance():.2f}")


# ---------------------------------------------------------------------------
# 2. INHERITANCE
# ---------------------------------------------------------------------------

# 2A. SINGLE INHERITANCE
# One child class inherits from one parent class.


class Person:
    def __init__(self, name: str) -> None:
        self.name = name

    def introduce(self) -> None:
        print(f"My name is {self.name}.")


class Student(Person):
    def study(self) -> None:
        print(f"{self.name} is studying Python.")


def demonstrate_single_inheritance() -> None:
    print("\n2A. SINGLE INHERITANCE")
    student = Student("Anudeep")
    student.introduce()  # Inherited from Person
    student.study()      # Defined in Student


# 2B. MULTIPLE INHERITANCE
# One child class inherits from more than one parent class.


class Camera:
    def take_photo(self) -> None:
        print("Photo captured.")


class MusicPlayer:
    def play_music(self) -> None:
        print("Playing music.")


class SmartPhone(Camera, MusicPlayer):
    def make_call(self) -> None:
        print("Making a phone call.")


def demonstrate_multiple_inheritance() -> None:
    print("\n2B. MULTIPLE INHERITANCE")
    phone = SmartPhone()
    phone.make_call()
    phone.take_photo()  # Inherited from Camera
    phone.play_music()


# 2C. MULTILEVEL INHERITANCE
# A class inherits from a child class, forming a chain:
# Person -> Employee -> Developer.


class Employee(Person):
    def work(self) -> None:
        print(f"{self.name} is working.")


class Developer(Employee):
    def write_code(self) -> None:
        print(f"{self.name} is writing Python code.")


def demonstrate_multilevel_inheritance() -> None:
    print("\n2C. MULTILEVEL INHERITANCE")
    developer = Developer("Anudeep")
    developer.introduce()  # From Person
    developer.work()       # From Employee
    developer.write_code() # From Developer


# 2D. HIERARCHICAL INHERITANCE
# Multiple child classes inherit from the same parent class.


class Vehicle:
    def start(self) -> None:
        print("Vehicle started.")


class Car(Vehicle):
    def drive(self) -> None:
        print("Car is being driven.")


class Bike(Vehicle):
    def ride(self) -> None:
        print("Bike is being ridden.")


def demonstrate_hierarchical_inheritance() -> None:
    print("\n2D. HIERARCHICAL INHERITANCE")
    car = Car()
    bike = Bike()

    car.start()   # Inherited from Vehicle
    car.drive()

    bike.start()  # Inherited from Vehicle
    bike.ride()


# ---------------------------------------------------------------------------
# 3. POLYMORPHISM AND METHOD OVERRIDING
# ---------------------------------------------------------------------------
# Polymorphism means a common method call can produce different behavior.
# Each child class overrides the parent's make_sound() method.


class Animal:
    def make_sound(self) -> None:
        print("The animal makes a sound.")


class Dog(Animal):
    def make_sound(self) -> None:
        print("Dog says: Woof!")


class Cat(Animal):
    def make_sound(self) -> None:
        print("Cat says: Meow!")


def demonstrate_polymorphism() -> None:
    print("\n3. POLYMORPHISM AND METHOD OVERRIDING")
    animals = [Dog(), Cat(), Animal()]

    # The same method call behaves differently for each object.
    for animal in animals:
        animal.make_sound()


# ---------------------------------------------------------------------------
# 4. METHOD OVERLOADING USING DEFAULT ARGUMENTS
# ---------------------------------------------------------------------------
# Python does not support traditional method overloading by defining
# multiple methods with the same name. Default arguments provide a simple
# way to support different numbers of arguments.


class Calculator:
    def add(self, first: float, second: float = 0,
            third: float = 0) -> float:
        return first + second + third


def demonstrate_method_overloading() -> None:
    print("\n4. METHOD OVERLOADING USING DEFAULT ARGUMENTS")
    calculator = Calculator()

    print("Adding two numbers:", calculator.add(10, 20))
    print("Adding three numbers:", calculator.add(10, 20, 30))
    print("Adding one number:", calculator.add(10))


# ---------------------------------------------------------------------------
# 5. COMPOSITION
# ---------------------------------------------------------------------------
# Composition represents a strong HAS-A relationship.
# A Car creates and owns its Engine. The engine is created inside Car.


class Engine:
    def start(self) -> None:
        print("Engine started.")


class ComposedCar:
    def __init__(self) -> None:
        self.engine = Engine()  # Car creates its own Engine.

    def start_car(self) -> None:
        self.engine.start()
        print("Car is ready to drive.")


def demonstrate_composition() -> None:
    print("\n5. COMPOSITION")
    car = ComposedCar()
    car.start_car()


# 6. AGGREGATION
# ---------------------------------------------------------------------------
# Aggregation represents a weaker HAS-A relationship.
# A Department uses an Employee object created outside the Department.
# The Employee can exist independently of the Department.


class TeamMember:
    def __init__(self, name: str) -> None:
        self.name = name


class Department:
    def __init__(self, name: str, employee: TeamMember) -> None:
        self.name = name
        self.employee = employee  # Receives an existing object.

    def show_member(self) -> None:
        print(
            f"{self.employee.name} works in the {self.name} department."
        )


def demonstrate_aggregation() -> None:
    print("\n6. AGGREGATION")
    employee = TeamMember("Anudeep")  # Created independently.
    department = Department("Engineering", employee)
    department.show_member()

    # The employee object can still be used independently.
    print(f"Employee object still exists: {employee.name}")



# ---------------------------------------------------------------------------
# MAIN PROGRAM
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    demonstrate_encapsulation()
    demonstrate_single_inheritance()
    demonstrate_multiple_inheritance()
    demonstrate_multilevel_inheritance()
    demonstrate_hierarchical_inheritance()
    demonstrate_polymorphism()
    demonstrate_method_overloading()
    demonstrate_composition()
    demonstrate_aggregation()

