class Weapon:
    def __init__(self, name, damage, price):
        self.name = name
        self.damage = damage
        self.price = price
    
    def __str__(self):
        return f"Weapon: {self.name} (Damage: {self.damage}, Price: {self.price})"

