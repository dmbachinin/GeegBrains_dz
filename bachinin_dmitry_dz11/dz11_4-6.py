class Werahouse():
    profit = 0
    def __init__(self,*args):
        self.list = [name for name in args]


    def __str__(self):
        '''Вывод основной информации о складе'''
        return str([f"Название: '{name.__doc__}' количество: {name.quantity}" for name in self.list])

    def add(self,name):
        '''Регистрация товара'''
        print(f"Товар {name.__doc__} добавлен на склад")
        self.list.append(name)

    def remove(self,name):
        '''Удаление товара'''
        print(f"Товар {name.__doc__} удален со склада")
        del self.list[self.list.index(name)]

    def shipment(self,name,count):
        '''Продажа товара'''
        if not(name in self.list):
            self.add(name)
        dell = False
        product = self.list[self.list.index(name)].quantity
        if count > product:
            print(f"Вы продаете больше, чем есть на скале\nПродано: {product}")
            count = product
            dell = True
        product -= count
        self.profit += count * self.list[self.list.index(name)].price
        if dell:
            self.remove(name)
        else:
            self.list[self.list.index(name)].quantity = product

    def supply(self,name,count):
        '''Поступление товара на склад'''
        if name in self.list:
            self.list[self.list.index(name)].quantity += count
        else:
            self.add(name)
            self.list[self.list.index(name)].quantity += count

    def info(self):
        '''Вывод полной информации о складе'''
        return str([stat.__dict__ for stat in self.list])

    def profit_str(self):
        '''Прибыль'''
        return self.profit

class Тechic():
    def __init__(self,price, quantity,model, color):
        self.name = self.__doc__
        self.price = price
        self.quantity = quantity
        self.model = model
        self.color = color
    def __str__(self):
        return str(self.__dict__)

    def validation(self,*args):
        for i in args:
            if type(i) != int:
                return False
        else:
            if i > 0:
                return True
            else:
                return False

class Printer(Тechic):
    __doc__ = "Принтер"
    def __init__(self,price, quantity,model, color,lnk_price = 100):
        if not self.validation(price, quantity,lnk_price):
            print("Неверные входные данные")
        else:
            super().__init__(price, quantity, model, color)
            self.lnk_price = lnk_price

class Scanner(Тechic):
    __doc__ = "Сканер"
    def __init__(self,price, quantity,model, color,possible_paper = []):
        if not self.validation(price, quantity):
            print("Неверные входные данные")
        else:
            super().__init__(price, quantity, model, color)
            self.lnk_price = possible_paper
            self.possible_paper = possible_paper


class Xerox(Тechic):
    __doc__ = "Ксерокс"
    def __init__(self,price, quantity,model, color,weight = 3):
        if not self.validation(price, quantity, weight):
            print("Неверные входные данные")
        else:
            super().__init__(price, quantity, model, color)
            self.lnk_price = weight
            self.weight = weight

pr = Printer(12,500,"GR89","синий",100)
print(pr)
Scan = Scanner(300,100,"GM823","красный",["A4","A3"])
print(Scan)
xer = Xerox(300,100,"GM823","красный",5)
print(xer)
werahouse = Werahouse(Scan)
werahouse.add(xer)
werahouse.shipment(pr,1300)
werahouse.supply(xer,100)
print(werahouse)
print(werahouse.profit)




