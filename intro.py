# isHot=False
# is_cold=False
# if isHot:
#     print("It's a hot day")
# elif is_cold and not isHot:
#     print("It's a coldyyy day")
# else:
#     print("It's a fair day!!")
# print('Enjoy!!')
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
secret=21
guess_count=0
guess_limit=int(input('How many guesses do you want? '))
while guess_count < guess_limit:
    guess = int (input('Guess: '))
    guess_count+=1
    if guess == secret:
        print('You won✅:)')
        break
    else:
        if guess_count == guess_limit:
            print('You lost❌:(')
        else:
            print('Incorrect ^_^ please try again..')