from table import Table
from player import Player

def main():
    table = Table()
    table.shuffle_deck()

    player1 = Player("Alice", 1000)
    player2 = Player("Bob", 1000)

    table.add_player(player1)
    table.add_player(player2)

    table.deal_to_player(player1, 2)
    table.deal_to_player(player2, 2)

    table.deal_community_cards(3)

    player1.bet(50)
    player2.bet(50)
    table.add_to_pot(100)

    print("Community Cards:", table.com_cards)
    print("Pot:", table.pot)
    print("Player 1 Cards:", player1.cards)
    print("Player 1 Money:", player1.money)
    print("Player 1 Status:", player1.status)
    print("Player 1 Current Bet:", player1.current_bet)

    print("Player 2 Cards:", player2.cards)
    print("Player 2 Money:", player2.money)
    print("Player 2 Status:", player2.status)
    print("Player 2 Current Bet:", player2.current_bet)

if __name__ == "__main__":
    main()
