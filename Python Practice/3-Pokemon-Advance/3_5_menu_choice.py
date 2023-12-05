"""
Pokemon Fight Game by Jocelyn, Anita, Joshua, Junyu, Lily

2022-05-01

"""

import random
import time


class Pokemon:

    def __init__(self, name, health, level, move, high, weight):
        self.name = name
        self.health = health
        self.level = level
        self.move = move
        self.high = high
        self.weight = weight

    def display(self):
        print(self.name)

    def attack(self):
        return random.randint(1, 10)

    def rps(self):
        rps_list = ["Rock", "Paper", "Scissors"]

        return random.choice(rps_list)


def stadium(pokemon_1, pokemon_2):
    if pokemon_1.health > 0 and pokemon_2.health > 0:
        print("Action, start to fight ~")

        while True:
            attack_1 = pokemon_1.attack()
            attack_2 = pokemon_2.attack()

            print(pokemon_1.name + "_" + str(pokemon_1.health)
                  + " --- " + str(attack_1) + " ---> "
                  + pokemon_2.name + "_" + str(pokemon_2.health))
            pokemon_2.health = pokemon_2.health - attack_1

            if pokemon_2.health <= 0:
                print(pokemon_1.name + " wins this fight.")
                break

            print(pokemon_1.name + "_" + str(pokemon_1.health)
                  + " <--- " + str(attack_2) + " --- "
                  + pokemon_2.name + "_" + str(pokemon_2.health))
            pokemon_1.health = pokemon_1.health - attack_2

            if pokemon_1.health <= 0:
                print(pokemon_2.name + " wins this fight.")
                break


def main():
    eevee = Pokemon("Eevee", 100, 5, 10, 8, 15)
    ditto = Pokemon("Ditto", 100, 3, 6, 7, 12)

    # eevee.display()
    # ditto.display()

    choice = True

    while choice:
        print("""
                1. Display your choice
                2. Fight
                3. Exit(Quit)
        """)

        choice = input("What is your choice for your Pokemon: ")

        if choice == "1":
            print(eevee.rps())
            print(ditto.rps())

        elif choice == "2":
            # print("fight")
            # stadium(eevee, ditto)

            while True:
                rps_1 = eevee.rps()
                rps_2 = ditto.rps()

                if rps_1 == rps_2:
                    print("It is a tie")
                    continue
                elif rps_1 == "Rock":
                    if rps_2 == "Paper":
                        stadium(ditto, eevee)
                        break
                    else:
                        stadium(eevee, ditto)
                        break
                elif rps_1 == "Paper":
                    if rps_2 == "Scissors":
                        stadium(ditto, eevee)
                        break
                    else:
                        stadium(eevee, ditto)
                        break
                elif rps_1 == "Scissors":
                    if rps_2 == "Rock":
                        stadium(ditto, eevee)
                        break
                    else:
                        stadium(eevee, ditto)
                        break
                else:
                    print("No fight ~ ")



        elif choice == "3":
            print("See you ~")
            choice = False

        else:
            print("Not valid choice.")


if __name__ == "__main__":
    main()
