class HealingPad:
    def _init_(self, health, price):
        self.health = health
        self.price = price
    
    def _str_(self):
        return f"Healing Pad: Health +{self.health}, Price: {self.price}"