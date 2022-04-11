
class Stationery:
    def __init__(self,title):
        self.title = title
    def draw(self):
        print(self.title)
        print("Запуск отрисовки")

class Pen(Stationery):
    def draw(self):
        print("Ручка пишет")

class Pencil(Stationery):
    def draw(self):
        print("Карандаш рисует")

class Handle(Stationery):
    def draw(self):
        print("Маркер подчеркивает")


stylus = Stationery("Перо")
stylus.draw()

print("")

pen = Pen("Ручка")
pen.draw()

print("")

pencil = Pencil("Карандаш")
pencil.draw()

print("")

handle = Handle("Маркер")
handle.draw()
