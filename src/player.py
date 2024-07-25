from enum import Enum, auto
import random
import names

class Status(Enum):
    ACTIVE = auto()
    FOLDED = auto()
    ALL_IN = auto()

class Position(Enum):
    SMALL_BLIND = auto()
    BIG_BLIND = auto()
    DEALER = auto()
    BASIC = auto()

class Player:
    def __init__(self, money, name=names.get_full_name()):
        """
        Initializes a new instance of the Player class.

        :param name: A string representing the name of the player.
        :param money: An integer representing the amount of money the player has.

        This method initializes a new instance of the Player class. It sets the initial values for the instance variables `name`, `cards`, `money`, `status`, and `current_bet`.

        Parameters:
            name (str): The name of the player.
            money (int): The amount of money the player has.

        Returns:
            None
        """
        self._name = name
        self._cards = []
        self._money = money
        self._status = Status.ACTIVE
        self._current_bet = 0
        self.position = Position.BASIC

    @property
    def name(self):
        return self._name

    @property
    def cards(self):
        return self._cards
    
    @cards.setter
    def cards(self, cards):
        self._cards = cards

    @property
    def money(self):
        return self._money

    @money.setter
    def money(self, amount):
        self._money = amount

    @property
    def status(self):
        return self._status

    @property
    def current_bet(self):
        return self._current_bet

    @current_bet.setter
    def current_bet(self, amount):
        self._current_bet = amount

    def fold(self):
        """
        Sets the status of the player to FOLDED.

        This function sets the `status` attribute of the `Player` object to `Status.FOLDED`.

        Parameters:
            None

        Returns:
            None
        """
        self.status = Status.FOLDED

    def call(self, amount):
        """
        Decreases the player's money by the given amount and increases their current bet by the same amount.

        Parameters:
            amount (int): The amount of money to call.

        Raises:
            None.

        Returns:
            None.
        """
        if amount > self.money:
            self.go_all_in()
        else:
            self.money -= amount
            self.current_bet += amount

    def bet(self, amount):
        """
        Decreases the player's money by the given amount and increases their current bet by the same amount.

        Parameters:
            amount (int): The amount of money to bet.

        Raises:
            ValueError: If the amount of money to bet is greater than the player's current money.

        Returns:
            None
        """
        if amount > self.money:
            raise ValueError("Cannot bet more money than the player has")
        self._money -= amount
        self._current_bet += amount

    def go_all_in(self):
        """
        Sets the player's current bet to their entire balance and sets their status to ALL_IN.

        This function increases the player's current bet by their entire balance and sets their money balance to 0.
        It also sets their status to Status.ALL_IN, indicating that the player has gone all-in.

        Parameters:
            None

        Returns:
            None
        """
        self.current_bet += self.money
        self.money = 0
        self.status = Status.ALL_IN

