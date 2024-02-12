import random
#Global variable for tries
def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]

#Global variable for words
words = ('cat dog tiger gorilla giraffe mouse beaver camel' 
         'coyote wolf rat ant panther puma aardvark bear' 
         'lynx fox elephant swan duck shark badger').split()
#Global variable for guessed
guessed = False
#Global variable for guessed letters
guessed_letters = []
#Global variable for guessed word
guessed_word = []
#Global variable for tries
tries = 6
def main():

    while True:
        play(choose_word())
   
        play_again = input("Thanks for playing! Play again? (Yes/No)")
        if play_again != "Yes":
            break

def choose_word():
    word = random.choice(words).upper()
    return word

def play(word):
    global guessed_letters
    global tries

    complete_word = "_" * len(word)

    print("Welcome to Hangman Classic!")
    print("Word list: Animals")
    print(complete_word)

    while tries > 0:
        guess = input("Please guess a letter or a word: ").upper()

        if guess in guessed_letters:
            print("You have already guessed that letter or word")
            guessed_letters.append(guess)
            guessed_letters.append(guess)
