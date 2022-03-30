def get_generator(len):
    gen = (num for num in range(1,len+1,2))
    return gen

gen = get_generator(101)

print(gen)
print(*gen)
