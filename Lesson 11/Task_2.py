import json

FILE_NAME = 'phonebook.json'


def save_to_disk(phone_book: dict, file_name: str) -> None:
    """
    :param phone_book: dict object
    :param file_name: str file_name. Example: phonebook.json
    :return: None
    """
    with open(file_name, "w") as file:
        json.dump(phone_book, file)


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


def search_phone_number(my_book):
    try:
        search_phone = input("Please, write your number: ")
        print(my_book[search_phone])
    except KeyError:
        print("Your phone does not exist!")


def search_first_name(my_book):
    search_first = input("Please, write first name: ")
    flag = False
    for k, v in my_book.items():
        if search_first == my_book[k]['first_name']:
            print(my_book[k])
            flag = True
    if not flag:
        print("Entered first name does not exist!")


def search_last_name(my_book):
    search_last = input("Please, write last name: ")
    flag = False
    for k, v in my_book.items():
        if search_last == my_book[k]['last_name']:
            print(my_book[k])
            flag = True
    if not flag:
        print("Entered last name does not exist!")


def search_full_name(my_book):
    search_full = input("Please, write full name: ")
    flag = False
    for k, v in my_book.items():
        if search_full == my_book[k]['full_name']:
            print(my_book[k])
            flag = True
    if not flag:
        print("Entered full name does not exist!")


def search_city_state(my_book):
    search_city = input("Please, city name: ")
    flag = False
    for k, v in my_book.items():
        if search_city == my_book[k]['city']:
            print(my_book[k])
            flag = True
    if not flag:
        print("Entered city does not exist!")




if __name__ == '__main__':
    data = read_from_file(FILE_NAME)
    if data is None:
        data = {}
    while True:
        choice = input("""
1 Add new entries
2 Search by first name
3 Search by last name
4 Search by full name
5 Search by telephone number
6 Search by city or state
7 Delete a record for a given telephone number
8 Update a record for a given telephone number
9 Look what we have
10 Exit!\n""")

        if choice == '1':
            add_item(data)
        elif choice == '2':
            search_first_name(data)
        elif choice == '3':
            search_last_name(data)
        elif choice == '4':
            search_full_name(data)
        elif choice == '5':
            search_phone_number(data)
        elif choice == '6':
            search_city_state(data)
        elif choice == '7':
            delete_item(data)
        elif choice == '8':
            update_item(data)
        elif choice == '9':
            print(data)
        if choice == '10':
            save_to_disk(data, FILE_NAME)
