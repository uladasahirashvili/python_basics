shop = [
    ['bottom bracket', 60],
    ['crank arm', 50],
    ['saddle', 15],
    ['pedal', 5],
    ['saddle', 75],
    ['frame', 600],
    ['rim', 100],
    ['crank arm', 10],
    ['saddle', 135]
]

part_name = input('Part name: ').lower()
count = 0
total_price = 0

for detail, price in shop:
    if detail.lower() == part_name:
        count += 1
        total_price += price

if count > 0:
    print('\nNumber of parts:', count)
    print('Total cost:', total_price)
else:
    print('Part not found')
