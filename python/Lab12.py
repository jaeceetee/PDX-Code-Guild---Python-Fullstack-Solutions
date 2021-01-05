# Lab 12 - Blackjack Advice

# Set Values for cards
cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]

# Ask user for cards
picked_cards = []
total_value = 0
while len(picked_cards) < 3:
    if len(picked_cards) == 0:
        card_seq = "first"
    elif len(picked_cards) == 1:
        card_seq = "second"
    else:
        card_seq = "third"
    current_pick = ""
    while current_pick not in cards:
        current_pick = input(f"What's your {card_seq} card? (2-10, A, J, Q, K) ").upper()
        if current_pick.isdigit() == True:
            current_pick = int(current_pick)
    
    if current_pick == "A":
        total_value += 1
    elif current_pick == "J" or current_pick == "Q" or current_pick == "K":
        total_value += 10
    else:
        total_value += current_pick
    picked_cards.append(current_pick)

# Generate advice
if total_value < 17:
    result = f"{total_value} Hit!"
elif total_value < 21:
    result = f"{total_value} Stay!"
elif total_value == 21:
    result = f"{total_value} Blackjack!"
else:
    result = f"{total_value} Already Busted!"


print(result)