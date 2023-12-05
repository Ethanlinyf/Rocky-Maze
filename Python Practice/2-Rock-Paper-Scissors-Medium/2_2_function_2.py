"""
Guess Number Game
"""

# import a needed module named random
import random


# a welcome message
def welcome_message():
    print("Welcome to my Guess Number Game")


welcome_message()


# create a magic number
def magic_number(a, b):
    r = random.randint(a, b)

    return r


# print(magic_number())

# input a player's guess number
def player_number():
    a = input("Please input your guess number between 1 and 100: ")
    a = int(a)

    return a


# print(player_number())


# comparision
def determine():
    c = magic_number(1, 100)
    p = player_number()

    if c == p:
        print("Gay REE Yo dog Congrats")
    else:
        print("Pokemon Go")


determine()
