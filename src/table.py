from player import Player
from enum import Enum, auto
import random

class Rank(Enum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14

class Suit(Enum):
    HEARTS = auto()
    DIAMONDS = auto()
    CLUBS = auto()
    SPADES = auto()


class Table:
    def __init__(self):
        """
        Initializes a new instance of the `Table` class.

        This method initializes a new instance of the `Table` class. It sets the initial values for the instance variables `players`, `com_cards`, `pot`, and `deck`.

        Parameters:
            None

        Returns:
            None
        """
        self.players = []
        self.com_cards = []
        self.pot = 0
        self.deck = self.create_deck()

    def create_deck(self):
        """
        Creates a new deck of cards.

        Returns:
            list: A list of tuples representing each card in the deck. Each tuple contains the rank and suit of a card.
        """
        deck = [(rank, suit) for suit in Suit for rank in Rank]
        return deck

    def shuffle_deck(self):
        """
        Shuffles the deck of cards.

        This method shuffles the deck of cards by using the `random.shuffle()` function from the `random` module. It takes the `self.deck` list, which represents the deck of cards, and shuffles it in place.

        Parameters:
            None

        Returns:
            None
        """
        random.shuffle(self.deck)

    def add_player(self, player):
        """
        Adds a player to the list of players.

        Parameters:
            player (Player): The player to be added.

        Returns:
            None
        """
        self.players.append(player)

    def add_to_pot(self, amount):
        """
        Adds the given amount to the pot.

        Args:
            amount (float): The amount to be added to the pot.

        Returns:
            None
        """
        self.pot += amount
        
    def deal_community_cards(self, num_cards):
        """
        Deals a specified number of community cards from the deck and adds them to the list of community cards.

        Parameters:
            num_cards (int): The number of community cards to deal.

        Returns:
            None
        """
        for _ in range(num_cards):
            card = self.deck.pop()
            self.com_cards.append(card)

    def deal_to_player(self, player, num_cards):
        """
        Deals a specified number of cards to a player from the deck.

        Args:
            player (Player): The player to whom the cards will be dealt.
            num_cards (int): The number of cards to deal to the player.

        Returns:
            None
        """
        for _ in range(num_cards):
            card = self.deck.pop()
            player.cards.append(card)

