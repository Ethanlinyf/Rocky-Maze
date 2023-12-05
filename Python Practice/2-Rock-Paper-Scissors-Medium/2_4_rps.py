"""
Rock Paper Scissors
"""

import random


def welcome_message():
    print("Welcome to My Rock Paper Scissors Game!")


def computer_choice():
    rps = ["rock", "paper", "scissors"]

    return random.choice(rps)


def player_choice():
    return input("Let's play: ")


def comparison():
    c = computer_choice()
    p = player_choice()

    if p == c:
        return "It's a tie!"
    elif (p == "rock" and c == "scissors") or \
            (p == "scissors" and c == "paper") or \
            (p == "paper" and c == "rock"):
        return "You win!"
    else:
        return "You lose!"


# please implement the comparison for this game

def main():
    welcome_message()
    print(comparison())


if __name__ == "__main__":
    main()
