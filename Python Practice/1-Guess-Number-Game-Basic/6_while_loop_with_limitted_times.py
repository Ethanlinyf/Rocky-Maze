"""
using while loop with limited times
"""

import random

print("Welcome to this Guess Number Game")

random_number = random.randint(1, 100)

# print(random_number)

guess_number = int(input("Please input your guess number: "))

times = 0

while True:
    times = times +1
    if guess_number == random_number:
        print("Congratulations")
        break
    else:
        if times == 10:
            print("you are using all the guess oportunities. The random number is %d." % (random_number))
            break
        # print("Wrong guess number, try it again")
        if guess_number > random_number:
            print("Your guess is too big. Try it again.")
        else:
            print("Your guess is too low. Try it again.")
        guess_number = int(input ("Please input your guess number: "))