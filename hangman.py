import random

# ==============================
#      HANGMAN GAME
# ==============================

print("===================================")
print("      WELCOME TO HANGMAN")
print("===================================")

# Predefined words
words = ["python", "gaming", "laptop", "coding", "apple"]

# Randomly choose a word
word = random.choice(words)

# Create hidden word display
display = ["_"] * len(word)

# Store guessed letters
guessed_letters = []

# Total lives
lives = 6

# Game loop
while lives > 0 and "_" in display:

    print("\nWord:", " ".join(display))
    print("Lives Left:", lives)
    print("Guessed Letters:", guessed_letters)

    # User input
    guess = input("Enter a letter: ").lower()

    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only ONE alphabet letter.")
        continue

    # Check repeated guess
    if guess in guessed_letters:
        print("You already guessed this letter.")
        continue

    # Save guessed letter
    guessed_letters.append(guess)

    # Correct guess
    if guess in word:
        print("Correct Guess!")

        # Reveal letters
        for index in range(len(word)):
            if word[index] == guess:
                display[index] = guess

    # Wrong guess
    else:
        lives -= 1
        print("Wrong Guess!")

# Final result
print("\n==============================")

if "_" not in display:
    print("CONGRATULATIONS! YOU WON!")
    print("The word was:", word)

else:
    print("GAME OVER!")
    print("The correct word was:", word)

print("==============================")