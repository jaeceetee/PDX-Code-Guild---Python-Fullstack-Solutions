# Lab11_v2 - Make Change - Put conversion values in tuples

# Create the converstion tuple
coins = [
    ('half_dollar', 50),
    ('quarter', 25),
    ('dime', 10),
    ('nickel', 5),
    ('penny', 1)
]

# Welcome Message
print("Welcome to the Change Maker 5000 (tm)")

# Ask user for dollar amount
dollar_amount = input("Enter a dollar amount: ")

# Convert dollar amount to pennies
dollar_amount = dollar_amount.replace(".", "")
dollar_amount = int(dollar_amount)

# Calculations
change_list = {}

for coin in coins:
    change = dollar_amount // coin[1]
    dollar_amount = dollar_amount % coin[1]
    change_list[coin[0]] = change

result =''
# Build print string
for change in change_list:
    result += str(change_list[change]) + " " + change
    if change != 'penny':
        result += ', '


print(result)