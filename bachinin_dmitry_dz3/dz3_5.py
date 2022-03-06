from random import choice


def get_jokes(n, jokes_repeated="Y"):
    ''' Функция генерации n шуток из 3 слов '''

    jokes_repeated = jokes_repeated.upper()
    jokes_list = []
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    if jokes_repeated == "Y":
        for i in range(n):
            jokes_list.append(f"{(choice(nouns))} {(choice(adverbs))} {(choice(adjectives))}")  # Генерация шутки
        print(jokes_list)
    else:
        for i in range(n):
            try:
                nouns_word, adverbs_word, adjectives_word = choice(nouns), choice(adverbs), choice(adjectives)
            except IndexError:
                print("Шутки закончились :(")
                break
            else:
                del nouns[nouns.index(nouns_word)]
                del adverbs[adverbs.index(adverbs_word)]
                del adjectives[adjectives.index(adjectives_word)]
                jokes_list.append(f"{nouns_word} {adverbs_word} {adjectives_word}")  # Генерация шутки
        print(jokes_list)


get_jokes(int(input("Введите количество шуток: ")), input("Шутки могут использовать одинаковые слова? (Y/N): "))
