# isHot=False
# is_cold=False
# if isHot:
#     print("It's a hot day")
# elif is_cold and not isHot:
#     print("It's a coldyyy day")
# else:
#     print("It's a fair day!!")
# print('Enjoy!!')
def convertWeight(weight, typeOfWeight):
    if typeOfWeight == 'K':
        return weight / 0.45
    else:
        return weight * 0.45
weight=int(input('Weight: '))
typeOfWeight=input('(L)bs or (K)g: ')
typeOfWeight=typeOfWeight.upper()
if typeOfWeight == 'L':
    print(f"You are {convertWeight(weight, 'L')} kilos")
else:
    print(f"You are {convertWeight(weight, 'K')} pounds")