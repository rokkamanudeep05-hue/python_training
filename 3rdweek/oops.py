class Employee:
    def __init__(self, name: str):
        self.name = name

    def show_name(self) -> None:
        print(f"Employee name: {self.name}")


class Developer(Employee):
    def write_code(self) -> None:
        print(f"{self.name} is writing Python code.")