import random
from enemy import enemy

class Goblin(enemy):
    """A completed character class students can examine as an OOP example."""

    def __init__(self, name):
        super().__init__(name, health = 100, attackPower = 15)
        self.attack_power = 15
        self.gold = 0

    def stealGold(self, hero):
        """Return a random amount of damage."""
        self.gold += hero.gold
        hero.gold = 0
        print("GET REKT NOOB")
