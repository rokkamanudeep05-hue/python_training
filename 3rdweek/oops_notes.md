
fundamentals of oops : 

What is Object-Oriented Programming (OOP)?
Object-Oriented Programming (OOP) is a programming approach in which we organize code using classes and objects.

why we use oops in python : it organies the code by combining data and functions into classes and objects 


## Class
A class is a collection of objects. Classes are blueprints for creating objects. A class defines a set of attributes and methods that the created objects (instances) .
Classes are defined using the class keyword, followed by the class name and a colon.

class Student:
    pass

    Explanation:
class is the Python keyword used to define a class.
Student is the class name.
pass means there is no implementation inside the class yet.

what is an object ?
An object is an instance of a class.

 
 class Student:
    pass


student1 = Student()
student2 = Student()

print(student1)
print(student2)

Student is the class.
student1 and student2 are variables referencing two separately created objects.
Student() creates an instance of the class.



## What is a constructor? 
a special function or method in class-based object-oriented programming (OOP) that is automatically called when a new object instance is created

## What are instance variables?
Instance variables are variables that belong to a specific object.
 Each object maintains its own copy of these variables.

 class Student:
    def __init__(self, name):
        self.name = name   # Instance variable

s1 = Student("Jake")
s2 = Student("Emily")

print(s1.name)
print(s2.name)


## Class Variables
A class variable is a variable that belongs to the class itself rather than to any specific object.

class Student:
    school = "ABC School"   # Class variable

s1 = Student()
s2 = Student()

print(s1.school)
print(s2.school)


## both class and instance variables

class CSStudent:
    stream = 'cse'          # Class variable

    def __init__(self, name, roll):
        self.name = name    # Instance variable
        self.roll = roll    # Instance variable

# Creating objects
a = CSStudent('Rose', 1)
b = CSStudent('Nat', 2)

print(a.stream)
print(b.stream)  
print(a.name)
print(b.name)

## instance variable	                                  Class variable
Belongs to an individual object	                      Belongs to the class
Usually defined using self	                          Defined directly inside the class
Each object can have different values	             Commonly shared by all objects

## instance, Class, and Static Methods

method is defined inside the class 

class Student:
    def greet(self):
        print("Hello, student!")


student1 = Student()
student1.greet()

Student is a class.
student1 is an object.
greet() is a method.
self refers to the object calling the method.


Python has three commonly used method types: instance methods, class methods, and static methods.

## Instance methods — working with individual objects

An instance method is used when an operation depends on the data of a particular object.

It normally receives self as its first parameter.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_details(self):
        print("Employee Name:", self.name)
        print("Employee Salary:", self.salary)

    def increase_salary(self, amount):
        self.salary = self.salary + amount


emp1 = Employee("Anil", 30000)
emp2 = Employee("Ravi", 40000)

emp1.display_details()

emp1.increase_salary(5000)

emp1.display_details()
emp2.display_details()

