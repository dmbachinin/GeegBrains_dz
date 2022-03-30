import json
result_dict = {}
with open("users.csv","r") as u:
    with open("hobby.csv","r") as h:
        with open("users_hobby.txt", "w",encoding="utf-8") as res:
            for line_u in u:
                line_u = line_u[:-1]
                line_h = h.readline()[:-1]
                res.write(f"{line_u}: {line_h if line_h else 'None'}\n")
                result_dict[line_u.replace(","," ")] = line_h if line_h else None

"сохранение словаря в файл"
with open("result_dict.txt","w",encoding="utf-8") as dict:
    json.dump(result_dict,dict)

"получение словаря из файла"
with open("result_dict.txt","r",encoding="utf-8") as dict:
    load_dict = json.load(dict)
    print(load_dict, type(load_dict))

if not(None in result_dict.values()):
    exit(1)