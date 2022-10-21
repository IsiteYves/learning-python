import random

choice = 2
print('''
0) Exit
1) Roll again
      ''')
while choice != 0:
    choice = int(input('>'))
    if choice ==  0:
        break
    else:
        print(f'({random.randint(1, 6)}, {random.randint(1, 6)})')
