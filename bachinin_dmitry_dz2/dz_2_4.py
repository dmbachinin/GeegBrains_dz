start_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй',
              'директор аэлита']
for element in start_list:
    str_list = element.split(" ")
    print(f"Привет, {str_list[-1].capitalize()}!")
