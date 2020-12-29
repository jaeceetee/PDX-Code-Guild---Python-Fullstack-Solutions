# Lab11 - Make Change

# Welcome Message
print("Welcome to the Change Maker 5000 (tm)")
dollar_amount = ""
# Ask user for dollar amount
valid_entry = False
while valid_entry == False:
    dollar_amount = input("Enter a dollar amount: ")
    try:
        dollar_amount = float(dollar_amount)
        valid_entry = True
    except:
        pass


# Convert dollar amount to pennies
dollar_amount *= 100
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
