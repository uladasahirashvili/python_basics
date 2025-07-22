main_list = [1, 5, 3]
side_list_1 = [1, 5, 1, 5]
side_list_2 = [1, 3, 1, 5, 3, 3]

print("Program output:")
main_list.extend(side_list_1)

count_5 = main_list.count(5)
print("Number of 5s after first merge:", count_5)

while 5 in main_list:
    main_list.remove(5)

main_list.extend(side_list_2)

count_3 = main_list.count(3)
print("Number of 3s after second merge:", count_3)

print("Final list:", main_list)
