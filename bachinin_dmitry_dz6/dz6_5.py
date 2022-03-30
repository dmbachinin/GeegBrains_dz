import sys
argv = sys.argv[1:]
if not(argv):
    user_file_name = input("Введите название файла с пользователями: ")
    hobby_file_name = input("Введите название файла с хобби: ")
    result_file_name = input("Введите имя результирующего файла: ")
    try:
        with open(user_file_name,"r") as u:
            with open(hobby_file_name,"r") as h:
                with open(result_file_name, "w",encoding="utf-8") as res:
                    for line_u in u:
                        line_u = line_u[:-1]
                        line_h = h.readline()[:-1]
                        res.write(f"{line_u}: {line_h if line_h else 'None'}\n")
        print(f"Файл {result_file_name} создан")
    except:
        print("Произошла ошибка:(")
elif len(argv) == 3:
    user_file_name = argv[0]
    hobby_file_name = argv[1]
    result_file_name = argv[2]
    try:
        with open(user_file_name, "r") as u:
            with open(hobby_file_name, "r") as h:
                with open(result_file_name, "w", encoding="utf-8") as res:
                    for line_u in u:
                        line_u = line_u[:-1]
                        line_h = h.readline()[:-1]
                        res.write(f"{line_u}: {line_h if line_h else 'None'}\n")
        print(f"Файл {result_file_name} создан")
    except:
        print("Произошла ошибка:(")
else:
    print("Входные данные некорректны")
