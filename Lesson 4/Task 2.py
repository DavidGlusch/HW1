phone_number = str(input())
if len(phone_number) == 10 and phone_number.isdigit():
    print('This phone number is valid')
else:
    print('This phone number is invalid')
