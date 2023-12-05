import random

print("Hello, welcome to my Guessing Number Game!")

magic_number = random.randint(1, 100)
# print(magic_number)

guess_number = input("Please input your guessing number between 1, 100: ")
# print(guess_number)
guess_number = int(guess_number)

if guess_number == magic_number:
    print("Congratulations")
else:
    print("Incorrect, the magic number is %d" % (magic_number))