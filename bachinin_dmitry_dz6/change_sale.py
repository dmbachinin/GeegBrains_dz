import sys
import pandas
try:
    num = int(sys.argv[1])
    val = float(sys.argv[2].replace(",","."))
    change = pandas.read_csv("bakery.csv",sep=",")
    if num > len(change)-1:
        print("Такого значения нет в списке")
    else:
        change.loc[num,"sale"] = val
        change.to_csv("bakery.csv",index=False)
        print(change)
except ValueError:
    print("Введенные значения некорректны")
