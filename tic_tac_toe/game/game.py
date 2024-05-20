from collections import deque

from tic_tac_toe.players.players import Players
from tic_tac_toe.symbol.symbols import Symbol


class Game:
    def __init__(self, total_players, board_size):
        self.total_players = total_players
        self.board_size = board_size

        self.players = deque([None]*total_players)
        self.symbols = deque([None]*total_players)
        self.board = None

    def add_players(self, name, user_id, gender):
        print(f'please enter {self.total_players} players details')
        i = 0
        while i < self.total_players:
            name = input('please enter players name')
            user_id = input('provide user name')
            gender = input('provide gender')
            player = Players()
            player.create_player(name, user_id, gender)
            if self.is_player_already_exist(player):
                print('player already exist please provide another player')
                continue
            else:
                self.players.appendleft(player)
                print(f'player {i+1} added successfully')
                i += 1
        print('all players added successfully')

    def add_symbols(self, symbol):
        print(f'please enter {self.total_players} symbols')
        i = 0
        while i < self.total_players:
            symbol_char = input('please enter symbol')
            upper_char = symbol_char.upper()
            symbol = Symbol()
            symbol.add_symbol(upper_char)
            if self.is_symbol_already_exist(symbol):
                print('symbol already exist please provide another symbol')
                continue
            else:
                self.symbols.appendleft(symbol)
                print(f'symbol {i+1} added successfully')
                i += 1

            print(f'player {i + 1} added successfully')
        print('all players added successfully')




    def is_player_already_exist(self,player):
        for p in self.players:
            if p.user_id == player.user_id:
                return True
        return False

    def is_symbol_already_exist(self,symbol):
        for s in self.symbols:
            if s.symbol == symbol.symbol:
                return True
        return False
