class Enemy:

    def __init__(self, name:str, damage:int, health:int, points:int=None):
        self.name:str = name
        self.damage:int = damage
        self.health:int = health
        self.points:int = points
    
    def __str__(self):
        enemy_info = f"Name: {self.name}\n"
        enemy_info += f"Damage: {self.damage}\n"
        enemy_info += f"Health: {self.health}\n"
        enemy_info += f"Points: {self.points}\n"
        return enemy_info
        
        
