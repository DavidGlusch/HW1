def number(a, b):
    try:
        return int(a)*int(a) / int(b)
    except ZeroDivisionError:
        raise ZeroDivisionError('Cannot divide by zero')
    except TypeError:
        raise TypeError('One of parameters isn`t a number')




print(number(input('Number a: '), input('Number b: ')))
