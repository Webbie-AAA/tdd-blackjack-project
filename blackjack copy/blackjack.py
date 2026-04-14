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
    suits = ["S", "D", "C", "H"]
    ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    for s in suits:
        for r in ranks:
            cards.append(r + s)

    return cards


def points_for_card(card: str) -> int:
    """Calculates the amount of points given for a single card"""
    ranks = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
             "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "K": 10, "Q": 10, "A": 11}

    rank = ranks[card[:-1]]
    return rank


def points_for(cards: list[str]) -> int:
    """Calculates the amount of points for a given list of cards"""

    if len(cards) == 2 and cards[0][:-1] == "A" and cards[1][:-1] == "A":
        return 21
    total = 0
    for card in cards:
        total += points_for_card(card)

    return total


def get_next_card_from_deck(deck: list[str]) -> str:
    """Gets the next card from the deck and returns it"""
    card = deck.pop(0)
    return card


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

        # TODO: Implement the rest of the players turn
        # It's still the player's turn
        deal_card_to_player(deck, player)
        player_points = points_for(player["hand"])
        print("Hitting")
        players_card = player["hand"]
        print(f"You draw {players_card[-1]}")
        if player_points > 21:
            print(
                f"Your hand is {', '.join(player['hand'])} ({points_for(player['hand'])} points)")
            print("You lose!")
            exit()
        return True
    elif action == "stick":

        return False  # End the player's turn
    else:
        return None


def get_player_name() -> str:

    return input("What is your name?")


def dealer_turn(deck: list[str], dealer: dict) -> bool:

    print(
        f"Dealer's hand is {', '.join(dealer['hand'])} ({points_for(dealer['hand'])} points)")
    dealer_points = points_for(dealer["hand"])
    if dealer_points < 17:
        deal_card_to_dealer(deck, dealer)
        print(f"Dealer draws {dealer["hand"][-1]}")
        return True
    if dealer_points > 21:
        print("You win!")
        exit()
    return False

    ...


def blackjack_outcome(player_hand: list[str], dealer_hand: list[str]) -> str:
    if player_hand == dealer_hand:
        print("It's a draw!")
    elif player_hand == 21:
        print("You win!")
    elif dealer_hand == 21:
        print("You lose!")
    elif player_hand > dealer_hand:
        print("You win!")
    else:
        print("You lose!")
    exit()


def play(seed: int) -> None:
    """
    Generates a deck and deals cards to the player and dealer.

    The 'seed' parameter is used to set a specific game. If you play the game
    with seed=313131 it will always have the same outcome (the order the cards are dealt)
    """
    new_deck = generate_deck()
    shuffled_deck = shuffle(new_deck, seed)
    name = get_player_name()

    print(f"Player {name} has entered the game")

    player = {
        "hand": [shuffled_deck.pop(0), shuffled_deck.pop(0)],
        "name": name
    }

    dealer = {
        "hand": [shuffled_deck.pop(0), shuffled_deck.pop(0)],
        "name": "Dealer"
    }

    is_player_turn = True

    while True:

        while is_player_turn:
            is_player_turn = player_turn(shuffled_deck, player)
        # TODO: Implement the Dealer's turn
        is_dealer_turn = True

        while is_dealer_turn:
            is_dealer_turn = dealer_turn(shuffled_deck, dealer)
        # TODO: Implement the end of the game
        blackjack_outcome(player["hand"], dealer["hand"])


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
