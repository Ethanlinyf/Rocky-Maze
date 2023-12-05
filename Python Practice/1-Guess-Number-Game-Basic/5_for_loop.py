"""
for loop with limited times
"""

import random

print("Welcome to My Guess Number Game!")

magic_number = random.randint(1,100)

for times in range(5):
    guess_number = input("Please input your guess number: ")
    guess_number = int(guess_number)

    if guess_number == magic_number:
        print("Congratulation!")
        break
    elif guess_number > magic_number:
        print("Too big")
        if times == 4:
            print("You have used all the times/opportunies")
        continue
    else:
        print("Too small")
        if times == 4:
            print("You have used all the times/opportunities")
        continue
        if times == 4:
            print("You have used all the times/opportunities")