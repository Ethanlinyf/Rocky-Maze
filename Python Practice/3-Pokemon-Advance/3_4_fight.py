"""

By Colin, Jade, Jason, Junhao, Junyu

"""

import random
import time


class Pokemon:
    name = "Pokemon"

    def __init__(self, name, age, typee, health, level):
        self.name = name
        self.age = age
        self.typee = typee
        self.health = health
        self.magic = level

    def display_pokemon(self):
        print(self.name + ", health: " + str(self.health))

    def attack(self, style):
        if style == "arena":
            basic_damage = random.randint(1, 10)

            return basic_damage


def stadium(pokemon_1, pokemon_2):
    print("Action, start to fight ~ ")

    while pokemon_1.health > 0 and pokemon_2.health > 0:
        attack_1 = pokemon_1.attack("arena")
        attack_2 = pokemon_2.attack("arena")

        print(pokemon_1.name + "_" + str(pokemon_1.health)
              + "---" + str(attack_1) + "--->"
              + pokemon_2.name + "_" + str(pokemon_2.health))
        pokemon_2.health = pokemon_2.health - attack_1

        time.sleep(1)

        print(pokemon_1.name + "_" + str(pokemon_1.health)
              + "<---" + str(attack_2) + "---"
              + pokemon_2.name + "_" + str(pokemon_2.health))
        pokemon_1.health = pokemon_1.health - attack_2

        time.sleep(1)

        if pokemon_1.health <= 0:
            print(pokemon_2.name + " wins this fight")
        elif pokemon_2.health <= 0:
            print(pokemon_1.name + " wins this fight")
        else:
            continue


def main():
    runeriges = Pokemon("Runeriges", 6582, "Gost", 100, 1)
    charizard = Pokemon("Charizard", 1000, "Fire", 100, 2)

    # runeriges.display_pokemon()
    # charizard.display_pokemon()
    stadium(runeriges, charizard)


if __name__ == "__main__":
    main()