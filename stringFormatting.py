__author__ = 'dev'
age = 24
print('My age is ' + str(age) + ' years') # must wrap integer to convert to string format

print('My age is {0} years'.format(age)) # placeholder is formatted position - similiar to string interpolation

print("""
January: {2}
February: {3}
March: {2}
April: {1}
May: {0}
June: {1}
July: {3}
""".format(20,33,12,56)) # allows multi-line and reuse of placeholder values

print('My age is %d years' % age)
print('My age is %d %s, %d %s' % (age, 'years', 6, 'months')) # multiple placeholders for inserting values

for i in range(1, 12):
    print('No. %2d squared is %4d and cubed is %4d' %(i, i ** 2, i ** 3)) # formatting with padding

print('Pi is approximately %12.20f' %(22 / 7)) # can define number of decimal places

for i in range(1, 12):
    print('No. {0:2} squared is {1:4} and cubed is {2:4}'.format(i, i ** 2, i ** 3)) # formatting with padding and position

for i in range(1, 12):
    print('No. {0:2} squared is {1:<4} and cubed is {2:<4}'.format(i, i ** 2, i ** 3)) # formatting with padding and position and justified

print(__author__)