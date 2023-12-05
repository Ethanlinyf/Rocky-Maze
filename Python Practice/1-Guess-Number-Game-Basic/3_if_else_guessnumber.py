"""
If elseif else statements
"""



import random

print("Hello, welcome to my Guessing Number Game!")

magic_number = random.randint(1, 100)
# print(magic_number)

guess_number = input("Please input your guessing number: between 1, 100 ")
# print(guess_number)
guess_number = int(guess_number)

if guess_number == magic_number:
    print("Congratulations")
elif guess_number > magic_number:
    print("Too big, the magic number is %d"%(magic_number))
else:
    print("Too small, the magic number is %d"%(magic_number))