class CuddlyToy:
    def __init__(self, name="Unknown", size="Medium", color="White"):
        self.name = name
        self.size = size
        self.color = color

    def set_name(self, n):
        self.name = n

    def set_size(self, s):
        self.size = s

    def set_color(self, c):
        self.color = c

    def get_name(self):
        return self.name

    def get_size(self):
        return self.size

    def get_color(self):
        return self.color

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Size: {self.size}")
        print(f"Color: {self.color}")


# Intermediate Class - Teddy
class Teddy(CuddlyToy):
    def __init__(self, name="Unknown", size="Medium", color="White"):
        super().__init__(name, size, color)

    def make_sound(self):
        print("Teddy growls: Grrr!")

    def hug(self):
        print("Teddy gives a hug.")


# Engineer (Blue Teddy)
class Engineer(Teddy):
    def __init__(self, name="Unknown", size="Medium", color="White"):
        super().__init__(name, size, color)

    def build_robot(self):
        print("Engineer builds an intellectual robot.")

    def write_code(self):
        print("Engineer is writing a complicated Java code.")


# Gardener (Red Teddy)
class Gardener(Teddy):
    def __init__(self, name="Unknown", size="Medium", color="White"):
        super().__init__(name, size, color)

    def plant_flowers(self):
        print("Gardener plants colorful and adorable flowers.")

    def water_plants(self):
        print("Gardener waters the plants in solace manner.")


# Intermediate Class - Bunny
class Bunny(CuddlyToy):
    def __init__(self, name="Unknown", size="Medium", color="White"):
        super().__init__(name, size, color)

    def jump_around(self):
        print("Bunny jumps around delightfully.")

    def blink_ears(self):
        print("Bunny blinks its ears sarcastically.")


# Clown (White Bunny)
class Clown(Bunny):
    def __init__(self, name="Unknown", size="Medium", color="White"):
        super().__init__(name, size, color)

    def tell_joke(self):
        print("Clown tells a joke.")

    def do_magic(self):
        print("Clown performs magic tricks.")


# Bank Manager (Black Bunny)
class BankManager(Bunny):
    def __init__(self, name="Unknown", size="Medium", color="White"):
        super().__init__(name, size, color)

    def open_account(self):
        print("BankManager opens a savings account for protection.")

    def print_balance(self):
        print("BankManager prints the toy's balance slip in a funny manner.")
