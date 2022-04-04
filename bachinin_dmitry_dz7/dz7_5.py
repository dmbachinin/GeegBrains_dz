import os
address_list = [*os.walk("test_dz7_5")]
stat_dict = {}
for address in address_list:
    file_list = address[len(address)-1]
    if file_list:
        for file in file_list:
            file_address = os.path.join(address[0], file)
            file_size = os.stat(file_address).st_size
            key_file_index = int("1"+"0"*len(str(os.stat(file_address).st_size)))
            filename, file_extension = os.path.splitext(file)
            file_extension = file_extension[1:]
            if key_file_index in stat_dict:
                stat_dict[key_file_index][0] += 1
                stat_dict[key_file_index][1].append(file_extension)
            else:
                stat_dict[key_file_index] = [1,[file_extension]]

"Красивый вывод словаря"
sort_dict_key = sorted(stat_dict)
final_dict = {}
for key in sort_dict_key:
    final_dict[key] = (stat_dict[key][0],list(set(stat_dict[key][1])))
print(final_dict)