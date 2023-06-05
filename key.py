class Key:
    def _init_(self, code, price):
        self.code = code
        self.price = price

    def _str_(self):
        return f"Key: Code: {self.code}, Price: {self.price}"
