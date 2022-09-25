day_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
result_dict1 = {}
result_dict2 = {}
for i in range(7):
    result_dict1[i+1] = day_list[i]
    result_dict2[day_list[i]] = i+1

print(result_dict1)
print(result_dict2)
