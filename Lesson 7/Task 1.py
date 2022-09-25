data = 'Make a program that has some sentence a string on input and returns a dict containing all unique words as keys and the number of occurrences as values.'
data = data.split()
result = {}
for i in data:
    if i not in result:
        result[i] = 0
    if i in result:
        result[i] += 1

print(result)
