"""
By "You"
"""


class Pokemon:
    name = "Pokemon"

    def __init__(self, name, age, typee, size, health, power, magic):
        self.name = name
        self.age = age
        self.typee = typee
        self.health = health
        self.power = power
        self.magic = magic

    def display_pokemon(self):
        print("Pokemon Name: ", self.name)

    # Jade:
    def moves(self):
        pass

    # Colin:
    def drug(self):
        pass

    # Junyu:
    def die(self):
        pass

    # Jason:
    def silence(self):
        pass

    # Junhao:
    def dance(self):
        pass

    # Mia:
    def smile(self):
        print("smiling")

    # Lily:
    def eat(self):
        pass


# define the entrance
def main():
    ditto = Pokemon("Ditto", 69, "SUSSY", 4.20, 420, 0.69, 100)
    # ditto.display_pokemon()

    choice = True

    while choice:
        print("""
            Please chose an option for your Pokemon:
                1. Display a pokemon
                2. Build a capacity for my Pokemon
                4. make your Pokemon laughing
                3. Exit/Quit
                """)

        choice = input("What woule like to choose for your Pokemon:")

        if choice == "1":
            # print("\nSquirtle")
            ditto.display_pokemon()
        elif choice == "2":
            print("\nI can fly.")
        elif choice == "4":
            ditto.smil()
        elif choice == "3":
            print("\nSee you")
            choice = False
        else:
            print("\n Not Valid Choice")


# initial program, green flag
if __name__ == "__main__":
    main()