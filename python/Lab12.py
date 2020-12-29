# Lab 12 - Blackjack Advice

import random

# Set Values for cards
cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]

# Select 3 random cards
picked_cards = []
total_value = 0
while len(picked_cards) < 3:
    current_pick = random.choice(cards)
    if current_pick == "A":
        total_value += 1
    elif current_pick == "J" or current_pick == "Q" or current_pick == "K":
        total_value += 10
    else:
        total_value += current_pick
    picked_cards.append(current_pick)

# Display cards
result = f"""What's your first card? {picked_cards[0]}
What's your second card? {picked_cards[1]}
What's your third card? {picked_cards[2]}
"""

# Generate advice
if total_value < 17:
    result += f"{total_value} Hit!"
elif total_value < 21:
    result += f"{total_value} Stay!"
elif total_value == 21:
    result += f"{total_value} Blackjack!"
else:
    result += f"{total_value} Already Busted!"


print(result)