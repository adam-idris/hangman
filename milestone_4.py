#%%
import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        
    def word(self):
        self.chosen_word = random.choice(self.word_list)
        print(self.chosen_word)

    def word_guessed(self, letter_guessed):
        self.letter_guessed = letter_guessed
        self.letter_list = []
        for i in range(0, len(self.chosen_word)):
            self.letter_list.append('_')
            if self.chosen_word[i] == self.letter_guessed:
                self.letter_list[i] = self.letter_guessed
            else:
                self.letter_list[i] = ('_')
        print(self.letter_list)
      
    def num_letters(self):

        self.unique_letters_list = list(set(self.chosen_word))
        self.unique_letters_left = len(self.unique_letters_list)

        for i in range(self.unique_letters_left):
            if self.unique_letters_list[i] in self.letter_list:
                self.unique_letters_left -= 1
        return self.unique_letters_left
    
    def word_list(self):
        self.list_used = ["apple", "banana", "peach", "orange", "mango"]
    
    def list_of_guesses(self):
        self.guess_list = []
      
    def check_guess(self, guess):
        self.guess = guess
        self.guess = guess.lower()
        if self.guess in self.chosen_word:
            print("Good guess! {} is in the word.".format(self.guess))
            
    def ask_for_input(self):
        while True:
            guess = input("Please enter a single letter: ")
            
            if len(guess) != 1 and guess.isalpha() == False:
                print("Invalid letter. Please, enter a single alphabetical character.")
            
            elif guess in self.guess_list == True:
                print("You already tried that letter!")
            
            else:
                self.guess_list.append(self.check_guess(guess))

#%%
        #     for i in range(0, len(self.chosen_word)):
        #         if self.chosen_word[i] == guess:
        #             self.letter_guessed[i] = guess
        #     self.num_letters -= 1
        # else: 
        #     self.num_lives -= 1
        #     print("Sorry, {} is not in the word".format(self.guess))
        #     print("You have {} lives left.".format(self.num_lives))
        # self.list_of_guesses.append(guess)