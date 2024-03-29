"""
Define an Employee class with attributes role, department and salary along with show_details() method
Create an Engineer class that inherits from Employee and has attributes name and age
"""
class Employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary

    def show_details(self):
        details = dict(
            role = self.role,
            department = self.department,
            salary = self.salary
        )
        print(details)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "Information Technology", 65000)

engineer1 = Engineer("Harsh Saxena", 25)
engineer1.show_details()