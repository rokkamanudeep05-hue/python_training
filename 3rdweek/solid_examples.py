"""
SOLID Principles in Python
==========================

This file demonstrates one practical example for each SOLID principle:
1. Single Responsibility Principle (SRP)
2. Open/Closed Principle (OCP)
3. Liskov Substitution Principle (LSP)
4. Interface Segregation Principle (ISP)
5. Dependency Inversion Principle (DIP)

Run:
    python solid_examples.py

Each example prints a short demonstration to the terminal.
"""


# ---------------------------------------------------------------------------
# 1. Single Responsibility Principle (SRP)
# ---------------------------------------------------------------------------
# A class should have one main responsibility and one reason to change.
# Employee stores employee information; EmployeeRepository handles saving it.


class Employee:
    def __init__(self, name: str, salary: float) -> None:
        self.name = name
        self.salary = salary

    def display_details(self) -> None:
        print(f"Employee: {self.name}")
        print(f"Salary: Rs.{self.salary:.2f}")


class EmployeeRepository:
    def save(self, employee: Employee) -> None:
        # Demonstration only: a real repository could save to a database.
        print(f"Saving {employee.name}'s details...")


def code_srp() -> None:
    print("\n1. SINGLE RESPONSIBILITY PRINCIPLE")
    employee = Employee("Anudeep", 30000)
    employee.display_details()

    repository = EmployeeRepository()
    repository.save(employee)


# ---------------------------------------------------------------------------
# 2. Open/Closed Principle (OCP)
# ---------------------------------------------------------------------------
# Software should be open for extension but closed for modification.
# New payment types can be added without changing PaymentProcessor.


class PaymentMethod:
    def pay(self, amount: float) -> None:
        raise NotImplementedError("Subclasses must implement pay().")


class CreditCardPayment(PaymentMethod):
    def pay(self, amount: float) -> None:
        print(f"Paid Rs.{amount:.2f} using Credit Card.")


class UpiPayment(PaymentMethod):
    def pay(self, amount: float) -> None:
        print(f"Paid Rs.{amount:.2f} using UPI.")


class PaymentProcessor:
    def process_payment(self, payment_method: PaymentMethod,
                        amount: float) -> None:
        payment_method.pay(amount)


def code_ocp() -> None:
    print("\n2. OPEN/CLOSED PRINCIPLE")
    processor = PaymentProcessor()
    processor.process_payment(CreditCardPayment(), 500)
    processor.process_payment(UpiPayment(), 1000)


# ---------------------------------------------------------------------------
# 3. Liskov Substitution Principle (LSP)
# ---------------------------------------------------------------------------
# An object of a child class should be usable wherever its parent is expected
# without breaking the program's expected behavior.
# Both SavingsAccount and CurrentAccount honor the withdraw() contract.


class BankAccount:
    def __init__(self, balance: float) -> None:
        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.balance = balance

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")

        self.balance -= amount


class SavingsAccount(BankAccount):
    pass


class CurrentAccount(BankAccount):
    pass


def make_withdrawal(account: BankAccount, amount: float) -> None:
    account.withdraw(amount)
    print(f"Withdrawal successful. Remaining balance: Rs.{account.balance:.2f}")


def code_lsp() -> None:
    print("\n3. LISKOV SUBSTITUTION PRINCIPLE")
    accounts = [SavingsAccount(5000), CurrentAccount(8000)]

    for account in accounts:
        make_withdrawal(account, 1000)


# ---------------------------------------------------------------------------
# 4. Interface Segregation Principle (ISP)
# ---------------------------------------------------------------------------
# Clients should not be forced to depend on methods they do not use.
# Instead of one large machine interface, define small capability interfaces.


class Printable:
    def print_document(self, document: str) -> None:
        raise NotImplementedError


class Scannable:
    def scan_document(self) -> str:
        raise NotImplementedError


class BasicPrinter(Printable):
    def print_document(self, document: str) -> None:
        print(f"Printing: {document}")


class MultiFunctionPrinter(Printable, Scannable):
    def print_document(self, document: str) -> None:
        print(f"Printing: {document}")

    def scan_document(self) -> str:
        scanned_text = "Scanned document content"
        print(scanned_text)
        return scanned_text


def code_isp() -> None:
    print("\n4. INTERFACE SEGREGATION PRINCIPLE")
    basic_printer = BasicPrinter()
    basic_printer.print_document("Training Report")

    multi_printer = MultiFunctionPrinter()
    multi_printer.print_document("Project Notes")
    multi_printer.scan_document()


# ---------------------------------------------------------------------------
# 5. Dependency Inversion Principle (DIP)
# ---------------------------------------------------------------------------
# High-level business logic should depend on an abstraction, not on a
# particular low-level implementation.
# NotificationService depends on MessageSender, not directly on EmailSender.


class MessageSender:
    def send(self, message: str) -> None:
        raise NotImplementedError


class EmailSender(MessageSender):
    def send(self, message: str) -> None:
        print(f"Sending email: {message}")


class SmsSender(MessageSender):
    def send(self, message: str) -> None:
        print(f"Sending SMS: {message}")


class NotificationService:
    def __init__(self, sender: MessageSender) -> None:
        self.sender = sender

    def notify(self, message: str) -> None:
        self.sender.send(message)


def code_dip() -> None:
    print("\n5. DEPENDENCY INVERSION PRINCIPLE")
    email_service = NotificationService(EmailSender())
    email_service.notify("Your task is completed.")

    # The sender can be changed without modifying NotificationService.
    sms_service = NotificationService(SmsSender())
    sms_service.notify("Your meeting starts in 10 minutes.")


# ---------------------------------------------------------------------------
# Run all demonstrations
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    code_srp()
    code_ocp()
    code_lsp()
    code_isp()
    code_dip()

