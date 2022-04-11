import re
add_parse = {}
def email_parse(add):
    try:
        add_parse["username"] = re.search(".{1,}@", add).group()[:-1]
        add_parse["domain"] = re.search("@\w{1,}[.]\w{1,}", add).group()[1:]
        print(add_parse["domain"])
    except AttributeError:
        raise ValueError
email_parse("someone@geekbrains.ru")
print(add_parse)
