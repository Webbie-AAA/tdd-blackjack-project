from collections import Counter
from time import time
from random import Random
import argparse

LOSE_MESSAGE = "You lose!"
WIN_MESSAGE = "You win!"
DRAW_MESSAGE = "Draw!"


def shuffle(deck: list, seed: int) -> list[str]:
    """Randomises a deck of cards"""
    copy_of_deck = deck.copy()
    Random(seed).shuffle(copy_of_deck)
    return copy_of_deck


def generate_deck() -> list[str]:
    """Generates a deck of cards and returns them"""
    cards = []
    rank = ["A", "2", "3", "4", "5", "6",
            "7", "8", "9", "10", "J", "Q", "K"]
    suits = ["S", "D", "C", "H"]
    for s in suits:
        for r in rank:
            pair = r + s
            cards.append(pair)

    return cards


def points_for(cards: list[str]) -> int:
    """Calculates the amount of points for a given list of cards"""
    if cards == []:
        return 0

    for card in cards:
        if card in generate_deck():

            ranks = []
            for card in cards:
                rank = card[:-1]
                ranks.append(rank)

            return points_for_card(ranks)

        else:

            return "Invalid input"


def points_for_card(ranks):
    """Returns points in a card"""
    ranks_dict = {"A": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
                  "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}

    points = 0
    if ranks[0] == "A" and ranks[1] == "A" and len(ranks) == 2:
        return 21

    for rank in ranks:
        points += ranks_dict[rank]

    return points


def get_next_card_from_deck(deck: list[str]) -> str:
    """Gets the next card from the deck and returns it"""

    card_draw = deck.pop(0)
    return card_draw


def deal_card_to_player(deck: list[str], player: dict) -> None:
    """
    Draws a card from the deck and adds it to the player's hand
    """

    new_card = get_next_card_from_deck(deck)
    player["hand"].append(new_card)


def deal_card_to_dealer(deck: list[str], dealer: dict) -> None:
    """
    Draws a card from the deck and adds it to the player's hand
    """

    new_card = get_next_card_from_deck(deck)
    dealer["hand"].append(new_card)


def player_turn(deck: list[str], player: dict) -> bool:
    """
    Asks the player for their next choice and changes the game state
    based on their response of either 'hit' or 'stick'
    """

    print(
        f"Your hand is {', '.join(player['hand'])} ({points_for(player['hand'])} points)")
    # Accept the choice from the player
    action = input('What do you want to do? ("hit" or "stick")')

    if action == "hit":

        deal_card_to_player(deck, player)

        print("Hitting")

        player_cards = player["hand"]
        print(f"You draw {player_cards[-1]}")
        return True
    elif action == "stick":

        return False  # End the player's turn
    else:
        return None


def get_player_name() -> str:
    """Takes the players name"""
    return input("What is your name?")


def dealer_turn(deck: list[str], dealer: dict) -> bool:
    """Decides the the Dealer's choice between 'hit' or 'stick' based on the number of points"""
    print(
        f"Dealer's hand is {', '.join(dealer['hand'])} ({points_for(dealer['hand'])} points)")
    total_points = points_for(dealer["hand"])
    dealers_cards = dealer["hand"]
    if total_points <= 17:
        deal_card_to_dealer(deck, dealer)
        print(f"Dealer draws {dealers_cards[-1]}")
        print(
            f"Dealer's hand is {', '.join(dealer['hand'])} ({points_for(dealer['hand'])} points)")
    else:

        return False


def play(seed: int) -> None:  # First function that plays
    """
    Generates a deck and deals cards to the player and dealer.

    The 'seed' parameter is used to set a specific game. If you play the game
    with seed=313131 it will always have the same outcome (the order the cards are dealt)
    """
    new_deck = generate_deck()  # This variable is triggered and it goes to the function
    shuffled_deck = shuffle(new_deck, seed)
    name = get_player_name()

    print(f"Player {name} has entered the game")

    player = {
        "hand": [shuffled_deck.pop(0), shuffled_deck.pop(0)],
        "name": name
    }

    is_player_turn = True

    while is_player_turn:
        is_player_turn = player_turn(shuffled_deck, player)

    dealer = {
        "hand": [shuffled_deck.pop(0), shuffled_deck.pop(0)],
        "name": "Dealer"
    }

    is_dealer_turn = True

    if is_player_turn == False:
        while is_dealer_turn:
            is_dealer_turn = dealer_turn(shuffled_deck, dealer)

    player_points = points_for(player["hand"])
    dealer_points = points_for(dealer["hand"])

    if player_points > 21:
        print(LOSE_MESSAGE)
    elif dealer_points > 21:
        print(WIN_MESSAGE)
    elif player_points > dealer_points:
        print(WIN_MESSAGE)
    elif dealer_points > player_points:
        print(LOSE_MESSAGE)
    else:
        print(DRAW_MESSAGE)


def get_seed() -> int:
    """
    You can safely ignore this function. It is used to accept a seed from the command line.
    For example

    python3 blackjack.py --seed 313131

    Would play the game with defined seed of 313131
    """
    parser = argparse.ArgumentParser("blackjack")
    parser.add_argument(
        "--seed", dest='seed', help="The seed that a game will be played with", type=float)
    args = parser.parse_args()
    seed = args.seed

    # If no seed is given, use the current time as the seed
    if seed is None:
        return time()

    return seed


if __name__ == "__main__":
    seed = get_seed()
    play(seed)
