
word = input("Enter the secret word: ").lower()

print("\n" * 50)

guessed_letters = []
wrong_guesses = 0
max_wrong = 6

display_word = ["_"] * len(word)

print(" Welcome to Hangman!")

while wrong_guesses < max_wrong and "_" in display_word:

    print("\nWord:", " ".join(display_word))
    print("Guessed letters:", " ".join(guessed_letters))
    print("Remaining attempts:", max_wrong - wrong_guesses)

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print(" Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print(" You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print(" Correct!")

        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess
    else:
        print(" Wrong!")
        wrong_guesses += 1


if "_" not in display_word:
    print("\n🎉 CONGRA YOU WIN !!! The word was:", word)
else:
    print("\n💀 OHH YOU LOST !!! The word was:", word)