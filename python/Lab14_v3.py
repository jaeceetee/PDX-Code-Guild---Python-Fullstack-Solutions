# Lab 14 - Number to Phrase - Handle numbers from 100-999
import random 

def get_roman(digit, ref_dict):
    if digit in ref_dict:
        return ref_dict[digit]
    elif digit < 4:
        return ref_dict[1] * digit
    else:
        return ref_dict[5] + (ref_dict[1] * (digit - 5))

# create dictionaries for reference
roman_ones = {
    1: "I",
    4: "IV",
    5: "V",
    9: "IX"
}

roman_tens = {
    1: "X",
    4: "XL",
    5: "L",
    9: "XC"
}

roman_hunds = {
    1: "C",
    4: "CD",
    5: "D",
    9: "CM"
}

# Get user number
#user_num = ""
#while len(user_num) > 3 or user_num.isdigit() == False:
#    user_num = input("Enter a number from 0 - 999 for conversion: ")
#user_num = int(user_num)
user_num = random.randint(0, 999)

# Separate digits
hunds_digit = user_num // 100
tens_digit = user_num % 100 // 10
ones_digit = user_num % 10

# Get roman numerals
# Hundreds
result = get_roman(hunds_digit, roman_hunds)

# Tens
result += get_roman(tens_digit, roman_tens)

# Ones
result += get_roman(ones_digit, roman_ones)

# Print result
print(user_num)
print(result)