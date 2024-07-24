from player import Player

from enum import Enum, auto

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
        self.players = []
        self.com_cards = []
        self.pot = 0
        self.deck = self.create_deck()

    def create_deck(self):
        deck = [(rank, suit) for suit in Suit for rank in Rank]
        return deck

    def shuffle_deck(self):
        import random
        random.shuffle(self.deck)

    def add_player(self, player):
        self.players.append(player)

    def add_to_pot(self, amount):
        self.pot += amount
        
    def deal_community_cards(self, num_cards):
        for _ in range(num_cards):
            card = self.deck.pop()
            self.com_cards.append(card)

    def deal_to_player(self, player, num_cards):
        for _ in range(num_cards):
            card = self.deck.pop()
            player.cards.append(card)

