numbers_list = [8, 5, 6, 3, 9, 12, 44]

for i in range(len(numbers_list) - 1, -1, -1):
    if numbers_list[i] % 2 == 0:
        print(numbers_list[i], end=' ')
