import re
class Сomplex_number():
    def __init__(self,number):
        number = number.replace(" ","")
        try:
            self.valid = int(re.match("\d+[+-]+",number).group()[:-1])
            self.novalid = int(re.search("[+-]\d+", number).group())
        except AttributeError:
            print("Введенное число некорректно")
    def __add__(self, other):
        res = self.novalid + other.novalid
        return f"{self.valid + other.valid}" if res == 0 else f"{self.valid + other.valid}{'+' if res>0 else ''}{res}i"
    def __mul__(self, other):
        res = self.valid*other.novalid + self.novalid*other.valid
        return f"{self.valid*other.valid - self.novalid*other.novalid}" if res == 0 else f"{self.valid*other.valid - self.novalid*other.novalid}{'+' if res>0 else ''}{res}i"

a = Сomplex_number("12+44i")
b = Сomplex_number("15-3i")
c = Сomplex_number("1sd2-3i")
print(f"Сумма: {a+b}")
print(f"Произведение: {a*b}")