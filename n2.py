class Clothes:
    def __init__(self, V, H):
        self.V = V
        self.H = H

    def get_m_jacket(self):
        return self.V / 6.5 + 0.5
    def get_m_costume(self):
        return self.H * 2 + 0,3
    @property
    def get_full(self):
        return f"пл.ткани\: " \
            f"((self.V / 6.5 + 0.5) + (self.H * 2 + 0, 3))"

class Jacket(Clothes):
    def __init__(self, V, H):
        super().__init__(V, H)
        self.m_jacket = round(self.V / 6.5 + 0.5)
    def __str__(self):
        return f'пальто {self.m_jacket}'

class Costume(Clothes):
    def __init__(self, V, H):
        super().__init__(V, H)
        self.m_costume = round(self.H * 2 + 0.3)
    def __str__(self):
        return f'костюм {self.m_costume}'

jacket = Jacket(10, 40)
costume = Costume(5, 10)
print(jacket)
print(costume)







