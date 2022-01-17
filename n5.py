class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        return "Начать рисовать", self.title

class Pen:
    def __init__(self, title):
        self.title = title
    def draw(self):
        return  self.title, "рисовать ручкой"
class Pencil:
    def __init__(self, title):
        self.title = title
    def draw(self):
        return self.title, "рисовать карандашом"
class Handle:
    def __init__(self, title):
        self.title = title
    def draw(self):
        return  self.title, "рисовать маркером"

pen = Pen("Ручка")
pencil = Pencil("карандаш")
handle = Handle("маркер")
print(pen.draw())
print(pencil.draw())
print(handle.draw())