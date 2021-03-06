# Lab 14 - Number to Phrase - Handle numbers from 100-999
import random
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


def num_to_phrase(user_input):

# Convert to phrase
    hunds_digit = user_input // 100
    tens_digit = user_input % 100 // 10
    ones_digit = user_input % 10
    result = ""

        # Over 99
    if hunds_digit > 0:
        result = ones_phrase[hunds_digit] + " hundred "
        if tens_digit == 0 and ones_digit == 0:
            pass
        else:
            result += "and "

        # Under 20
    if tens_digit == 0 and ones_digit == 0:
        pass
    elif tens_digit < 2:
        under_twenty = 0
        if tens_digit == 1:
            under_twenty += 10
        under_twenty += ones_digit
        result += ones_phrase[under_twenty]


        # 20 or over
    else:
        result += tens_phrase[tens_digit]
        if ones_digit != 0:
            result += "-" + ones_phrase[ones_digit]

    # Display result
    return result

# Ask user for number
user_input = ""
while user_input.isdigit() == False or len(user_input) > 3:
    user_input = input("Enter up to 3 digit number from 0 - 999: ")
user_input = int(user_input)

print(num_to_phrase(user_input))
