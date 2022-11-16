#%% Instructions

# Step 1. Create a class called Hangman. [X]

# Step 2. Inside the class, create an __init__ method to initialise the attributes of the class. Pass in word_list and num_lives as parameters. 
#         Make num_lives a default parameter and set the value to 5. [x]

# Step 3. Initialise the following attributes:

# word: The word to be guessed, picked randomly from the word_list. Remember to import the random module into your script.

# word_guessed: list - A list of the letters of the word, with _ for each letter not yet guessed. 
#               For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']. 
#               If the player guesses 'a', the list would be ['a', '_', '_', '_', '_'].

# num_letters: int - The number of UNIQUE letters in the word that have not been guessed yet.

# num_lives: int - The number of lives the player has at the start of the game.

# word_list: list - A list of words.

# list_of_guesses: list - A list of the guesses that have already been tried. Set this to an empty list initially.


#%%

import random

class Hangman():
    def __init__(self, word_list, num_lives=5):
        pass
        
    def word(self):
        pass
        
    def word_guessed(self):
        pass
    
    def num_letters(self):
        pass
    
    def word_list(self):
        pass
    
    def list_of_guesses(self):
        pass
            
        