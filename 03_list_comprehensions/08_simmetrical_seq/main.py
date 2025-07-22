n = int(input('Number of numbers: '))
arr = []

for i in range(n):
    arr.append(int(input('Number: ')))

print('Sequence:', arr)

if arr == arr[::-1]:
    print('Numbers to add: 0')
else:
    copy_arr = arr.copy()
    count = 0
    while copy_arr != copy_arr[::-1]:
        count += 1
        copy_arr = arr.copy()
        for i in range(count):
            copy_arr.append(copy_arr[count - i - 1])

    print('Numbers to add:', count)
    print('The numbers themselves:', copy_arr[-count:])
