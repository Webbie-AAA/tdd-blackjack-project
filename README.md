# Blackjack TDD Project

A command-line game of blackjack in Python, built using **test-driven development (TDD)** and checked with **pylint**.

This was part of a class on learning how to build blackjack. I've since gone back and rewritten the main game code from memory to revise the concepts and test my own ability.

## About the tests

There are two sets of tests:

- **Coach tests:** written by the teachers, which I had to complete and make pass
- **Trainee tests:** written by me

A seeded shuffle makes the game testable. The same seed always produces the same deck, so tests can check exact outcomes:

```python
def shuffle(deck: list, seed: int) -> list[str]:
    """Randomises a deck of cards"""
    copy_of_deck = deck.copy()
    Random(seed).shuffle(copy_of_deck)
    return copy_of_deck
```

The game returns three possible results: `"You win!"`, `"You lose!"` and `"Draw!"`.

## Running the project

```bash
python blackjack.py
pytest
pylint blackjack.py
```

## What I practised

- Test-driven development: writing tests first, then code to pass them
- Making random behaviour testable with seeds
- Code quality and style with pylint
- Writing code from memory to check my understanding
