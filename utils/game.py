import random

class Hangman:

    """
    A Hangman game class that allows a player to guess a word letter by letter.
    
    Attributes:
    -----------
    possible_words : list
        A list of possible words to be guessed.
    word_to_find : list
        The word chosen to be guessed, represented as a list of letters.
    lives : int
        The number of lives the player has, starting at 5.
    correctly_guessed_letters : list
        A list representing the correctly guessed letters in the word, initialized with underscores.
    wrongly_guessed_letters : list
        A list of letters that were guessed incorrectly.
    turn_count : int
        The number of turns taken by the player.
    error_count : int
        The number of incorrect guesses made by the player.
    """        
    def __init__(self):
        """
        Initializes the Hangman game with a list of possible words, 
        chooses a random word to guess, and sets initial game parameters.
        """
        self.possible_words = ['becode', 'learning', 'mathematics', 'sessions']
        self.word_to_find = list(random.choice(self.possible_words))
        self.lives = 5
        self.correctly_guessed_letters = ["_"] * len(self.word_to_find)
        self.wrongly_guessed_letters = [] 
        self.turn_count = 0 
        self.error_count = 0


    def play(self):
        """
        Asks the player to enter a letter and checks if it is in the word to guess.
        Updates the game state based on whether the guess is correct or not.
        """
        guessed_letter = input("Enter a letter: ") ###then create try except
        self.turn_count += 1
        if guessed_letter in list(self.word_to_find):
            for letter in range(len(self.word_to_find)):
                if self.word_to_find[letter] == guessed_letter:
                    self.correctly_guessed_letters[letter] = guessed_letter
            print(self.correctly_guessed_letters)
            
        else:
            self.wrongly_guessed_letters.append(guessed_letter)
            self.error_count += 1
            self.lives -= 1
        
        print(self.correctly_guessed_letters)

    def game_over(self):
        """
        Checks if the game is over (player has no lives left).
        Prints a game over message and returns False.
        """
        if self.lives == 0:
            print("|}|GAME OVER|{|")
            return False
        
    def well_played(self):
        """
        Checks if the player has correctly guessed all the letters in the word.
        Prints a congratulatory message with game statistics.
        """
        if "_" not in self.correctly_guessed_letters:
            print(f"Well Done!! You found the word: {self.word_to_find} in {self.turn_count} turns with {self.error_count} errors!")

    def display(self):
        """
        Displays the hangman state based on the number of lives remaining.
        """
        if self.lives == 5:
            print("""
        |
        |
        |
        |
        |
    """)

        elif self.lives == 4:
            print("""
        |-------
        |
        |
        |
        |
    """)

        elif self.lives == 3:
            print("""
        |-------
        |       |
        |       O
        |
        |
    """)

        elif self.lives == 2:
            print("""
        |-------
        |       |
        |       O
        |       |
        |
    """)

        elif self.lives == 1:
            print("""
        |-------
        |       |
        |       O
        |      /|\\
        |
    """)

        elif self.lives == 0:
            print("""
        |-------
        |       |
        |       O
        |      /|\\
        |       |
        |      / \\
    """)



    def start_game(self):
        """
        Starts the game and continues until the player either wins or loses.
        Calls the play method for each turn and updates the game display.
        """
        print(self.correctly_guessed_letters)
        while self.lives > 0 and "_" in self.correctly_guessed_letters:
            self.play()
            self.display()
            if self.lives == 0:
                self.game_over()
            elif "_" not in self.correctly_guessed_letters:
                self.well_played()


play_game = Hangman()
play_game.start_game()




