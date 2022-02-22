duration = int(input("Введите количество секунд: "))
day = duration // 86400 # Находим количество дней
duration = duration % 86400
hours = duration // 3600 # Находим количество часов
duration = duration % 3600
minutes = duration // 60 # Находим количество минут
second = duration % 60 # Находим количество секунд
result = [day,"дн",hours,"час",minutes,"мин",second,"сек"]
for i in range(0,len(result),2):
    if result[i] != 0:
        print(str(result[i])+f" {result[i+1]}",end=" ")
