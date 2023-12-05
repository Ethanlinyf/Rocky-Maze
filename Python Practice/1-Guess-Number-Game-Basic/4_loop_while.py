"""
While loop
"""

import random

print("Welcome to this guess money game")

random_number = random.randint(1, 10)

guess_number = input ("Please input your guess number: ")

guess_number = int(guess_number)

while True:
    if guess_number == random_number:
        print("Congratulations")
        break
    else:
        print("Wrong guess number, try it again")
        guess_number = int(input ("Please input your guess number: "))