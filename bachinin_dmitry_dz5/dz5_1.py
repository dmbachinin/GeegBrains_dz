def get_generator(len):
    for n in range(1, len + 1, 2):
        yield n


gen = get_generator(10)

print(gen)
print(*gen)
