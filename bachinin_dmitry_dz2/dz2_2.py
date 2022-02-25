start_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(f"Начальное id списка {id(start_list)}")
for num, element in enumerate(start_list):
    try:
        el = int(element)

    except ValueError:
        print(element, end=" ")
        continue
    else:
        if len(element) <= 2:
            if "+" in element:
                element = "+0" + str(int(element))
            elif "-" in element:
                element = "-0" + str(-int(element))
            elif len(element) < 2:
                element = "0" + str(int(element))
        if start_list[num - 1] != '"':
            start_list.insert(num, '"')
            start_list.insert(num + 2, '"')
            print('"' + element, end="")

print("")
print(f"Конечное id списка {id(start_list)}")
