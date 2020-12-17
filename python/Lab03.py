# Lab 03 - Grading - Convert number grade to letter grade

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

# Display letter grade
print(f"You got a/an {letter_grade} for your score of {num_grade}")