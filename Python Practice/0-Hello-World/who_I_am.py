"""
Practice: variables and functions
"""

print("Hello, Welcome to Python World")

def who_am_i(name, age):
    print("My name is %s and I am %d years old." % (name, age))


name = input("Please input your name: ")
age = input("Please input your age:")
age = int(age)

who_am_i(name, age)