from weapon import Weapon
from key import Key
from armour import Armour
from healingPad import HealingPad

class Inventory:
    def __init__(self, weapons:list[Weapon]=[], keys:list[Key]=[], armour:Armour=None, healingPad:HealingPad=None):
        self.weapons:list[Weapon] = weapons
        self.keys:list[Key] = keys
        self.armour:Armour = armour
        self.healingPad:HealingPad = healingPad
    
    def  __str__(self):
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
             
       