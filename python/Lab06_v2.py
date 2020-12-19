# Lab 06 - Password Generator - User sets how long the the length of password is

import random
import string

# Password length = n
n = ""
while not n.isdigit():
    n = input("Enter the length of your desired password: ")

n = int(n)

# Generate random characters
password = ''
while len(password) < n:
    randomizer = random.choice(range(3))
    if randomizer == 0:
        password += random.choice(string.ascii_lowercase)
    elif randomizer == 1:
        password += random.choice(string.ascii_uppercase)
    elif randomizer == 2:
        password += random.choice(string.digits)

# Print password
print(password)