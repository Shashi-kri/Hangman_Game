"""
Hangman Game — Console Edition
================================
A simple text-based Hangman game where the player guesses a word
one letter at a time.

Rules:
  - A random word is chosen from a small predefined list.
  - The player has 6 incorrect guesses before losing.
  - Letters are guessed one at a time via keyboard input.

Key Concepts: random, while loop, if-else, strings, lists.
"""

import random

# WORD LIST  (5 predefined words)
WORDS = ["python", "hangman", "keyboard", "science", "dragon"]

# HANGMAN ASCII STAGES  (0 = safe … 6 = dead)
HANGMAN_STAGES = [
    # 0 wrong guesses
    """
   +---+
   |   |
       |
       |
       |
       |
=========
    """,
    # 1 wrong guess
    """
   +---+
   |   |
   O   |
       |
       |
       |
=========
    """,
    # 2 wrong guesses
    """
   +---+
   |   |
   O   |
   |   |
       |
       |
=========
    """,
    # 3 wrong guesses
    """
   +---+
   |   |
   O   |
  /|   |
       |
       |
=========
    """,
    # 4 wrong guesses
    """
   +---+
   |   |
   O   |
  /|\\  |
       |
       |
=========
    """,
    # 5 wrong guesses
    """
   +---+
   |   |
   O   |
  /|\\  |
  /    |
       |
=========
    """,
    # 6 wrong guesses — game over
    """
   +---+
   |   |
   O   |
  /|\\  |
  / \\  |
       |
=========
    """,
]

MAX_WRONG = 6


# HELPER FUNCTIONS

def get_display(word: str, guessed: list) -> str:
    """Return the word with un-guessed letters shown as underscores."""
    return "  ".join(letter if letter in guessed else "_" for letter in word)


def print_state(wrong_count: int, word: str, guessed: list, wrong_letters: list) -> None:
    """Print the current hangman stage, word progress, and wrong guesses."""
    print(HANGMAN_STAGES[wrong_count])
    print(f"  Word:   {get_display(word, guessed)}")
    print(f"  Wrong guesses ({wrong_count}/{MAX_WRONG}): {', '.join(wrong_letters) if wrong_letters else '-'}")
    print()


def is_solved(word: str, guessed: list) -> bool:
    """Return True when every letter in the word has been guessed."""
    return all(letter in guessed for letter in word)


def get_valid_guess(guessed: list) -> str:
    """Prompt the player until a new, single alphabetic letter is entered."""
    while True:
        guess = input("  Guess a letter: ").strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            print("  [!] Please enter a single letter (a-z).\n")
        elif guess in guessed:
            print(f"  [!] You already guessed '{guess}'. Try another.\n")
        else:
            return guess


def play_game() -> bool:
    """
    Run one full game of Hangman.

    Returns:
        True if the player won, False if they lost.
    """
    word = random.choice(WORDS)
    guessed: list = []       # all letters guessed so far
    wrong_letters: list = [] # only the incorrect ones
    wrong_count: int = 0

    print("\n" + "=" * 40)
    print("       Welcome to HANGMAN!")
    print("=" * 40)
    print(f"  The word has {len(word)} letters. You have {MAX_WRONG} lives.")
    print()

    while wrong_count < MAX_WRONG:
        print_state(wrong_count, word, guessed, wrong_letters)

        if is_solved(word, guessed):
            print(f"  *** You guessed it!  The word was: '{word.upper()}' ***")
            return True

        guess = get_valid_guess(guessed)
        guessed.append(guess)

        if guess in word:
            print(f"  [+] '{guess}' is in the word!\n")
        else:
            wrong_letters.append(guess)
            wrong_count += 1
            remaining = MAX_WRONG - wrong_count
            if remaining > 0:
                print(f"  [-] '{guess}' is NOT in the word. {remaining} guess(es) left.\n")

    # Final state — player lost
    print_state(wrong_count, word, guessed, wrong_letters)
    print(f"  GAME OVER! The word was: '{word.upper()}'")
    return False


# ─────────────────────────────────────────
# MAIN LOOP
# ─────────────────────────────────────────

def main() -> None:
    """Entry point — loops until the player chooses to quit."""
    print("\n" + "=" * 40)
    print("          H A N G M A N")
    print("=" * 40)

    while True:
        play_game()

        print()
        again = input("  Play again? (y/n): ").strip().lower()
        if again != "y":
            print("  Thanks for playing! Goodbye!\n")
            break


if __name__ == "__main__":
    main()
