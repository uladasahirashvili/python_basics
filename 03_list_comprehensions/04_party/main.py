guests = ['Peter', 'Ivan', 'Alex', 'Lisa', 'Kate']
max_guests = 6

print("There are", len(guests), "people at the party right now:", guests)

while True:
    action = input('\nDid a guest arrive or leave? (arrived/left/Time to sleep): ').lower()

    if action == 'time to sleep':
        print("The party's over, everyone went to bed.")
        break

    name = input("Guest's name: ")

    if len(guests) >= max_guests and action == 'arrived':
        print("Sorry,", name + ", but there's no room.")
        continue

    if action == 'arrived':
        guests.append(name)
        print("Hey,", name + "!")
    elif action == 'left':
        if name in guests:
            guests.remove(name)
            print("Bye,", name + "!")
        else:
            print(name, "wasn't at the party.")

    print("There are", len(guests), "people at the party right now:", guests)
