class Armour:
    def _init_(self, durability:int, price:int):
        self.durability:int = durability
        self.price:int = price
    
    def _str_(self):
        return f"Armour: Durability: {self.durability}, Price: {self.price}"