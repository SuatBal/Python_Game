class Key:
    def __init__(self, code, price):
        self.code = code
        self.price = price
    
    def __str__(self):
        return f"Key: Code: {self.code}, Price: {self.price}"
