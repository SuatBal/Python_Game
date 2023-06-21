from enemy import Enemy
from weapon import Weapon
from treasure import Treasure
from key import Key
from room import Room
from player import Player
from inventory import Inventory
from healingPad import HealingPad
from armour import Armour

def read_shop_data():
    shop_data = {}
    weapons = {}
    keys = {}
    healing_pads = {}
    armours = {}
    with open("Shop.txt", 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            if line.startswith("weapon"):
                weapon_data = line.split(":")
                weapon_name = weapon_data[0]
                name, damage, price = map(str, weapon_data[1].split(","))
                weapon = Weapon(name=name, damage=int(
                    damage), price=int(price))
                weapons[weapon_name] = weapon

            elif line.startswith("key"):
                key_data = line.split(":")
                code, price = map(str, key_data[1].split(","))
                key = Key(code=int(code), price=int(price))
                keys[code] = key

            elif line.startswith("healingPad"):
                healing_pad_data = line.split(":")
                healing_pad_name = healing_pad_data[0]
                health, price = map(str, healing_pad_data[1].split(","))
                healing_pad = HealingPad(
                    health=int(health), price=int(price))
                healing_pads[healing_pad_name] = healing_pad

            elif line.startswith("armour"):
                armour_data = line.split(":")
                armour_name = armour_data[0]
                durability, price = map(str, armour_data[1].split(","))
                armour = Armour(durability=int(durability), price=int(price))
                armours[armour_name] = armour
              
        
        shop_data["weapons"] = weapons
        shop_data["keys"] = keys
        shop_data["healing_pads"] = healing_pads
        shop_data["armours"] = armours
        
        return shop_data


# Example usage:
shop_data = read_shop_data()
print("Shop Data:")
print("Weapons:")

for weapon_name, weapon in shop_data["weapons"].items():
    print(weapon)
print("Keys:")
for code, key in shop_data["keys"].items():
    print(key)
print("Healing Pads:")
for healing_pad_name, healing_pad in shop_data["healing_pads"].items():
    print(healing_pad)
print("Armours:")
for armour_name, armour in shop_data["armours"].items():
    print(armour)
