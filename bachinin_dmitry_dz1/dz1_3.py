for num in range(1, 101):
    percent = "процент"
    if str(num)[-1] == "1":
        if num == 11:
            percent += "ов"
    elif str(num)[-1] == "2":
        if num == 12:
            percent += "ов"
        else:
            percent += "а"
    elif str(num)[-1] == "3":
        if num == 13:
            percent += "ов"
        else:
            percent += "а"
    elif str(num)[-1] == "4":
        if num == 14:
            percent += "ов"
        else:
            percent += "а"
    else:
        percent += "ов"
    print(num, percent)
