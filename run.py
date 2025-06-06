import random


# Global variable for tries
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


# Global variable for words
words = ('cat dog tiger gorilla giraffe mouse beaver camel' 
         'coyote wolf rat ant panther puma aardvark bear' 
         'lynx fox elephant swan duck shark badger').split()


# Global variable for guessed
guessed = False


# Global variable for guessed letters
guessed_letters = []


# Global variable for guessed word
guessed_word = []


# Global variable for tries
tries = 6


def main():
    global guessed_letters
    global tries

    print("Welcome to hangman!")
    print("\n")
    print("The goal of the game is to guess the word.")
    print("To guess the word type your letter of choice.")
    print("Guess the word before you get hanged.")
    print("Good luck!")
    print("\n")
    start = input("Press enter to start the game...")

    while True:
        guessed_letters = []
        tries = 6
        play(choose_word())
        play_again = input("Thanks for playing! Play again? (Yes/No)").lower()
        if play_again == "yes":
            continue
        elif play_again == "no":
            print("See you later!")
            break


def choose_word():
    word = random.choice(words).upper()
    return word


def play(word):
    global guessed_letters
    global tries

    complete_word = "_" * len(word)

    print(display_hangman(tries))
    print("Word list: Animals")
    print(complete_word)

    while tries > 0:
        guess = input("Please guess a letter: ").upper()

        if guess in guessed_letters:
            print("You have already guessed that letter")
        elif guess not in word:
            wrong_guess = ("Wrong guess!",
                           "Womp womp...",
                           "Oh no!",
                           "Take another guess!",
                           "Close. But not close enough.")
            print(random.choice(wrong_guess))
            tries -= 1
            guessed_letters.append(guess)
            print(display_hangman(tries))
            print(complete_word)

        else:
            right_guess = ("You guessed " + guess + " and you were right!",
                           "Good job! " + guess + " is in the word",
                           guess + " is right!")
            for i in range(len(word)):
                if word[i] == guess:
                    complete_word = complete_word[:i] + guess + complete_word[i+1:]
            print(random.choice(right_guess))
            print(complete_word)
            guessed_letters.append(guess)
            print(display_hangman(tries))
            if complete_word == word:
                print("Winner Winner! Chicken Dinner!")
                break


if __name__ == "__main__":
    main()
