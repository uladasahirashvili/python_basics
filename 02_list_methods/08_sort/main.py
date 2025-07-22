numbers = [1, 4, -3, 0, 10]
length = len(numbers)

print('Original list:', numbers)

swapped = True
while swapped:
    swapped = False
    for i in range(1, length):
        if numbers[i] < numbers[i - 1]:
            numbers[i], numbers[i - 1] = numbers[i - 1], numbers[i]
            swapped = True

print('Sorted list:', numbers)

