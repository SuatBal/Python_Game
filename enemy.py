class Enemy:

    def __init__(self, name, damage, health, points=None):
        self.name = name
        self.damage = damage
        self.health = health
        self.points = points
    
    def __str__(self):
        enemy_info = f"Name: {self.name}\n"
        enemy_info += f"Damage: {self.damage}\n"
        enemy_info += f"Health: {self.health}\n"
        enemy_info += f"Points: {self.points}\n"
        return enemy_info
        
        
