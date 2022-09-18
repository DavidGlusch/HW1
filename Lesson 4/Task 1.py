string = input()
if len(string) < 2:
    print("Empty String")
else:
    result_string = string[0:2]+string[-2:]
    print(result_string)
