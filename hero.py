import random

class Hero:
    """The hero blueprint will be implemented later in the project."""

    def __init__(self, name):
        self.name = "Tommy"
        self.health = 120
        self.attack_power = 20

    def attack(self):
        random.ranint(1,120)

    def take_damage(self, damage):
        self.health = max(0, self.health - damage)

    def is_alive(self):
        return self.health > 0

    def hero_class(role):
        if random.randint(1,4) == 1:
            self.role = "Knight"
        elif random.randint(1,4) == 2:
            self.role = "Mage"
        elif random.randint(1,4) == 3:
            self.role = "Hacker"
        else:
            self.role = "Ranger"
        return self.role



