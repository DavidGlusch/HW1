def oops():
    raise IndexError


def catch_error():
    try:
        print(oops())
    except IndexError:
        return 'Error caught'


print(catch_error())
