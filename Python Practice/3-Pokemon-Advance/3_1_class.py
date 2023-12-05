"""
Pokemon Go Platform
"""


class Pokemon:
    name = "Pokemon"
    age = 0
    size = 0
    SN = 0

    def __init__(self, name, age, typee, health, power, magic):
        self.name = name
        self.age = age
        self.typee = typee
        self.health = health
        self.power = power
        self.magic = magic

    def display_pokemon(self):
        print("My Pokemon is ", self.name)


def welcome_message():
    print("Welcome to our session for Python programming")

    charmamder = Pokemon("Charmamder", 5, "Fire", 39, 5, 20)
    charmamder.display_pokemon()


def main():
    welcome_message()


if __name__ == "__main__":
    main()