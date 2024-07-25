from player import Player
from table import Table

class Round:
    def __init__(self,player_count=7,buyin=200,small_blind=2):
        self.small_blind = small_blind
        self.big_blind = small_blind*2
        self._dealer_num = 0

        self.table = Table()

        self._user_player = Player(buyin,"Player")
        players = [Player(buyin) for _ in range(player_count)]
        
        self.table.players.add_player(self._user_player)
        for player in players:
            self.table.add_player(player)
        
    def start_round(self):
        # Shuffle deck
        self.table.shuffle_deck()
        # Dealer, BB, SB
        self.table.players[self._dealer_num%len(self.table.players)].position = Player.Position.DEALER
        self.table.players[(self._dealer_num+1)%len(self.table.players)].position = Player.Position.SMALL_BLIND
        self.table.players[(self._dealer_num+2)%len(self.table.players)].position = Player.Position.BIG_BLIND
        # Deal cards
        self.table.deal_to_all()
        # dealer+3 (UTG) starts betting
        # continues until the round reaches the last person who bet

        # flop
        # dealer+1 (SB) starts betting
        # continues until the round reaches the last person who bet

        # turn
        # dealer+1 (SB) starts betting
        # continues until the round reaches the last person who bet

        # river
        # dealer+1 (SB) starts betting
        # continues until the round reaches the last person who bet

        # showdown
        # winner gets calculated
        # round is over
        