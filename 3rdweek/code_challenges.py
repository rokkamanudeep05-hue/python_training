""" Story6  - OOP Coding Challenges
File: coding_challenges.py
This file contains 10 independent, beginner-friendly OOP examples.
Run the file to see a demonstration of every challenge.
"""

# ------------------------------------------------------------
# 1. STUDENT CLASS
# Concepts: class, object, constructor, instance variables,
#           instance methods, calculations
# ------------------------------------------------------------#

class Student:
   def __init__(self, name, roll_number, marks):
       self.name = name
       self.roll_number = roll_number
       self.marks = marks  # Example: [85, 90, 78]
   def total_marks(self):
       return sum(self.marks)
   def average_marks(self):
       if not self.marks:
           return 0
       return self.total_marks() / len(self.marks)
   def grade(self):
       average = self.average_marks()
       if average >= 90:
           return "A"
       elif average >= 75:
           return "B"
       elif average >= 60:
           return "C"
       elif average >= 40:
           return "D"
       return "Fail"
   def display(self):
       print(f"Name: {self.name}")
       print(f"Roll number: {self.roll_number}")
       print(f"Marks: {self.marks}")
       print(f"Total: {self.total_marks()}")
       print(f"Average: {self.average_marks():.2f}")
       print(f"Grade: {self.grade()}")

# ------------------------------------------------------------
# 2. BANK ACCOUNT CLASS
# Concepts: encapsulation, validation, instance methods
# ------------------------------------------------------------
class BankAccount:
   def __init__(self, account_holder, opening_balance=0):
       if opening_balance < 0:
           raise ValueError("Opening balance cannot be negative.")
       self.account_holder = account_holder
       self.__balance = opening_balance  # Private attribute
   def deposit(self, amount):
       if amount <= 0:
           print("Deposit amount must be greater than zero.")
           return
       self.__balance += amount
       print(f"Deposited Rs. {amount:.2f} successfully.")
   def withdraw(self, amount):
       if amount <= 0:
           print("Withdrawal amount must be greater than zero.")
       elif amount > self.__balance:
           print("Insufficient balance.")
       else:
           self.__balance -= amount
           print(f"Withdrawn Rs. {amount:.2f} successfully.")
   def check_balance(self):
       return self.__balance
   def display(self):
       print(f"Account holder: {self.account_holder}")
       print(f"Current balance: Rs. {self.__balance:.2f}")

# ------------------------------------------------------------
# 3. EMPLOYEE MANAGEMENT
# Concepts: classes, objects, lists, methods
# ------------------------------------------------------------
class Employee:
   def __init__(self, employee_id, name, department, monthly_salary):
       self.employee_id = employee_id
       self.name = name
       self.department = department
       self.monthly_salary = monthly_salary
   def annual_salary(self):
       return self.monthly_salary * 12
   def display(self):
       print(
           f"ID: {self.employee_id} | Name: {self.name} | "
           f"Department: {self.department} | "
           f"Monthly salary: Rs. {self.monthly_salary:.2f} | "
           f"Annual salary: Rs. {self.annual_salary():.2f}"
       )

class EmployeeManager:
   def __init__(self):
       self.employees = []
   def add_employee(self, employee):
       self.employees.append(employee)
       print(f"{employee.name} added successfully.")
   def find_employee(self, employee_id):
       for employee in self.employees:
           if employee.employee_id == employee_id:
               return employee
       return None
   def display_all(self):
       if not self.employees:
           print("No employees found.")
           return
       for employee in self.employees:
           employee.display()

# ------------------------------------------------------------
# 4. VEHICLE INHERITANCE
# Concepts: inheritance, method overriding, super()
# ------------------------------------------------------------
class Vehicle:
   def __init__(self, brand, model):
       self.brand = brand
       self.model = model
   def start(self):
       print(f"{self.brand} {self.model} is starting.")
   def display_info(self):
       print(f"Brand: {self.brand}, Model: {self.model}")

class Car(Vehicle):
   def __init__(self, brand, model, number_of_doors):
       super().__init__(brand, model)
       self.number_of_doors = number_of_doors
   def start(self):
       print(f"Car {self.brand} {self.model} starts with a key/button.")
   def display_info(self):
       super().display_info()
       print(f"Number of doors: {self.number_of_doors}")

class Bike(Vehicle):
   def __init__(self, brand, model, has_gear):
       super().__init__(brand, model)
       self.has_gear = has_gear
   def start(self):
       print(f"Bike {self.brand} {self.model} is started.")
   def display_info(self):
       super().display_info()
       print(f"Has gears: {'Yes' if self.has_gear else 'No'}")

