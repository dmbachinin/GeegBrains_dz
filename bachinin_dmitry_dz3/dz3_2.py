def num_translate_adv(number=None):

    '''Функция перевода чисел от 1 до 10 на русский или английский языки'''

    translate_number_en = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
    translate_number_ru = ["один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять", "десять"]
    if number.lower() in translate_number_en:
        translat_language = "русский"
        correct_tran = 1
    else:
        translat_language = "английский"
        correct_tran = 0
    for i in zip(translate_number_en, translate_number_ru):
        if number.lower() in i:
            if number.istitle():
                print(f"Перевод на {translat_language}: {i[correct_tran].capitalize()}")
            else:
                print(f"Перевод на {translat_language}: {i[correct_tran]}")
            break


num_translate_adv(input("Введите слово для перевода: "))
