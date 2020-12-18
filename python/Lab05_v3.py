# Lab 05_v3 - Random Emoticon Generator - make vertical emoticons

import random

# Define a list of face, eyes, and mouth
faces = [['(',')'], ['[', ']'], ['<(',')>'], ['_(',')_']]
eyes = ['O', '^', '~', '.', 'T']
mouth = ['_', '.', '-', 'O']

# Randomly pic face, eyes, and mouth
face = random.choice(faces)
eye = random.choice(eyes)
head = face[0] + eye + random.choice(mouth) + eye + face[1]

# Display face
print(head)