# ------------------------------------------------------------
# 5. SHAPE AREA CALCULATOR
# Concepts: inheritance, polymorphism, method overriding
# ------------------------------------------------------------
class Shape:
   def area(self):
       raise NotImplementedError("Child classes must implement area().")

class Circle(Shape):
   def __init__(self, radius):
       if radius <= 0:
           raise ValueError("Radius must be positive.")
       self.radius = radius
   def area(self):
       return 3.14159 * self.radius ** 2

class Rectangle(Shape):
   def __init__(self, length, width):
       if length <= 0 or width <= 0:
           raise ValueError("Length and width must be positive.")
       self.length = length
       self.width = width
   def area(self):
       return self.length * self.width

class Triangle(Shape):
   def __init__(self, base, height):
       if base <= 0 or height <= 0:
           raise ValueError("Base and height must be positive.")
       self.base = base
       self.height = height
   def area(self):
       return 0.5 * self.base * self.height

# ------------------------------------------------------------
# 6. SHOPPING CART
# Concepts: composition, lists, objects, calculations
# ------------------------------------------------------------
class Product:
   def __init__(self, product_id, name, price):
       if price < 0:
           raise ValueError("Product price cannot be negative.")
       self.product_id = product_id
       self.name = name
       self.price = price

class ShoppingCart:
   def __init__(self):
       self.items = []  # Stores (Product object, quantity)
   def add_product(self, product, quantity=1):
       if quantity <= 0:
           print("Quantity must be greater than zero.")
           return
       for item in self.items:
           if item[0].product_id == product.product_id:
               item[1] += quantity
               print(f"Updated quantity of {product.name}.")
               return
       self.items.append([product, quantity])
       print(f"{product.name} added to cart.")
   def remove_product(self, product_id):
       for item in self.items:
           if item[0].product_id == product_id:
               self.items.remove(item)
               print(f"{item[0].name} removed from cart.")
               return
       print("Product not found in cart.")
   def total_bill(self):
       return sum(product.price * quantity
                  for product, quantity in self.items)
   def display_cart(self):
       if not self.items:
           print("Shopping cart is empty.")
           return
       print("Shopping cart:")
       for product, quantity in self.items:
           print(
               f"{product.name} x {quantity} = "
               f"Rs. {product.price * quantity:.2f}"
           )
       print(f"Total bill: Rs. {self.total_bill():.2f}")

# ------------------------------------------------------------
# 7. MOVIE RATING SYSTEM
# Concepts: classes, lists, validation, average calculation
# ------------------------------------------------------------
class Movie:
   def __init__(self, title):
       self.title = title
       self.ratings = []
   def add_rating(self, rating):
       if not 1 <= rating <= 10:
           print("Rating must be between 1 and 10.")
           return
       self.ratings.append(rating)
       print("Rating added.")
   def average_rating(self):
       if not self.ratings:
           return 0
       return sum(self.ratings) / len(self.ratings)
   def display(self):
       print(f"Movie: {self.title}")
       print(f"Ratings: {self.ratings}")
       print(f"Average rating: {self.average_rating():.2f}/10")

# ------------------------------------------------------------
# 8. HOSPITAL PATIENT RECORDS
# Concepts: encapsulation, dictionaries, CRUD operations
# ------------------------------------------------------------
class Patient:
   def __init__(self, patient_id, name, age, condition):
       self.patient_id = patient_id
       self.name = name
       self.age = age
       self.condition = condition
   def display(self):
       print(
           f"Patient ID: {self.patient_id} | Name: {self.name} | "
           f"Age: {self.age} | Condition: {self.condition}"
       )

class Hospital:
   def __init__(self):
       self.patients = {}
   def register_patient(self, patient):
       if patient.patient_id in self.patients:
           print("Patient ID already exists.")
           return
       self.patients[patient.patient_id] = patient
       print(f"Patient {patient.name} registered.")
   def update_condition(self, patient_id, new_condition):
       patient = self.patients.get(patient_id)
       if patient is None:
           print("Patient not found.")
           return
       patient.condition = new_condition
       print("Patient condition updated.")
   def display_patients(self):
       if not self.patients:
           print("No patient records available.")
           return
       for patient in self.patients.values():
           patient.display()

