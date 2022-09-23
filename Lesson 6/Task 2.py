import random
random.seed()
list_1 = []
list_2 = []
result_list = []
while len(list_1) != 10:
    list_1.append(random.randint(1, 10))
    list_2.append(random.randint(1, 10))

for i in list_1:
    if i in list_2 and i not in result_list:
        result_list.append(i)
print(list_1, list_2, result_list, sep='\n')
