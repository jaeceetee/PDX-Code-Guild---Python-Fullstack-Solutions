# Lab 03_v2 - Grading - Convert number grade to letter grade with + or -

# Get grade from user
num_grade = int(input("What is the numeric grade? [0-100]: "))
letter_grade = ''

# Get letter grade
if num_grade >= 90:
    letter_grade = "A"
elif num_grade >= 80:
    letter_grade = "B"
elif num_grade >= 70:
    letter_grade = "C"
elif num_grade >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

# Add + or -
if num_grade == 100:        # 100 is +
    letter_grade += "+"
elif num_grade < 60:        # ignore if mid range
    pass
elif num_grade % 10 > 7:    # 8 and 9  gets +
    letter_grade += "+"
elif num_grade % 10 < 3:    # 0, 1, and 2 gets -
    letter_grade += "-"

# Display letter grade
print(f"You got a/an {letter_grade} for your score of {num_grade}")