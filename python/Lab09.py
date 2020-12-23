# Lab09 - ROT Cipher - ROT 13
import string


# Build cypher dictionary
cypher = {}
for letter in string.ascii_lowercase:
    if ord(letter) + 13 > 122:
        cypher[letter] = chr(ord(letter) - 13)
    else:
        cypher[letter] = chr(ord(letter) + 13)
    
# Get user string
user_input = ""
user_input_valid = False
while user_input_valid == False:
    user_input = input("What string would you like to encrypt in ROT 13? ").lower()
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
