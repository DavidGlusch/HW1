import random
random.seed()
result = []
while len(result) != 10:
    result.append(random.randint(1, 10))
print(max(result))





