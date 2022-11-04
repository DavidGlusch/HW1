import unittest
from Lesson_15.Task_2 import Dog


class TestDog(unittest.TestCase):

    def setUp(self) -> None:
        self.dog_test = Dog(5)

    def test_age_factor_value(self):
        self.assertEqual(self.dog_test.age_factor, 7)

    def test_human_age(self):
        self.assertEqual(self.dog_test.human_age(), 35)

if __name__ == '__main__':
    unittest.main()
