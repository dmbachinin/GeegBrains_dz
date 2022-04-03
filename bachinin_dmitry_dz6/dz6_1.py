with open("dz6.txt", "r", encoding="utf-8") as f:
    result_list = []
    spam_dict = {}
    for line in f:
        remote_addr = line[:line.index("-")-1]
        request_type = line[line.index('"')+1:line.index(" /")]
        requested_resource_prob = line[line.index(" /")+1:line.index('" ')]
        requested_resource = requested_resource_prob[:requested_resource_prob.index(" ")]
        if remote_addr in spam_dict:
            spam_dict[remote_addr] += 1
        else:
            spam_dict[remote_addr] = 1
        result_list.append((remote_addr,request_type,requested_resource))

for element in result_list:
    print(element)
    break

val_spam = max(spam_dict.values())
for key,val in spam_dict.items():
    if val == val_spam:
        print(f"Спамер найден!\nЕго id: {key}\nКоличество запросов от этого пользователя: {val}")
        break
