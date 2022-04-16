# 1 способ реализации
class Number_list():
    def __init__(self,*args):
        self.list  = [num for num in args if type(num) == int or type(num) == float]
    def append(self,arg):
        self.list.append(arg)
    def __str__(self):
        return str(self.list)
    
# 2 способ реализации
class Record():
    def __init__(self):
        self.list = []
        user = ""
        while user.lower() != "stop":
            user = input("Введите число или 'stop', для прекращения работы: ")
            if user.lower() != "stop":
                if self.is_number(user):
                    self.list.append(float(user))
                else:
                    print("Вы ввели не число")
    def __str__(self):
        return str(self.list)
    @staticmethod
    def is_number(arg):
        try:
            res = float(arg)
        except ValueError: return False
        else: return True

n = Number_list(1,2,3,"4","56",1.4,12,2)
print(n)
res = Record()
print(res)





