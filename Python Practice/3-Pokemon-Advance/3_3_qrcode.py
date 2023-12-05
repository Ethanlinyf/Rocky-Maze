import qrcode


class Pokemon:
    def __init__(self, name, size, age, health):
        self.name = name
        self.size = size
        self.age = age
        self.health = health

    def pokemon_qrcode(self, message):
        image_pok = qrcode.make(message)
        image_pok.show()
        image_pok.save(self.name)

    def display_pokemon(self):
        print("Pokemon Name: ", self.name)


def main():
    eevee = Pokemon("Eevee", 3, 6, 100)

    print("""
            Please choose an option for your Pokemon:
            1. Display your pokemon name;
            2. Create your pokemon QR code;
            3. Exit/Quit
    """)

    choice = input("Please input your choice: ")

    if choice == "1":
        eevee.display_pokemon()
    elif choice == "2":
        eevee.pokemon_qrcode("thethingsengine.org")


if __name__ == "__main__":
    main()
