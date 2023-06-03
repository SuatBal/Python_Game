import random
from inventory import Inventory

MIN_MONEY = 50
MAX_MONEY = 310
INITIAL_HEALTH = 100
INITIAL_POINTS = 0

class Player:

    def __init__(self, name):
        self.name = name
        self.money = random.randint(MIN_MONEY, MAX_MONEY)
        self.health = INITIAL_HEALTH
        self.points = INITIAL_POINTS
        self.inventory = Inventory()
