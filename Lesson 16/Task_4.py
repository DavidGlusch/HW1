class CustomException(Exception):
    @staticmethod
    def save_error_message(msg):
        print(msg)
        with open('logs.txt', 'w') as message:
            message.write(msg)


def add(a, b):
    if a > 0 and b > 0:
        return a + b
    else:
        raise CustomException.save_error_message('a or b is less than 0')


add(-1, -1)

