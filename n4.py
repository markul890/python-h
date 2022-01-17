class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return self.name(" поехала")
    def stop(self):
        return self.name(" остановилась")
    def turn_right(self):
        return self.name("повернула вправо")
    def turn_left(self):
        return self.name("повернула влево")
    def show_speed(self):
        return self.speed("это скорость авто")

class TownCar(Car):
    def init(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def show_speed(self):
        print("Скорость авто", self.speed)
        if self.speed > 60:
            print("Превышение скорости")


class WorkCar(Car):
    def init(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        print("Скорость авто", self.speed)
        if self.speed > 40:
            print("Превышение скорости")


class SportCar(Car):
    def init(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name

class PoliceCar(Car):
    def init(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

ferari = SportCar(200,"red", "ferari", False)
wolkswagen = TownCar(70,"green","wolkswagen", False)
skoda = WorkCar(90, "white", "skoda", False )
ford = PoliceCar(100, "blue", "ford", True)
print(ford.turn_right())
print(wolkswagen.turn_left())
print(ferari.go())
print(skoda.stop())
print(ford.show_speed())
print(ferari.show_speed())