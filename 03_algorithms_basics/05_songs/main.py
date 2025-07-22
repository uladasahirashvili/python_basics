violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.90],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

n = int(input('How many songs do you want to choose? '))

chosen_songs = []
total_time = 0

for i in range(1, n + 1):
    song_name = input('Name of song ' + str(i) + ': ')
    for song in violator_songs:
        if song[0] == song_name:
            chosen_songs.append(song)
            total_time += song[1]
            break
    else:
        print('Song "' + song_name + '" not found in the list.')

formatted_time = "{:.2f}".format(total_time)
print('Total playing time of chosen songs: ' + formatted_time + ' minutes')
