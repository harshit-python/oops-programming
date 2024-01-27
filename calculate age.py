'''* python program to create a person class. include attributes like name, country and date of birth
and than calculate person's age
'''
from datetime import date


class Person:
    def __init__(self, name, country, date_of_birth) -> None:
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth

    def calculate_age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year
        if today < date(today.year, self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        return age


person = Person("Harsh", "India", date(1998, 5, 31))
print("Person name:", person.name)
print("Person's country:", person.country)
print("Person's date of birth:", person.date_of_birth)
print("Person's Age:", person.calculate_age())
