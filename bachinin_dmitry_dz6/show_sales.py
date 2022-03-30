import csv
import sys
try:
    with open("bakery.csv","r",encoding="utf-8") as show:
        show_read = csv.reader(show)
        a = [*show_read][1:]
        if len(sys.argv) == 2:
            last = int(sys.argv[1])-1
            first = len(a)
        elif len(sys.argv) == 3:
            last = int(sys.argv[1])-1
            first = int(sys.argv[2])
        elif len(sys.argv) == 1:
            last = 0
            first = len(a)
        for num in range(last, first):
            print(a[num][0])
except IndexError:
    print("\nВы вышли за пределы списка значений")
except ValueError:
    print("Введенное значение промежутка не число")
except NameError:
    print("Введено слишком много значений")
