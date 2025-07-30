text = input('Enter your text: ')
vowels_list = ['a', 'e', 'i', 'o', 'u']  # 'y' is not considered a vowel here

vowels = [letter for letter in text if letter.lower() in vowels_list]
print('List of vowels:', vowels)
print('Number of vowels:', len(vowels))