"""This file is used to generate a card for the blackjack game"""


def generate_card(suit: str, number: str) -> str:
    """Generates a card based on the suit and number. (e.g. 8C) Should return an "Error" message if the suit or number is invalid."""
    if type(number) != str or type(suit) != str:
        return "Error. Invalid input"
    elif number == "" or suit == "":
        return "Error. Empty string"
    elif number not in ["2", "3", "4", "5", "6", "7", "8", "9", "10"]:
        return "Error. Invalid number"
    elif suit not in ["S", "H", "C", "D"]:
        return "Error. Invalid suit"
    else:
        return number + suit


def get_score(card: str) -> int:
    """Gets the score of the card (e.g. 8H returns 8). Return 0 if the card is invalid"""
    total = 0
    number = int(card[:-1])
    if number in range(2, 11):
        total += number
        return total
    else:
        return 0
