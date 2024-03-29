class Student:
    def __init__(self, physics, chemistry, maths):
        self.physics = physics
        self.chemistry = chemistry
        self.maths = maths

    # using @property decorator
    @property
    def percentage(self):
        return (self.physics + self.chemistry + self.maths)/3

student1 = Student(98, 99, 100)
print(student1.percentage)
student1.chemistry = 88
print(round(student1.percentage, 2))