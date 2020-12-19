# Lab 06 - Password Generator

import random
import string

# Password length = n
n = 8

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
        
