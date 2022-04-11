import os

with open("config.yaml", "r", encoding="utf-8") as config:
    for line in config:
        line = line.replace("\n", "")
        if line and not (line.startswith("//")):
            address = os.path.split(line)
            os.makedirs(rf"{address[0]}", exist_ok=True)
            with open(f"{address[0]}\\{address[1]}", "w", encoding="utf-8"):
                pass