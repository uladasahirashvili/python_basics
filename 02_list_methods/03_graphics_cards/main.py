card_count = int(input("Number of graphics cards: "))
card_models = []

# Input the model numbers
for i in range(1, card_count + 1):
    model = int(input(f"Card {i}: "))
    card_models.append(model)

# Find the highest model number
max_model = 0
for model in card_models:
    if model > max_model:
        max_model = model

# Create a new list without the highest model(s)
filtered_cards = []
for model in card_models:
    if model != max_model:
        filtered_cards.append(model)

print("Old list of graphics cards:", card_models)
print("New list of graphics cards:", filtered_cards)
