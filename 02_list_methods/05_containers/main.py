containers = int(input('Number of containers: '))
containers_list = []
position = 1

for _ in range(containers):
    cont_weight = int(input('Enter container weight: '))
    if cont_weight > 200:
        print('Error: container weight must not exceed 200 kg')
    else:
        containers_list.append(cont_weight)

new_cont_weight = int(input('\nEnter the new container weight: '))

if new_cont_weight > 200:
    print('Error: container weight must not exceed 200 kg')

for mass in containers_list:
    if mass <= new_cont_weight:
        break
    position += 1

print('The new container will be placed at position:', position)
