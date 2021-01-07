# Lab 15 - Count Words

import requests
import string

special_char = string.punctuation

# Functions
def get_book():
    response = requests.get("http://www.gutenberg.org/files/46/46-0.txt")
    response.encoding = 'utf-8'

    return response.text

# Get the book
book = get_book()

# Modify string - remove unwanted characters
    # Strip header and footer
index = book.find("Produced by Jose Menendez")
book = book[index::]
index = book.find("End of the Project Gutenberg EBook of A Christmas Carol, by Charles Dickens")
book = book[:index:]

book = book.lower() # all lowercase

    # Remove punctuation, new lines, etc
for char in special_char:
    book = book.replace(char, " ")
book = book.replace("\n", " ")
book = book.replace("\r", " ")

    # Remove extra spaces
while '  ' in book:
    book = book.replace("  ", " ")

# Split by space
words = book.split(" ")

# Count each new word into dictionary
word_count = {}
for word in words:
    if word not in word_count:
        word_count[word] = 1
    else:
        word_count[word] += 1

# Sort
# word_count is a dictionary where the key is the word and the value is the count
word_items = list(word_count.items()) # .items() returns a list of tuples
word_items.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(word_items))):  # print the top 10 words, or all of them, whichever is smaller
    print(word_items[i])
