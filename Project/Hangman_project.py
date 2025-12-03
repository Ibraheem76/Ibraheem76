import random
import os

WORDS = [
    "python", "hangman", "variable", "function", "program", "computer",
    "keyboard", "network", "database", "algorithm", "debug", "module",
    "package", "integer", "string", "conditional", "iteration"
]

HANGMAN_PICS = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    ========="""
]

def choose_word():
    fn = "words.txt"
    if os.path.exists(fn):
        try:
            with open(fn, "r", encoding="utf-8") as f:
                words = [w.strip() for w in f if w.strip()]
                if words:
                    return random.choice(words).lower()
        except:
            pass
    
    return random.choice(WORDS).lower()


def display_state(secret, guessed, wrong_count, max_wrong):
    stage_index = min(wrong_count, len(HANGMAN_PICS) - 1)
    print(HANGMAN_PICS[stage_index])

    revealed = " ".join(c if c in guessed else "_" for c in secret)
    print("\nWord:", revealed)
    print(f"Guessed letters: {', '.join(sorted(guessed)) if guessed else '(none)'}")
    print(f"Wrong guesses: {wrong_count} / {max_wrong}\n")


def get_guess(guessed):
    while True:
        g = input("Enter a letter: ").strip().lower()
        if len(g) != 1 or not g.isalpha():
            print("Please enter a single alphabetical character.")
            continue
        if g in guessed:
            print("You have already guessed that letter.")
            continue
        return g


def pick_difficulty():
    print("Pick difficulty: (E)asy, (N)ormal, (H)ard")
    while True:
        choice = input("Choice [N]: ").strip().lower() or "n"
        if choice.startswith("e"):
            return 6
        if choice.startswith("h"):
            return 4
        if choice.startswith("n"):
            return 5
        print("Enter E, N, or H.")


def play_round():
    secret_word = choose_word()
    max_wrong = pick_difficulty()
    guessed_letters = set()
    wrong_guesses = 0

    print("\nLet's play Hangman!")

    while True:
        display_state(secret_word, guessed_letters, wrong_guesses, max_wrong)

        # Win condition
        if all(c in guessed_letters for c in secret_word):
            score = (max_wrong - wrong_guesses) + 1
            print(f"Congratulations! You guessed the word '{secret_word}'!")
            print(f"Your score: {score}")
            break

        # Lose condition
        if wrong_guesses >= max_wrong:
            print(HANGMAN_PICS[-1])
            print(f"Sorry, you've been hanged! The word was '{secret_word}'.")
            break

        guess = get_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess in secret_word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            wrong_guesses += 1


def main():
    print("Welcome to Hangman!")
    while True:
        play_round()
        again = input("Play again? (Y/N): ").strip().lower()
        if not again.startswith("y"):
            print("Thanks for playing Hangman! Goodbye.")
            break


if __name__ == "__main__":
    main()
