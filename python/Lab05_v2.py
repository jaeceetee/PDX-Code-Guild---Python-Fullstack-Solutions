# Lab 05_v2 - Random Emoticon Generator - While loop to make 5 emoticons

import random

# Define a list of eyes, noses, mouths
eyes = [':', ';', 'X', '=', '8']
noses = ['-', '^', 'o', 'c', '']
mouths = ['|', '//', ')', '(', '[', ']', 'O', 'D', 'P']

# Loop to make 5 faces
counter = 0
while counter <5:

    # Randomly pick a set of eyes, a nose, and a mouth
    face = random.choice(eyes)
    face += random.choice(noses)
    face += random.choice(mouths)

    # Display emoticon
    print(face)
    counter += 1