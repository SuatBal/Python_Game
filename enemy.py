class Enemy:

    def _init_(self, name, damage, health, points=None):
        self.name = name
        self.damage = damage
        self.health = health
        self.points = points
    
    def _str_(self):
        enemy_info = f"Name: {self.name}\n"
        enemy_info += f"Damage: {self.damage}\n"
        enemy_info += f"Health: {self.health}\n"
        enemy_info += f"Points: {self.points}\n"
        return enemy_info