def find_smallest_divisor(n):
    for divisor in range(2, n + 1):
        if n % divisor == 0:
            print('The smallest divisor greater than 1 is:', divisor)
            break


number = int(input('Enter a natural number greater than 1: '))
find_smallest_divisor(number)
