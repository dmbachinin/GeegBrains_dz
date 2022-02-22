
start_list = [i**3 for i in range(1,1000) if i%2 == 1]
a_sum = 0
b_sum = 0
for i in start_list:
    i_copy_for_a = i
    i_copy_for_b = i+17
    sum_i = 0
    while i_copy_for_a != 0:
        sum_i += i_copy_for_a % 10
        i_copy_for_a //= 10
    if sum_i%7 == 0:
        a_sum+=i
    sum_i = 0
    while i_copy_for_b != 0:
        sum_i += i_copy_for_b % 10
        i_copy_for_b //= 10

    if sum_i%7 == 0:
        b_sum+=i+17

print(f"Ответ в а: {a_sum}")
print(f"Ответ в b: {b_sum}")
