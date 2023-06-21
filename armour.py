class Armour:
    def __init__(self, durability:int, price:int):
        self.durability:int = durability
        self.price:int = price
    
    def __str__(self):
        return f"Armour: Durability: {self.durability}, Price: {self.price}"

