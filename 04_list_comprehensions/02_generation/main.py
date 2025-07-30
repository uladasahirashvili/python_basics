n = int(input('Enter the length of the list: '))

user_list = [(1 if num % 2 == 0 else num % 5) for num in range(n)]

print('Result:', user_list)
