def logger(func):
    def wrapper():
        print('!' * 50)
        print(func)  # NOTE! It should print the function, not the result of its execution!
        print('!' * 50)
    return wrapper


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


add()
square_all()
