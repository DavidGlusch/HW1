import json
from unittest import TestCase
# import sys
# from Lesson_11.Task_2 import add_item, read_from_file, delete_item, update_item
# sys.path.insert(1, 'E:\HomeWork\Lesson_11\Task_2.py')


def read_from_file(path_to_file):
    """
    :param path_to_file: srt
    :return: dict
    """
    try:
        with open(path_to_file, encoding='utf-8') as book:
            temp = json.load(book)
    except:
        print("There is no such file.")
        return None
    return temp


def add_item(my_book: dict):
    first_name = input('Enter your first name: ')
    last_name = input('Enter your last name: ')
    full_name = input('Enter your full name: ')
    phone_number = input('Enter your phone number: ')
    city = input('Enter your city: ')
    my_book[phone_number] = {'first_name': first_name,
                             'last_name': last_name,
                             'full_name': full_name,
                             'phone_number': phone_number,
                             'city': city}
    return my_book




def delete_item(my_book: dict):
    phone_num = input("Enter your phone number: ")

    try:
        my_book.pop(phone_num)
    except KeyError:
        print("No such number")
        return None


class MockInputFunction:
    def __init__(self, return_value=None):
        self.return_value = return_value
        self._orig_input_fn = __builtins__['input']

    def _mock_input_fn(self, prompt):
        # print(prompt + str(self.return_value))
        return self.return_value

    def __enter__(self):
        __builtins__['input'] = self._mock_input_fn

    def __exit__(self, type, value, traceback):
        __builtins__['input'] = self._orig_input_fn


class TestPhonebook(TestCase):
    FILE_NAME = 'phonebook.json'
    data = read_from_file(FILE_NAME)

    def test_read_from_file(self):
        with open(self.FILE_NAME, encoding='utf-8') as book:
            for_test = json.load(book)
        self.assertEqual(read_from_file(self.FILE_NAME), for_test)

    def test_add_item(self):
        with MockInputFunction(return_value='test'):
            self.assertEqual(add_item(self.data), {'test': {'city': 'test',
                                                            'first_name': 'test',
                                                            'full_name': 'test',
                                                            'last_name': 'test',
                                                            'phone_number': 'test'}})

    def test_delete_item(self):
        with MockInputFunction(return_value='test'):
            add_item(self.data)
        with MockInputFunction(return_value='test'):
            delete_item(self.data)
        self.assertNotIn('test', self.data)
