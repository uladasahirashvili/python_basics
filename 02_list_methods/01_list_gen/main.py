n = int(input('Enter a number: '))
odd_numbers = []

for number in range(1, n + 1):
    if number % 2 == 1:
        odd_numbers.append(number)

print('List of odd numbers from 1 to N:', odd_numbers)
