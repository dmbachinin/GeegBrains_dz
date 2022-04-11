
class Car:
    speed_now = 0
    def __init__(self,speed,name,color,is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        if is_police:
            self.is_police = True
        else:
            self.is_police = False

    def go(self):
        print(f"{self.name} поехала")
        self.speed_now = self.speed

    def stop(self):
        print(f"{self.name} остановилась")
        self.speed_now = 0

    def turn(self, direction):
        print(f"{self.name} повернула {direction}")

    def show_speed(self):
        print(f"cкорость {self.name}: {self.speed_now}")

class TownCar(Car):
    speed_limit = 60
    def show_speed(self):
        print(f"cкорость {self.name}: {self.speed_now}")
        if self.speed_now > self.speed_limit:
            print(f"{self.name} превысила скорость!")
            self.speed_now = self.speed_limit

class SportCar(Car):
    pass
class WorkCar(Car):
    speed_limit = 40
    def show_speed(self):
        print(f"cкорость {self.name}: {self.speed_now}")
        if self.speed_now > self.speed_limit:
            print(f"{self.name} превысила скорость!")
            self.speed_now = self.speed_limit


class PoliceCar(Car):
    pass

#Городская машина
print("\tГородская машина")
Town = TownCar(70,"городская машина","серая")
Town.show_speed()
Town.go()
Town.show_speed()
Town.show_speed()
Town.turn("налево")
Town.stop()
Town.show_speed()

print("")

#Спортивная машина
print("\tСпортивная машина")
Town = SportCar(150,"спортивная машина","красная")
Town.show_speed()
Town.go()
Town.show_speed()
Town.turn("направо")
Town.stop()
Town.show_speed()

print("")

#Рабочая машина
print("\tРабочая машина")
Town = WorkCar(80,"рабочая машина","желтая")
Town.show_speed()
Town.go()
Town.show_speed()
Town.show_speed()
Town.turn("налево")
Town.stop()
Town.show_speed()

print("")

#Полицейская машина
print("\tПолицейская машина")
Town = PoliceCar(90,"полицейская машина","синяя",True)
Town.show_speed()
Town.go()
Town.show_speed()
Town.turn("направо")
Town.turn("направо")
Town.turn("налево")
Town.stop()
Town.show_speed()


