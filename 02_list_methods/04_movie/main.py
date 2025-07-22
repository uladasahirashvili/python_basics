films = ['Die Hard', 'Back to the Future', 'Taxi Driver',
         'Léon', 'Bohemian Rhapsody', 'Sin City',
         'Memento', 'The Departed', 'The Village']

film_amount = int(input('How many films would you like to add? '))
fav_list = []

for _ in range(film_amount):
    your_film = input('Enter the film name: ')
    if your_film in films:
        fav_list.append(your_film)
    else:
        print('Error: the film', your_film, 'is not in our database :(')

print('Your favorite films:', ', '.join(fav_list))
