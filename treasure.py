class Treasure:
    def __init__(self, code, point):
        self.code = code
        self.point = point
    
    def __str__(self):
        return f"Treasure: (Code: {self.code}, Point: {self.point})"
