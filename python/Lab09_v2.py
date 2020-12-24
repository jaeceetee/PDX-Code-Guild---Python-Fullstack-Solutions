# Lab09 - ROT Cipher - User sets N
import string

# User sets rotation
N = input("Enter number of rotations: ")
while N.isdigit() == False:
    N = input("Invalid entry. Enter number of rotations: ")
N = int(N)

# If number is greater than 26, bring it to usable number
if N > 26:
    N = N % 26

# Build cypher dictionary
cypher = {}
for letter in string.ascii_lowercase:
    if ord(letter) + N > 122:
        cypher[letter] = chr(ord(letter) - 26 + N)
    else:
        cypher[letter] = chr(ord(letter) + N)
    
# Get user string
user_input = ""
user_input_valid = False
while user_input_valid == False:
    user_input = input(f"What string would you like to encrypt in ROT{N}? ").lower()
    for char in user_input:
        if char not in string.ascii_lowercase:
            break
    else:
        user_input_valid = True

# Build new string
encrypted_string = ""
for char in user_input:
    encrypted_string += cypher.get(char)

# Print encrypted string
print(encrypted_string)

