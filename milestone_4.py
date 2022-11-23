#%%
import random

class Hangman:

    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_' for char in self.word]
        self.num_letters = len(list(set(self.word)))
        self.num_lives = num_lives
        self.list_of_guesses = []
        
      
    def check_guess(self, guess):
        self.guess = guess.lower()
        if self.guess in self.word:
            print("Good guess! {} is in the word.".format(self.guess))
            
    def ask_for_input(self):
        while True:
            guess = input("Please enter a single letter: ")
            
            if len(guess) != 1 and guess.isalpha() == False:
                print("Invalid letter. Please, enter a single alphabetical character.")
            
            elif guess in self.list_of_guesses == True:
                print("You already tried that letter!")
            
            else:
                self.list_of_guesses.append(self.check_guess(guess))
                
fruits = ["apple", "banana", "peach", "orange", "mango"]
game = Hangman(fruits, num_lives=5)
game.ask_for_input()

