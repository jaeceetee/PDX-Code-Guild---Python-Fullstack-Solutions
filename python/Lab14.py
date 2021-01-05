# Lab 14 - Number to Phrase

# create dictionaries for reference
tens_phrase = {
    0: "",
    2: "twenty",
    3: "thirty",
    4: "forty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninety"
}

ones_phrase = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sisteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen"
}

# Ask user for number
user_input = ""
while user_input.isdigit() == False or len(user_input) > 2:
    user_input = input("Enter 2 digit number from 00 - 99: ")
user_input = int(user_input)

# Convert to phrase
ones_digit = user_input % 10
tens_digit = user_input // 10
result = ""

    # Under 20
if tens_digit == 0 or tens_digit == 1:
    result = ones_phrase[ones_digit]

    # 20 or over
else:
    result = tens_phrase[tens_digit] + "-" + ones_phrase[ones_digit]

# Display result
print(result)