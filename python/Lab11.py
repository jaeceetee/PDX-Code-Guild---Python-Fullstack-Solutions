# Lab11 - Make Change

# Welcome Message
print("Welcome to the Change Maker 5000 (tm)")

# Ask user for dollar amount
dollar_amount = input("Enter a dollar amount: ")

# Convert dollar amount to pennies
dollar_amount = dollar_amount.replace(".", "")
dollar_amount = int(dollar_amount)

# Calculations
num_quarters = dollar_amount // 25
dollar_amount = dollar_amount % 25

num_dimes = dollar_amount // 10
dollar_amount = dollar_amount % 10

num_nickel = dollar_amount // 5
dollar_amount = dollar_amount % 5

num_pennies = dollar_amount

# Print result
print(f"""
    {num_quarters} quarters, 
    {num_dimes} dimes, 
    {num_nickel} nickels, 
    {num_pennies} pennies.
""".replace("\n", ""))
