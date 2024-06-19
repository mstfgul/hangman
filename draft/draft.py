def get_word():
    secret_word = input("Choose your secret word: ")
    return secret_word

def get_lives():
    lives_left = int(input("Enter a number of lives: "))
    return lives_left


def get_guess(guessed_letters=[]):
    while True:
        guessed_letter = input("Enter a letter: ")
        if len(guessed_letter) != 1:
            print("Please enter just one letter.")
        elif guessed_letter in guessed_letters:
            print("The letter has already been suggested.")
        else:
            return guessed_letter
    

def asses_guess(secret_word, guessed_letter, lives_left):
        if guessed_letter in [i for i in secret_word]:
            print("the letter is correct")
        else:
            lives_left -=1
            print(f"the letter is wrong and you still have {lives_left} lives")
        return lives_left
        


def display_word(secret_word, guessed_letters = []):
    result = []
    is_word_found = False
    for letter in secret_word:
        if letter in list(guessed_letters):
            result.append(letter)
        else:
            result.append("_")
    result_in_string = " ".join(result) 
    print(result_in_string)

    if "_" not in list(result_in_string):
        is_word_found = True
    return is_word_found


    

    
def main():
    secret_word = get_word()
    lives_left = get_lives()
    guessed_letters = []
    is_word_found = False
    while not is_word_found and lives_left > 0:
        letter = get_guess(guessed_letters)
        lives_left = asses_guess(secret_word,letter, lives_left)
        guessed_letters.append(letter)
        display_word(secret_word, guessed_letters)
        if lives_left == 0:
            print("GAME OVER")
            break
main()
        
