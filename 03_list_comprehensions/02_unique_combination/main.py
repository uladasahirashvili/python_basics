list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 5, 6, 8, 10]

i, j = 0, 0
while i < len(list1) and j < len(list2):
    if list1[i] < list2[j]:
        i += 1
    elif list1[i] > list2[j]:
        list1.insert(i, list2[j])
        i += 1
        j += 1
    else:
        i += 1
        j += 1

while j < len(list2):
    list1.append(list2[j])
    j += 1

print(list1)
