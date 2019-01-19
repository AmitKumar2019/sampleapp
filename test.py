number = list(map(int, input('Enter three numbers: \n').split()))


if number[0] > number[1] and number[0] > number[2]:
    print('{} is greatest'.format(number[0]))

elif number[1] > number[0] and number[1] > number[2]:
    print('{} is greatest'.format(number[1]))

else:
    print(number[2], 'is greatest.')