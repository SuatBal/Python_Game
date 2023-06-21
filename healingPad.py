class HealingPad:
    def __init__(self, health, price):
        self.health = health
        self.price = price
    
    def __str__(self):
        return f"Healing Pad: Health +{self.health}, Price: {self.price}"
