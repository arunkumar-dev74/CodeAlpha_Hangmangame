
import random

# Predefined words
words = ["python", "computer", "coding", "program", "developer"]

# Select a random word
secret_word = random.choice(words)

# Game variables
guessed_letters = []
incorrect_guesses = 0
max_attempts = 6

print("================================")
print("       HANGMAN GAME")
print("================================")
print("Guess the hidden word!")
print("You have 6 incorrect guesses.")

# Main game loop
while incorrect_guesses < max_attempts:

    # Display the word
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Incorrect guesses:", incorrect_guesses)
    print("Guessed letters:", guessed_letters)

    # Check winning condition
    if all(letter in guessed_letters for letter in secret_word):
        print("\nCongratulations! You won!")
        print("The word was:", secret_word)
        break

    # Take user input
    guess = input("\nGuess a letter: ").lower().strip()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet letter!")
        continue

    if guess in guessed_letters:
        print("You already guessed this letter!")
        continue

    guessed_letters.append(guess)

    # Check the guessed letter
    if guess in secret_word:
        print("Correct guess!")
    else:
        incorrect_guesses += 1
        print("Wrong guess!")

# Losing condition
if incorrect_guesses == max_attempts:
    print("\nGame Over!")
    print("The correct word was:", secret_word)

print("\nThanks for playing Hangman!")
