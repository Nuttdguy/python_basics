name = input('Please enter your name: ')  # get string input
age = int(input('How old are you, {0}? '.format(name)))  # for getting integer input

if age >= 21:
    print('You\'re old enough for to drink alcohol')
else:
    print('You have %d years before you can drink alcohol %s' % (21 - age, name))  # formatting using interpolation

if age >= 16 and age <= 65:  # using 'and' and greater than | equal
    print('You\'re old')

if (age >= 16) and (age <= 65):  # can contain within parenthesis
    print('You\'re old')

