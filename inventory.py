from weapon import Weapon
from key import Key
from armour import Armour


class Inventory:
    def __init__(self, weapons: list[Weapon] = [], keys: list[Key] = [], armor: Armour = None):
        self.weapons = weapons
        self.keys = keys
        self.armor = armor

    def __str__(self):
        inventory_info = "Inventory:\n"
        for weapon in self.weapons:
            inventory_info += f"Weapon: {weapon.name} (Damage: {weapon.damage}, Price: {weapon.price})\n"
        for key in self.keys:
            inventory_info += f"Key: Code: {key.code}, Price: {key.price}\n"
        if self.armor:
            inventory_info += f"Armor: Durability: {self.armor.durability}, Price: {self.armor.price}\n"
        return inventory_info
