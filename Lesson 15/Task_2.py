class Dog:
    age_factor = 7

    def __init__(self, dog_age):
        self.dog_age = dog_age

    def human_age(self):
        return self.age_factor * self.dog_age


dog_1 = Dog(3)
print(dog_1.human_age())
