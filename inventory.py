from weapon import Weapon
from key import Key
from armour import Armour
from healingPad import HealingPad



class Inventory:
    def _init_(self, weapons: list[Weapon] = [], keys: list[Key] = [], armour: Armour = None, healingPad: HealingPad = None):
        self.weapons = weapons
        self.keys = keys
        self.armour = armour
        self.healingPad = healingPad

    def _str_(self):
        inventory_info = "Inventory:\n"
        for weapon in self.weapons:
            inventory_info += f"Weapon: {weapon.name} (Damage: {weapon.damage}, Price: {weapon.price})\n"
        for key in self.keys:
            inventory_info += f"Key: Code: {key.code}, Price: {key.price}\n"
        if self.armour:
            inventory_info += f"Armour: Durability: {self.armour.durability}, Price: {self.armour.price}\n"
        if self.healingPad:
            inventory_info += f"Healing Pad: Health: {self.healingPad.health}, Price: {self.healingPad.price}\n"
        return inventory_info
