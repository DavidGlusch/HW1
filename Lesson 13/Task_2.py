def first():
    def second():
        return 2 + 2
    return second


def one():
    a = first()
    return a()


print(one())

