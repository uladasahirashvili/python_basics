N = int(input('Number of people: '))
K = int(input('Count to which number? '))

circle = list(range(1, N + 1))
index = 0
cycle_count = 1

while len(circle) > 1:
    print('\nCycle', cycle_count, ':')
    print('Current circle of people:', circle)
    print('Starting count from number', circle[index % len(circle)])
    index = (index + K - 1) % len(circle)
    removed_person = circle.pop(index)
    print('Person number', removed_person, 'is out')
    cycle_count += 1

last_person = circle[0]
print('\nThe last remaining person is number', last_person)
