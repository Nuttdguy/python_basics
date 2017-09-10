
import random

# availableExits = ['East', 'West', 'North', 'South']
#
# chosenExit = ''
# while chosenExit not in availableExits:
#     chosenExit = input('Please choose a direction: ')
#     if chosenExit == "quit":
#         print("Game Over")
#         break
#
# else:
#     print("Aren't you glad you got out of there!")

highest = 1000
answer = random.randint(1, highest)

print("Please guess a number between 1 and {}: ".format(highest))
guess = int(input())

if guess == answer:
    print("You got it first time")
else:
    while guess != answer:
        if guess < answer:
            print("Please guess higher")
        else:
            print("Please guess lower")

        guess = int(input())
        if guess == answer:
            print("Well done, you guessed the number")
        else:
            print("Sorry, you have not guessed correctly")
