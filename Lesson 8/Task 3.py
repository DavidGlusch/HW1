def make_operation(operator, *args):
    args = list(args)
    res = args[0]
    for i in args[1:]:
        if operator == '+':
            res += i
        elif operator == '-':
            res -= i
        elif operator == '*':
            res *= i
    print(res)


make_operation('-', 5, 5, -10, -20)

