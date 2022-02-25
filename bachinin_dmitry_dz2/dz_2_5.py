from random import randint

start_list = [randint(100, 10000) / 100 for i in range(randint(10, 20))]
start_id_list = id(start_list)
yes_rat = False
print(f"Начальный список цен:\n{start_list}, {len(start_list)} - длина списка")
print("Ответ на A:")
for element in start_list:
    print(f"{int(element)} руб {(str(round(element % 1, 2)) + '0').split('.')[1][:2]} коп", end=", ")
else:
    print("")
print("")
print("Ответ на B:")
start_list.sort()
for element in start_list:
    print(f"{int(element)} руб {(str(round(element % 1, 2)) + '0').split('.')[1][:2]} коп", end=", ")
else:
    print("")
print(f"Конечное id списка {id(start_list)} || {start_id_list} - начальное id списка ")
print("")
print("Ответ на C:")
start_list.reverse()
new_list = start_list.copy()
print(f"id нового списка {id(new_list)}")
print(f"Начальный список цен:\n{new_list}, {len(new_list)} - длина списка")
print("")
print("Ответ на D:")
for element in new_list[:5]:
    print(f"{int(element)} руб {(str(round(element % 1, 2)) + '0').split('.')[1][:2]} коп", end=", ")
