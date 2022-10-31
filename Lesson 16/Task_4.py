class CustomException(Exception):
    def __init__(self, msg):
        self.msg = msg
        with open('logs.txt', 'w') as message:
            message.write(self.msg)


def add(a, b):
    if a > 0 and b > 0:
        return a + b
    else:
        raise CustomException('a or b is less than 0')


add(-1, -1)

