def make_operation(operator, *args):
    args = list(args)
    res = args[-1]
    for i in range(len(args)-1):
        if operator == '+':
            res += args[i]
        elif operator == '-':
            res -= args[i]
        elif operator == '*':
            res *= args[i]
    print(res)


make_operation('*', 7, 6)

