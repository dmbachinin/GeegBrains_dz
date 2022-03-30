def thesaurus_adv(*name_list):

    ''' Функция сортировки имен и фамилий по ключам первых букв '''

    name_dict = {}
    for name in name_list:
        key_name = name[0].upper()
        key_surname = name.split(" ")[1][0]
        if key_surname in name_dict:
            if key_name in name_dict[key_surname]:
                name_dict[key_surname][key_name].append(name)
            else:
                name_dict[key_surname][key_name] = [name]
        else:
            name_dict[key_surname] = {key_name: [name]}
    for key, value in name_dict.items():
        print("{}: {}".format(key, value))


thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
