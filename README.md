# Hangman Game — Console Edition

A simple text-based Hangman game where the player guesses a word one letter at a time.

## How to Run

```bash
python main.py
```

No external libraries required — uses only the Python standard library.

## Rules

- A random word is chosen from a list of **5 predefined words**.
- The player guesses one letter at a time.
- **6 incorrect guesses** are allowed before the game is lost.
- An ASCII-art hangman is drawn after each wrong guess.

## Word List

```
python, hangman, keyboard, science, dragon
```

## Key Concepts Used

| Concept | Where used |
|---------|-----------|
| `random` | `random.choice()` picks the secret word |
| `while` loop | Main game loop and input validation loop |
| `if-else` | Correct/wrong guess branching, win/lose checks |
| Strings | Word display, input handling, ASCII art stages |
| Lists | `WORDS` pool, `guessed` letters, `wrong_letters` |

## Sample Run

```
========================================
       Welcome to HANGMAN!
========================================
  The word has 6 letters. You have 6 lives.

   +---+
   |   |
       |
       |
       |
       |
=========

  Word:   _  _  _  _  _  _
  Wrong guesses (0/6): -

  Guess a letter: p
  ✅ 'p' is in the word!
  ...
```
