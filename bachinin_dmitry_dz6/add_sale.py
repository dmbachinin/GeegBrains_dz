import csv
import sys
try:
    sale_sum = float(sys.argv[1].replace(",","."))
    with open("bakery.csv","a",encoding="utf-8") as f:
        f_write=csv.writer(f,delimiter=",",lineterminator="\n")
        f_write.writerow([sale_sum])
except ValueError:
    print("Значение введено некорректно")
except IndexError:
    print("Вы не ввели значение")
