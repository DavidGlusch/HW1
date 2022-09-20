import random
s = input('Enter your string: ')
for i in range(5):
    result = "".join(random.sample(s, len(s)))
    print(result, end=' ')