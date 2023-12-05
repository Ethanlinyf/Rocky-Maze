import random


class Player:

    def __init__(self, name, age, welcome):
        self.name = name
        self.age = age
        self.welcome = welcome

    def displayPlayer(self):
        print("Name: ", self.name, "| Age: ", self.age)

    def welcome_message(self):
        print(self.welcome)

    def guess_number_game(self):
        (lambda: print("Congrats"), lambda: print("Incorrect"))[random.randint(1,2) == int(input("input your guess: "))]()
    def fire_grass_water(self):
        print("Anita is playing Fire Grass Water game.")

    def rock_paper_scissors(self):
        print("Joshua is playing Rock Paper Scissors.")

    def pokemonGo(self):
        print("Jade is playing PokemonGo game.")

    def GsGo(self):
        print("Henryk is playing GsGo")


Eevee = Player("Anita", 11, "Hello Hoomans")
Jade = Player("Jade", 11, "sucks to be U")
Henryk = Player("Henryk", 11, "chobabmonano")
Josh = Player("Joshua", 10,  "hello")
Lilili = Player("Lilili", -2, "gogo gaga")

print(Eevee.welcome, Jade.welcome, Henryk.welcome, Josh.welcome, Lilili.welcome)

Eevee.fire_grass_water()
Jade.pokemonGo
Josh.rock_paper_scissors()
Henryk.GsGo()
Lilili.guess_number_game()