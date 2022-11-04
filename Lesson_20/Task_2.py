import json
import unittest
# import sys
# from Lesson_11.Task_2 import add_item, read_from_file,  delete_item, update_item
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


def update_item(my_book: dict):
    phone_num = input("Enter phone number you would like to change: ")
    phone_num_new = input('Enter new phone number: ')
    new_city = input("Enter new city: ")
    my_book[phone_num]['phone_number'] = phone_num_new
    if new_city:
        my_book[phone_num]['city'] = new_city
    my_book[phone_num_new] = my_book[phone_num]
    del my_book[phone_num]
    return my_book


class TestPhonebook(unittest.TestCase):
    FILE_NAME = 'phonebook.json'
    data = read_from_file(FILE_NAME)

    def test_read_from_file(self):
        with open(self.FILE_NAME, encoding='utf-8') as book:
            for_test = json.load(book)
        self.assertEqual(read_from_file(self.FILE_NAME), for_test)

    def test_add_item(self):
        self.data_before_add = self.data.copy()
        print('Testing add_item')
        add_item(self.data)
        self.assertNotEqual(self.data, self.data_before_add)

    def test_update_item(self):
        print("Testing update_item")
        data_before_update = self.data.copy()
        print(data_before_update)
        update_item(self.data)
        self.assertNotEqual(data_before_update, self.data)

    def test_delete_item(self):
        print('Testing delete_item')
        print('Choose phone number to delete')
        data_before_delete = self.data.copy()
        print(data_before_delete)
        delete_item(self.data)
        self.assertNotEqual(data_before_delete, self.data)
        print(self.data)
        print(data_before_delete)








