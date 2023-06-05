class Weapon:
    def _init_(self, name, damage, price):
        self.name = name
        self.damage = damage
        self.price = price

    def _str_(self):
        return f"Weapon: {self.name} (Damage: {self.damage}, Price: {self.price})"
