import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        
    def word(self):
        self.word = random.choice(self.word_list)
        
    def word_guessed(self, letter_guessed):
        self.word_guessed = []
        for i in range(0, self.word):
            if self.word[i] == letter_guessed:
                self.word_guessed[i] = letter_guessed
            else:
                self.word_guessed[i] = ('_')
        
    
    def num_letters(self):
        pass
    
    def word_list(self):
        self.word_list = ["apple", "banana", "peach", "orange", "mango"]
    
    def list_of_guesses(self):
        self.list_of_guesses = []
        
    def check_guess(self, guess):
        self.guess = guess.lower()
        if self.guess in self.word:
            print("Good guess! {} is in the word.".format(guess))
            
    def ask_for_input(self):
        while True:
            guess = input("Please enter a single letter: ")
            
            if len(guess) != 1 and guess.isalpha() == False:
                print("Invalid letter. Please, enter a single alphabetical character.")
            
            elif guess in self.list_of_guesses == True:
                print("You already tried that letter!")
            
            else:
                self.list_of_guesses.append(self.check_guess(guess))
                