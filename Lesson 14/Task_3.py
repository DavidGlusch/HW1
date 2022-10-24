def arg_rules(type_: type, max_length: int, contains: list):
    def decorator(func):
        def wrapper(name):
            func_ex = func(name)
            for i in contains:
                if i not in name:
                    print(f"{i} not in the list {contains}")
                    return False
            if len(name) >= max_length:
                print(f'Maximum length is {max_length}')
                return False
            elif type(name) != type_:
                print(f'Type must be {type_}')
                return False

            else:
                print(func_ex)
                return func_ex
        return wrapper
    return decorator


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW !"


if create_slogan('johndoe05@gmail.com'):
    print(1)
else:
    print(0)



