# Hangman
    Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts. This is an implementation of the Hangman game, where the computer chooses a random word from a list and the user tries to guess it. 

    The Hangman game is written using object-oriented programming and loops.

## Initialised Attributes

    word: The word to be guessed, picked randomly from the word_list.

    word_guessed: A list of the letters of the word, with _ for each letter not yet guessed. For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']. If the player guesses 'a', the list would be ['a', '_', '_', '_', '_'].

    num_letters: The number of UNIQUE letters in the word that have not been guessed yet.

    num_lives: The number of lives the player has at the start of the game.

    word_list: A list of words the computer will randomly choose from.

    list_of_guesses: A list of the guesses that have already been tried.

    man: An empty string which is to be replaced with a picture of the hangman depending on how many lives have been lost.

## Methods

    hangman_picture: Takes in an argument of num_lives and returns a picture of the hangman that reflects the stage of the game. The code snippet shows the image when there are no lives left and the player has lost the game.

    ```python
        elif num_lives == 0:
        self.man = '  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n======='
        return self.man
    ```

    check_guess: Takes an argument of 'guess' which is the letter that has been guessed by the user. For consistency, the letter is always converted to lower case. If the letter guessed is in the word, the '_' in the word_guessed attribute is replaced with the corresponding letter using indexing and the num_letters attribute is decreased by one. A message is printed to show how many. However, in the instance of an incorrect guess, the num_lives attribute decreases by one and the picture of the hangman is printed.