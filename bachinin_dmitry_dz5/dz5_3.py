tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

gen_klass = ((tutors[num], klasses[num] if num < len(klasses) else None) for num in range(len(tutors)))

print(gen_klass)
print(*gen_klass)

try:
    print(next(gen_klass))
except StopIteration:
    print("Генератор истощен")
