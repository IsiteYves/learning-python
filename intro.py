# kilos-pounds & vice-versa converter
# def convertWeight(weight, typeOfWeight):
#     if typeOfWeight == 'K':
#         return weight / 0.45
#     else:
#         return weight * 0.45
# weight=int(input('Weight: '))
# typeOfWeight=input('(L)bs or (K)g: ')
# typeOfWeight=typeOfWeight.upper()
# if typeOfWeight == 'L':
#     print(f"You are {convertWeight(weight, 'L')} kilos")
# else:
#     print(f"You are {convertWeight(weight, 'K')} pounds")

# guessing game
# secret = 21
# guess_count = 0
# guess_limit=-3
# while guess_limit not in range(1, 11):
#     guess_limit = int(input('How many guesses do you want? '))
#     if guess_limit in range(1, 11):
#         break
#     print('You can only have 1-10 guesses')
# while guess_count < guess_limit:
#     guess = int(input('Guess: '))
#     guess_count += 1
#     if guess == secret:
#         print('You won✅:)')
#         break
#     else:
#         if guess_count == guess_limit:
#             print('You lost❌:(')
#         else:
#             print('Incorrect ^_^ please try again..')
            
cmd='default'
while cmd != 'quit':
    prev_cmd = cmd
    cmd = input('>').lower()
    if cmd == 'help':
        print('''
start - to start the car
stop - to stop the car
quit/exit - to quit
              ''')
    elif cmd == 'start':
        print('Car started...')
    elif cmd == 'stop':
        if prev_cmd != 'start':
            print("Car wasn't moving to be stopped❌")
        else:
            print('Car stopped.')
    elif cmd == 'quit' or cmd == 'exit':
        break
    else:
        print('I don\'t understand that...')
