from enum import Enum, auto
import random

class Status(Enum):
    ACTIVE = auto()
    FOLDED = auto()
    ALL_IN = auto()

class Player:
    def __init__(self, name, money):
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
        self.name = name
        self.cards = []
        self.money = money
        self.status = Status.ACTIVE
        self.current_bet = 0

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
        self.money -= amount
        self.current_bet += amount

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

