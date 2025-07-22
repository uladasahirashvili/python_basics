num_skates = int(input('Number of skates: '))
skate_sizes = []
for i in range(1, num_skates + 1):
    size = int(input('Size of skate pair ' + str(i) + ': '))
    skate_sizes.append(size)

num_people = int(input('\nNumber of people: '))
people_sizes = []
for i in range(1, num_people + 1):
    size = int(input('Foot size of person ' + str(i) + ': '))
    people_sizes.append(size)

max_people = 0

for skate in skate_sizes:
    for person in people_sizes:
        if skate == person:
            max_people += 1
            people_sizes.remove(person)
            break

print('Maximum number of people who can take skates:', max_people)