# ------------------------------------------------------------
# 9. SCHOOL RESULT PROCESSING
# Concepts: classes, dictionaries, loops, conditions
# ------------------------------------------------------------
class SchoolResult:
   def __init__(self, student_name, subject_marks):
       self.student_name = student_name
       self.subject_marks = subject_marks  # {"Python": 85, "SQL": 90}
   def total_marks(self):
       return sum(self.subject_marks.values())
   def percentage(self):
       if not self.subject_marks:
           return 0
       maximum_marks = len(self.subject_marks) * 100
       return (self.total_marks() / maximum_marks) * 100
   def result(self):
       if not self.subject_marks:
           return "No marks available"
       if any(mark < 0 or mark > 100
              for mark in self.subject_marks.values()):
           return "Invalid marks"
       if any(mark < 35 for mark in self.subject_marks.values()):
           return "Fail"
       return "Pass"
   def display(self):
       print(f"Student: {self.student_name}")
       for subject, mark in self.subject_marks.items():
           print(f"{subject}: {mark}")
       print(f"Total: {self.total_marks()}")
       print(f"Percentage: {self.percentage():.2f}%")
       print(f"Result: {self.result()}")

# ------------------------------------------------------------
# 10. ONLINE COURSE MANAGEMENT
# Concepts: classes, object relationships, lists, methods
# ------------------------------------------------------------
class Course:
   def __init__(self, course_id, title, instructor):
       self.course_id = course_id
       self.title = title
       self.instructor = instructor
       self.enrolled_students = []
   def enroll_student(self, student_name):
       if student_name in self.enrolled_students:
           print(f"{student_name} is already enrolled.")
           return
       self.enrolled_students.append(student_name)
       print(f"{student_name} enrolled in {self.title}.")
   def display(self):
       print(f"Course: {self.title}")
       print(f"Course ID: {self.course_id}")
       print(f"Instructor: {self.instructor}")
       print(f"Enrolled students: {self.enrolled_students}")

# ------------------------------------------------------------
# MAIN: DEMONSTRATE ALL 10 CHALLENGES
# ------------------------------------------------------------
def main():
   print("\n========== 1. STUDENT CLASS ==========")
   student = Student("Anil", 101, [85, 90, 78])
   student.display()
   print("\n========== 2. BANK ACCOUNT ==========")
   account = BankAccount("Anil", 5000)
   account.deposit(1500)
   account.withdraw(1000)
   account.display()
   print("\n========== 3. EMPLOYEE MANAGEMENT ==========")
   manager = EmployeeManager()
   manager.add_employee(Employee(1, "Ravi", "IT", 30000))
   manager.add_employee(Employee(2, "Priya", "HR", 35000))
   manager.display_all()
   print("\n========== 4. VEHICLE INHERITANCE ==========")
   car = Car("Toyota", "Innova", 4)
   bike = Bike("Honda", "Shine", True)
   car.display_info()
   car.start()
   bike.display_info()
   bike.start()
   print("\n========== 5. SHAPE AREA CALCULATOR ==========")
   shapes = [Circle(5), Rectangle(10, 4), Triangle(6, 3)]
   for shape in shapes:
       print(f"{type(shape).__name__} area: {shape.area():.2f}")
   print("\n========== 6. SHOPPING CART ==========")
   cart = ShoppingCart()
   laptop = Product(1, "Laptop", 50000)
   mouse = Product(2, "Mouse", 500)
   cart.add_product(laptop, 1)
   cart.add_product(mouse, 2)
   cart.display_cart()
   print("\n========== 7. MOVIE RATING SYSTEM ==========")
   movie = Movie("Inception")
   movie.add_rating(9)
   movie.add_rating(8)
   movie.add_rating(10)
   movie.display()
   print("\n========== 8. HOSPITAL PATIENT RECORDS ==========")
   hospital = Hospital()
   hospital.register_patient(Patient(101, "Kiran", 30, "Fever"))
   hospital.register_patient(Patient(102, "Meena", 25, "Cold"))
   hospital.update_condition(101, "Recovering")
   hospital.display_patients()
   print("\n========== 9. SCHOOL RESULT PROCESSING ==========")
   result = SchoolResult("Arjun", {"Python": 85, "SQL": 90, "Maths": 78})
   result.display()
   print("\n========== 10. ONLINE COURSE MANAGEMENT ==========")
   course = Course("PY101", "Python Programming", "Mr. Kumar")
   course.enroll_student("Anil")
   course.enroll_student("Priya")
   course.display()

if __name__ == "__main__":
   main()
