lst = [1, 2, 3, 4, 5]
k = int(input('Shift: '))

# Cyclically shift the list to the right by k positions
new_lst = lst[-k % len(lst):] + lst[:-k % len(lst)]

print('Original list:', lst)
print('Shifted list:', new_lst)
