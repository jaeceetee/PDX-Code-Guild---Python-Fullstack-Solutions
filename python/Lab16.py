# Lab 16 - Compute Automated Readability Index

import requests
import string

special_char = string.punctuation

# Required items
num_words = 0
num_char = 0
num_sent = 0
title = ""

ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}

# Functions
def get_book():
    response = requests.get("http://www.gutenberg.org/files/1952/1952-0.txt")
    response.encoding = 'utf-8'

    return response.text

def get_title(content):
    title_begins = content.find("Title: ") + 7
    author_begins = content.find("Author: ")

    rough_title = content[title_begins:author_begins:]

    rough_title = rough_title.replace("\n", "")
    rough_title = rough_title.replace("\r", "")
    while '  ' in rough_title:
        rough_title = rough_title.replace("  ", " ")
    rough_title = rough_title.lstrip()
    
    return rough_title

def strip_header_footer(content):
    content = content.lower()
    start_line = content.find("start of this project gutenberg")
    end_of_line = content[start_line::].find("***") + 3
    begin = start_line + end_of_line
    end = content.find("End of the Project Gutenberg")

    return content[begin:end:]

def count_setence(content):
    counter = 0
    for char in content:
        if char == "!" or char == "?" or char == ".":
            counter += 1

    return counter

# Get the book
book = get_book()

# Get title
title = get_title(book)

# Strip header and footer
book = strip_header_footer(book)

# Remove new lines and "\r" in the book
book = book.replace("\n", " ")
book = book.replace("\r", " ")

# Get Sentence count
num_sent = count_setence(book)

# Replace all special characters
for char in special_char:
    book = book.replace(char, " ")

# Remove extra spaces
while '  ' in book:
    book = book.replace("  ", " ")

# Split by space to get word count
words = book.split(" ")
num_words = len(words)

# Purge spaces and count characters
book = book.replace(" ", "")
num_char = len(book)

# Calculate ARI
ari = (4.71 * (num_char/num_words)) + (.5 * (num_words/num_sent)) - 21.43
ari = round(ari)
if ari > 14:
    ari = 14

# craft output
print("-" * 56)
print(f"The ARI for {title} is {ari}")
print(f"This corresponds to a {ari_scale[ari]['grade_level']} level of difficulty")
print(f"that is suitable for an average person {ari_scale[ari]['ages']} years old.")
print("-" * 56)