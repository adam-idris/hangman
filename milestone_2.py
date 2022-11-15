import random

# Create a list of five favourite fruits

word_list = ["apple", "banana", "peach", "orange", "mango"]
print(word_list)

# Print out a random fruit from the list

word = random.choice(word_list)
print(word)

# Assign the input to a variable

guess = input("Please enter a single letter: ")

# Check that the input is a single letter

if len(guess) == 1 and guess.isalpha() == True:
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")