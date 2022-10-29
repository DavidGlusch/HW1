class Person:
    def __init__(self, age, gender, race):
        self.age = age
        self.gender = gender
        self.race = race


class Student(Person):
    def __init__(self, age, gender, race, grade):
        super().__init__(age, gender, race)
        self.grade = grade


class Teacher(Person):
    def __init__(self, age, gender, race, salary):
        super().__init__(age, gender, race)
        self.salary = salary
