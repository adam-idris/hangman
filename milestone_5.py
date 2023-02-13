
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
        self.man = ''
        
    def hangman_picture(self, num_lives):

        if num_lives == 5:
            self.man = ''
            return self.man

        if num_lives == 4:
            self.man = '  +---+\n      |\n      |\n      |\n      |\n      |\n======='
            return self.man

        elif num_lives == 3:
            self.man = '  +---+\n      |\n  O   |\n      |\n      |\n      |\n======='
            return self.man

        elif num_lives == 2:
            self.man = '  +---+\n      |\n  O   |\n  |   |\n / \  |\n      |\n======='
            return self.man

        elif num_lives == 1:
            self.man = '  +---+\n      |\n  O   |\n /|\  |\n / \  |\n      |\n======='
            return self.man
            
        elif num_lives == 0:
            self.man = '  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n======='
            return self.man

    def check_guess(self, guess):
        self.guess = guess
        self.guess = self.guess.lower()
        if self.guess in self.word:
            print("Good guess! {} is in the word.".format(self.guess))
            for i in range(0, len(self.word)):
                if self.word[i] == self.guess:
                    self.word_guessed[i] = self.guess
            self.num_letters -= 1
            print("\n {}".format(self.word_guessed))
            print("\n")
            print(self.hangman_picture(self.num_lives))

        else:
            self.num_lives -= 1
            print("Sorry {} is not in the word.".format(self.guess))
            print("\n {}".format(self.word_guessed))
            print("\nYou have {} lives left".format(self.num_lives))
            print("\n")
            print(self.hangman_picture(self.num_lives))
            

        self.list_of_guesses.append(self.guess)
        print("Guessed letters: " + ", ".join(list(set(self.list_of_guesses))) + "\n")

            
    def ask_for_input(self):
        
        while True:
            guess = input("Please enter a single letter: ")
            
            if len(guess) != 1 or guess.isalpha() == False:
                print("Invalid letter. Please, enter a single alphabetical character.")
                
            
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break

def play_game(word_list):
    game = Hangman(word_list, num_lives=5)
    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print("Congratulations. You won the game!")
            break

fruits = ["apple", "banana", "peach", "orange", "mango"]

play_game(fruits)