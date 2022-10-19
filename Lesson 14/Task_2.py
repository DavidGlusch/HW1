def stop_words(words: list):
    def decorator(func):
        def wrapper(name):
            result = ""
            func_ex = func(name)
            for i in func_ex.split():
                if i in words:
                    result += '****'
                    result += ' '
                else:
                    result += i
                    result += ' '
            print(result)
        return wrapper
    return decorator


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW !"


create_slogan("Steve")
