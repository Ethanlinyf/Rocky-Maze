"""
Welcome to Rocky-Maze!

A template for a Rocky-Maze game is created.
"""

def welcome_to_rocky_maze_0():
    print("Welcome to Rocky-Maze!")


def welcome_to_rocky_maze_1():
    print("Welcome to Rocky-Maze!")
    print("A template for a Rocky-Maze game is created.")


def welcome_to_rocky_maze_2(name):
    print("Hi, %s, welcome to Rocky-Maze!" % name)


welcome_to_rocky_maze_0()

welcome_to_rocky_maze_1()

welcome_to_rocky_maze_2("John")

name = input("What is your name? ")
welcome_to_rocky_maze_2(name)