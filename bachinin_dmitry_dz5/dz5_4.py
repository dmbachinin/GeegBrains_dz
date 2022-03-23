start_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [start_list[num] for num in range(1,len(start_list)) if start_list[num] > start_list[num-1]]
print(result)
