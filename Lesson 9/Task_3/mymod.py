def count_lines(name):
    # file_lines = name.readlines()
    # return len(file_lines) : таким образом возвращал пустой список, почему?
    with open(r"test.txt", 'r') as fp:
        x = len(fp.readlines())
    return x


def count_chars(name):
    file_chars = name.read()
    return len(file_chars)


def test(name):
    print(count_lines(name))
    print(count_chars(name))
    return ''# если написать: 'return count_chars(name), count_lines(name)', то второе значение показывает 0, почему?



f = open('test.txt', 'r')
print(test(f))
