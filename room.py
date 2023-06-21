from enemy import Enemy
from weapon import Weapon
from treasure import Treasure
from key import Key

class Room:
    def __init__(self, description, enemy:Enemy, points:int, weapon:Weapon, money:int, treasure:Treasure, healingPad, key:Key):
        self.description = description
        self.enemy = enemy
        self.points = points
        self.weapon = weapon
        self.money = money
        self.treasure = treasure
        self.healingPad = healingPad
        self.key = key
    
    def __str__(self):
        room_info = f"Description: {self.description}\n"
        room_info += f"Enemy: {self.enemy.name} (Damage: {self.enemy.damage}, Health: {self.enemy.health})\n"
        room_info += f"Points: {self.points}\n"
        room_info += f"Weapon: {self.weapon.name} (Damage: {self.weapon.damage}, Price: {self.weapon.price})\n"
        room_info += f"Money: {self.money}\n"
        if self.treasure == None:
            room_info += f"Treasure: None\n"
        else:
            room_info += f"Treasure: Code: {self.treasure.code}, Point: {self.treasure.point}\n"
        
        if self.healingPad == None:
            room_info += f"Healing Pad: None\n"
        else:
            room_info += f"Healing Pad: {self.healingPad}\n"
        
        if self.key == None:
            room_info += f"Key: None\n"
        else:            
            room_info += f"Key: Code: {self.key.code}, Price {self.key.price}\n"
        return room_info
