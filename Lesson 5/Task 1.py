import random
random_number = random.randint(1, 10)
task = int(input('Take your guess!:'))
if task == random_number:
    print('Congratulations, You`ve got it!')
else:
    print('Incorrect, try again next time!')
