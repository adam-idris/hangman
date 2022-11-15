import random

# Create a list of five favourite fruits

word_list = ["apple", "banana", "peach", "orange", "mango"]

# Print out a random fruit from the list

word = random.choice(word_list)

# Check whether the guess is in the word
    
def check_guess(guess): 
    
    guess = guess.lower()
    if guess in word:
        print("Good guess! {} is in the word.".format(guess))  
    else:
        print("Sorry, {} is not in the word. Try again.".format(guess))
    
    
def ask_for_input():
    
    while True:
        guess = input("Please enter a single letter: ")
    
        if len(guess) == 1 and guess.isalpha() == True:
            break

        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
        
    check_guess(guess)

ask_for_input()
