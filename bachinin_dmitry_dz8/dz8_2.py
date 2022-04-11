import re
import requests
parsed_dict = []
i = 1
res = requests.get("https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs")
for line in res.text.split("\n"):
    try:
        id = re.search("\d{1,3}[.]\d{1,3}[.]\d{1,3}[.]\d{1,3}", line).group()
        date = re.search("\d{2}[/]\D{1,10}[/]\d{4}[:]\d{2}[:]\d{2}[:]\d{2} [+-]\d{4}", line).group()
        move = re.search('["]\w{2,3}', line).group()[1:]
        add = re.search("[/]\w{1,}[/]\D{1,}\d", line).group()
        code, size = re.search(" \d{1,} \d{1,}", line).group()[1:].split(" ")
        parsed_dict.append((id,date,move,add,code,size))
    except AttributeError:
        pass
for stat in parsed_dict:
    print(stat)
    break



