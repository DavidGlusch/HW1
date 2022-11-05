class TypeDecorators:

    @staticmethod
    def to_int(func):
        def wrapper(*args, **kwargs):
            try:
                return int(func(*args, **kwargs))
            except ValueError as e:
                return f'Cant convert this data type to int, {e}'
        return wrapper

    @staticmethod
    def to_str(func):
        def wrapper(*args, **kwargs):
            try:
                return str(func(*args, **kwargs))
            except ValueError as e:
                return f'Cant convert this data type to str, {e}'
        return wrapper

    @staticmethod
    def to_bool(func):
        def wrapper(*args, **kwargs):
            try:
                return bool(func(*args, **kwargs))
            except ValueError as e:
                return f'Cant convert this data type to bool, {e}'
        return wrapper

    @staticmethod
    def to_float(func):
        def wrapper(*args, **kwargs):
            try:
                return float(func(*args, **kwargs))
            except ValueError as e:
                return f'Cant convert this data type to float, {e}'
        return wrapper


@TypeDecorators.to_int
def test1(n):
    return n


@TypeDecorators.to_str
def test2(n):
    return n


@TypeDecorators.to_bool
def test3(n):
    return n


@TypeDecorators.to_float
def test4(n):
    return n


print(test1('54'), type(test1('54')))
print(test2(45), type(test2(45)))
print(test3('1'), type(test3('1')))
print(test4('54.6'), type(test4('54.6')))
