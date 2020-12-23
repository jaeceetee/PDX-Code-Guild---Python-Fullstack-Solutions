# Lab09_v3 - ROT Cipher - User sets N - Includes upper, lower, numbers, and spec chars
import string

accpectable_characters = string.ascii_letters + string.digits + string.punctuation + " "
print(accpectable_characters)
# User sets rotation
N = input("Enter number of rotations: ")
while N.isdigit() == False:
    N = input("Invalid entry. Enter number of rotations: ")
N = int(N)

# If number is greater than 26, bring it to usable number
if N > 95:
    N = N % 95

# Build cypher dictionary
cypher = {}
for char in accpectable_characters:
    if ord(char) + N > 126:
        cypher[char] = chr(ord(char) - 95 + N)
    else:
        cypher[char] = chr(ord(char) + N)
    
# Get user string
user_input = ""
user_input_valid = False
while user_input_valid == False:
    user_input = input(f"What string would you like to encrypt in ROT {N}? ").lower()
    for char in user_input:
        if char not in accpectable_characters:
            break
    else:
        user_input_valid = True

# Build new string
encrypted_string = ""
for char in user_input:
    encrypted_string += cypher.get(char)

# Print encrypted string
print(encrypted_string)
# print(cypher)
