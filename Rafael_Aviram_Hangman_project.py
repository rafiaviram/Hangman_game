import random
import time

# Define phrases
PHRASES = [
    "Do your best",
    "Dreams come true",
    "Drill your skills",
    "Embrace Carpe Diem",
    "Embrace constant change",
    "Emotions create relatability",
    "Energy draws attention",
    "Enforce consequences rigorously",
    "Exceptional makes memorable",
    "Exclusivity adds value",
    "Focus and win",
]

# Select a random phrase
phrase = random.choice(PHRASES)

# Split the phrase into words
words = phrase.split()

# Create a set of unique letters in the phrase
unique_letters = set("".join(words))

# Initialize the guess word with underscores
guess_word = ["_" if letter.isalpha() else letter for letter in phrase]

# Start the game
print("Welcome to Hangman!")
print(f"The phrase has {len(words)} words and {len(unique_letters)} unique letters.")

# Initialize the number of guesses, incorrect guesses, and score
num_guesses = 0
num_incorrect_guesses = 0
score = 0

# Start the timer
start_time = time.time()

# Loop until the player has guessed all letters
while "_" in guess_word:
    # Print the current state of the game
    print(" ".join(guess_word))

    # Ask the player for a guess
    guess = input("Guess a letter: ")

    # Check if the guess is valid
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid guess. Please enter a single letter.")
        continue

    # Check if the guess is correct
    if guess in unique_letters:
        # Update the guess word with the correct guess
        for i, letter in enumerate(phrase):
            if letter == guess:
                guess_word[i] = letter
        print("Correct!")
        score += 5
    else:
        print("Incorrect.")
        num_incorrect_guesses += 1
        score -= 1

    # Increment the number of guesses
    num_guesses += 1

# Stop the timer
end_time = time.time()

# Calculate the time taken to guess the phrase
time_taken = end_time - start_time

# Check if the player guessed the phrase quickly enough for the bonus
if time_taken < 30:
    score += 30
    print("Congratulations, you won and earned a bonus of 30 points!")
else:
    print("Congratulations, you won!")

# Print the final score
print(f"Your score is {score}.")
