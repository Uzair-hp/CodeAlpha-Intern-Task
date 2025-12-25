import random

words = ["python", "java", "coding", "logic", "debug"]
word = random.choice(words)

guessed_letters = []
attempts = 6
display = ["_"] * len(word)

print("Welcome to Hangman Game!")
print("Guess the word:", " ".join(display))

while attempts > 0 and "_" in display:
    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single valid letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Good guess!")
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
    else:
        attempts -= 1
        print("Wrong guess! Attempts left:", attempts)

    print("Word:", " ".join(display))
    print()

if "_" not in display:
    print(" Congratulations! You guessed the word:", word)
else:
    print("Game Over! The word was:", word)
