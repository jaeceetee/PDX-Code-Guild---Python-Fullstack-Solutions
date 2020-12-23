# Lab 06 - Password Generator - User sets how many lower, upper letters, numbers, and spec char

import string
import random

# Ask user how many of each they would like
num_lower_letters = ""
num_upper_letters = ""
num_numbers = ""
num_spec_char = ""

while not num_lower_letters.isdigit():
    num_lower_letters = input("Enter number of lower case letters in your desired password: ")
num_lower_letters = int(num_lower_letters)
while not num_upper_letters.isdigit():
    num_upper_letters = input("Enter number of upper case letters in your desired password: ")     
num_upper_letters = int(num_upper_letters)
while not num_numbers.isdigit():
    num_numbers = input("Enter number of numbers in your desired password: ")
num_numbers = int(num_numbers)
while not num_spec_char.isdigit():
    num_spec_char = input("Enter number of special characters in your desired password: ")
num_spec_char = int(num_spec_char)

# Radomly pick requested number of chars
password = ""
while len(password) < num_lower_letters:
    password += random.choice(string.ascii_uppercase)
while len(password) < num_lower_letters + num_upper_letters:
    password += random.choice(string.ascii_lowercase)
while len(password) < num_lower_letters + num_upper_letters + num_numbers:
    password += random.choice(string.digits)
while len(password) < num_lower_letters + num_upper_letters + num_numbers + num_spec_char:
    password += random.choice(string.punctuation)

# Randomize the order
#password_list = password.split('')
password_list = list(password) 
random.shuffle(password_list)
password = ''.join(password_list)

# Display the password
print(password)