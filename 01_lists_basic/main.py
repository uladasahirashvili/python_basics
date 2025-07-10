def sum_digits(number):
    total = 0
    while number > 0:
        total += number % 10
        number //= 10
    return total

def count_digits(number):
    count = 0
    while number > 0:
        count += 1
        number //= 10
    return count

num = int(input('Enter a positive integer: '))
print('\nSum of digits:', sum_digits(num))
print('Number of digits:', count_digits(num))
print('Difference between sum and count:', sum_digits(num) - count_digits(num))
