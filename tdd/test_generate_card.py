# pylint: skip-file

"""Tests for the generate_card.py file"""

from generate_card import generate_card, get_score

"""Tests that the generate_card function returns the correct card"""


def test_generate_card():
    assert generate_card("H", "8") == "8H"
    pass

# TODO: Write several more tests below using different inputs for the generate_card function. You won't be able to cover them all - but try to cover the main cases.


def test_invalid_suit_letter():
    """Tests that the generate_card function returns an error message if the suit is invalid"""
    assert generate_card("O", "8") == "Error. Invalid suit"


# TODO: Write several tests below to test this function


def test_invalid_suit_datatype():
    assert generate_card(8, "8") == "Error. Invalid input"
    pass


def test_invalid_rank_datatype():
    assert generate_card("8", 8) == "Error. Invalid input"
    pass


def test_empty_string_suit():
    assert generate_card("", "8") == "Error. Empty string"
    pass


def test_empty_string_rank():
    assert generate_card("8", "") == "Error. Empty string"
    pass


"""Tests that the generate_card function returns an error message if the number is invalid"""
# TODO: Write several tests below to test this function


def test_invalid_number_card():
    assert generate_card("S", "11") == "Error. Invalid number"


def test_negative_number():
    assert generate_card("S", "-1") == "Error. Invalid number"


"""Tests that the get_score function returns the correct score"""
# TODO: Write several tests below to test this function


def test_get_card_score():
    assert get_score("8H") == 8


"""Tests that the get_score function returns 0 if the card is invalid"""
# TODO: Write several tests below to test this function


def test_get_card_score_invalid():
    assert get_score("11H") == 0
