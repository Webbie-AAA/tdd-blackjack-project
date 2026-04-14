# pylint: skip-file
"""File for tests written by you - the trainee"""

from blackjack import generate_deck, points_for, play, get_next_card_from_deck, deal_card_to_player
from support.testing_util import player_chooses


# Tests for get_next_card_from_deck

def test_get_one_card_from_deck():
    """Assert the function returns only one card from the deck"""
    # Arrange
    card_drawn = ["2S"]
    # Act
    result = get_next_card_from_deck(card_drawn)
    # Assert
    assert len(result) == 2
    pass


def test_draws_first_card_from_deck():
    """Assert the function returns the first card in the deck """
    # Arrange
    list_of_cards = ['AS', '2S', '3S', '4S',
                     '5S', '6S', '7S', '8S', '9S', '10S']
    # Act
    result = get_next_card_from_deck(list_of_cards)
    # Assert
    assert result == "AS"
    pass


def test_draw_modifies_deck_size():
    # Arrange
    deck = ['AS', '2S', '3S', '4S',
            '5S', '6S', '7S', '8S', '9S', '10S']
    len_of_deck = len(deck)
    # Act
    get_next_card_from_deck(deck)
    # Assert
    assert len(deck) == len_of_deck-1


# Tests for deal_card_to_player()

def test_player_hand_updated():
    """Checks Player dict "hand" key value has been updated to one more"""
    # Arrange
    deck = ['AS', '2S', '3S', '4S',
            '5S', '6S', '7S', '8S', '9S', '10S']
    player_hand = {"hand": ['AS', '2S', '3S']}
    hand_list = player_hand["hand"]
    original_count = len(hand_list)
    # Act
    deal_card_to_player(deck, player_hand)
    # Assert
    assert len(player_hand['hand']) == original_count+1


def test_deck_size_updates():
    """Checks the deck of cards has been updated to one less"""
    # Arrange
    deck = ['AS', '2S', '3S', '4S',
            '5S', '6S', '7S', '8S', '9S', '10S']
    player_hand = {"hand": ['AS', '2S', '3S']}
    # Act
    result = deal_card_to_player(deck, player_hand)
    # Assert
    assert len(deck) == 10-1


def test_correct_card_is_dealt():
    # Arrange
    deck = ['AS', '2S', '3S', '4S']
    player_hand = {"hand": ['KH', 'QH']}
    expected_card = deck[0]
    # Act
    deal_card_to_player(deck, player_hand)
    # Assert
    assert player_hand["hand"][-1] == expected_card


def test_deck_is_updated():
    # Arrange
    deck = ['AS', '2S', '3S', '4S']
    player_hand = {"hand": ['KH', 'QH']}
    expected_card = deck[0]
    # Act
    deal_card_to_player(deck, player_hand)
    # Assert
    assert expected_card not in deck
