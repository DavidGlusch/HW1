def logger(func):
    def wrapper(*args):
        print('!' * 50)
        print(f'{func.__name__} called with {args}')
        print('!' * 50)
    return wrapper


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


add(4, 6)
square_all(3, 5, 7 ,8)
