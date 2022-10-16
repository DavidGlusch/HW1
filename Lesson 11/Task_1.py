with open('my_file.txt', 'w') as my_file:
    my_file.write("Hello file world!")
with open('my_file.txt') as my_file:
    print(my_file.read())