# pylint: skip-file

"""File for tests written by you - the trainee"""

from blackjack import generate_deck, points_for, play, get_next_card_from_deck, deal_card_to_player, points_for_card
from support.testing_util import player_chooses


def test_points_for_card():
    assert points_for_card("8C") == 8


def test_points_for_card_non_int_rank():
    assert points_for_card("AC") == 11


def test_points_for_10():
    assert points_for_card("10S") == 10


def test_get_next_card_from_deck():
    deck = ['JS',
            'QS',
            'KS',
            'AD',
            '2D',
            '3D',
            '4D',]
    assert get_next_card_from_deck(deck) == '4D'


def test_deck_length_changes():
    deck = ['7C',
            '8C',
            '9C',
            '10C',
            'JC',
            'QC',
            'KC',
            'AH',
            '2H']
    get_next_card_from_deck(deck)
    assert len(deck) == 8


def test_deal_card_to_player():
    # Arrange
    player_dict = {"name": "name", "hand": ['JC', 'QC', 'KC', 'AH', '2H']}
    deck = ['7C', '8C', '9C', '10C', 'JC', 'QC', 'KC', 'AH', '2H']
    # Act
    deal_card_to_player(deck, player_dict)
    # Assert
    assert player_dict['hand'] == ['JC', 'QC', 'KC', 'AH', '2H', '2H']
