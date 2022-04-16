
class division_by_zero(Exception):

    def __str__(self):
        return "Попытка деления на 0"

try:
    k = int(input())
    if k == 0:
        raise division_by_zero
    else:
        res = 10/k
        print("Деление прошло успешно")
except division_by_zero:
    print("Вы попытались поделить на 0")

