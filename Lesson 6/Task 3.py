list_1 = []
count = 0
result_list = []
i = 0
while len(list_1) != 100:
    count += 1
    list_1.append(count)
while i != 100:
    if list_1[i] % 7 == 0 and list_1[i] % 5 != 0:
        result_list.append(list_1[i])
    i += 1
print(result_list)

