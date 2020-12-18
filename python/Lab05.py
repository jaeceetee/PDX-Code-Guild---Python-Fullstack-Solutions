# Lab 05 - Random Emoticon Generator

import random

# Define a list of eyes, noses, mouths
eyes = [':', ';', 'X', '=', '8']
noses = ['-', '^', 'o', 'c', '']
mouths = ['|', '//', ')', '(', '[', ']', 'O', 'D', 'P']

# Randomly pick a set of eyes, a nose, and a mouth
face = random.choice(eyes)
face += random.choice(noses)
face += random.choice(mouths)

# Display emoticon
print(face)