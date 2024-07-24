from enum import Enum, auto
import random

class Status(Enum):
    ACTIVE = auto()
    FOLDED = auto()
    ALL_IN = auto()

class Player:
    def __init__(self, name, money):
        self.name = name
        self.cards = []
        self.money = money
        self.status = Status.ACTIVE
        self.current_bet = 0

    def bet(self, amount):
        if amount > self.money:
            raise ValueError("Cannot bet more money than the player has")
        self.money -= amount
        self.current_bet += amount

    def fold(self):
        self.status = Status.FOLDED

    def go_all_in(self):
        self.current_bet += self.money
        self.money = 0
        self.status = Status.ALL_IN

