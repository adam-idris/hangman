# Hangman
    Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

    This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

# Word List
    A predefined list of fruits are stored in the variable word_list. Using the random function, a random fruit is selected from the list. This will be the word that the user is trying to guess.

# Input
    The input function is used to ask the user to enter a single letter. An if statement is used to verify that the only one letter has been entered and that it is in the alphabet.

# Functions
    The check_guess function first changes the input to lowercase and then determines whether the user has entered a letter contained within the random word. If the letter is not in the word, the function prints a message to the user to try again. If the letter is in the word, the function prints a message telling the user that the letter is in the word.

    The ask_for_input function verifies that the user has input a single letter and continues to loop until the user inputs a valid letter. The check_guess function is nested within the ask_for_input function so that validation and verification of the input is performed.