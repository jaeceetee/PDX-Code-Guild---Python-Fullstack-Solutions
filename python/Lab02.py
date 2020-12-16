#Lab 02 - MadLibs
#Ask user for various words for a mad lib

#Get user input to variables
adj1 = input("Enter an adjective: ")
adj2 = input("Enter another adjective: ")
adj3 = input("Enter another adjective: ")
adj4 = input("Enter another adjective: ")

noun1 = input("Enter a noun: ")
noun2 = input("Enter another noun: ")
noun3 = input("Enter another noun: ")

verb1 = input("Enter a verb: ")

pverb1 = input("Enter a past tense of a verb: ")
pverb2 = input("Enter another past tense of a verb: ")

adverb1 = input("Enter an adverb: ")
adverb2 = input("Enter another adverb: ")

#Enter variables into madlib
madlib = f"Today I went to the zoo. I saw a(n) {adj1} {noun1} jumping up and down in its tree. "
madlib += f"He {pverb1} {adverb1} through the large tunnel that led to its {adj2} {noun2}. "
madlib += f"I got some peanuts and passed them through the cage to a gigantic gray {noun3} towering above my head. "
madlib += f"Feeding that animal made me hungry. I went to get a {adj3} scoop of ice cream. "
madlib += f"It filled my stomach. Afterwards I had to {verb1} {adverb2} to catch our bus. When I got home I {pverb2} my mom for a(n) {adj4} day at the zoo. "

#Print result to user
print(madlib)