from collections import deque

from tic_tac_toe.board.boards import Board
from tic_tac_toe.players.players import Players
from tic_tac_toe.symbol.symbol_enum import SymbolType
from tic_tac_toe.symbol.symbol_x import SymbolX
from tic_tac_toe.symbol.symbol_o import SymbolO
from tic_tac_toe.symbol.symbols import Symbol


class Game:
    def __init__(self):

        self.players = deque([])
        # self.symbols = deque([None]*total_players)
        self.board = None

    def initialize_game(self):
        piece_x = SymbolX()
        piece_o = SymbolO()
        name1 = input('please enter 1st players name')
        player1 = Players(name1, piece_x)
        print(f'player {name1} added successfully with piece {piece_x.symbol.value}')
        name2 = input('please  enter 2nd players name')
        player2 = Players(name2, piece_o)
        print(f'player {name2} added successfully with piece {piece_o.symbol.value}')
        self.players.append(player1)
        self.players.append(player2)
        board_size = input('please provide board size')
        self.board = Board(int(board_size))

    # def add_players(self):
    #     print(f'please enter {self.total_players} players details')
    #     i = 0
    #     while i < self.total_players:
    #         name = input('please enter players name')
    #         user_id = input('provide user name')
    #         player = Players()
    #         player.create_player(name, user_id)
    #         if self.is_player_already_exist(player):
    #             print('player already exist please provide another player')
    #             continue
    #         else:
    #             self.players.appendleft([player, None])
    #             print(f'player {i + 1} added successfully')
    #             i += 1
    #     print('all players added successfully')

    # def is_player_already_exist(self, player):
    #     for p in self.players:
    #         if p[0].name == player.name:
    #             return True
    #     return False
    #
    # def is_symbol_already_exist(self, symbol):
    #     for s in self.players:
    #         if s[1] == symbol:
    #             return True
    #     return False

    def start_game(self):
        no_winner = True
        while no_winner:
            p_move = self.players.pop()
            print(f"player name {p_move.name} it's your turn")
            print('please select your move from available space')
            self.print_board()
            x_cor = int(input('please provide x co-ordinate'))
            y_cor = int(input('please provide y co-ordinate'))
            is_valid = self.board.is_valid_move(x_cor, y_cor)
            if not is_valid:
                print('this is not a valid move please select a valid move')
                self.players.append(p_move)
                continue
            else:
                self.board.add_piece(x_cor, y_cor, p_move.symbol)

            if self.is_winner(x_cor, y_cor):
                print(f'player {p_move.name} Won the game')
                no_winner = False
            elif not self.board.is_space_available():
                print('No space available game draw')
                return True
            else:
                self.players.appendleft(p_move)
                print('move update next players turn')

    def is_winner(self, row, col):
        r_d = False
        l_d = False
        if self.is_right_diagonal(row, col):
            r_d = self.board.match_right_diagonal()
        if self.is_left_diagonal(row, col):
            l_d = self.board.match_left_diagonal()
        r = self.board.match_row(row)
        c = self.board.match_col(col)
        if r_d or l_d or r or c:
            return True

    def is_left_diagonal(self, row, col):
        if row == col:
            return True
        return False

    def is_right_diagonal(self, row, col):
        n = self.board.board_size
        if col == n - row - 1:
            return True
        return False

    def print_board(self):
        n = self.board.board_size
        for i in range(-1, n):
            if i == -1:
                print(' ', end=" ")
            else:
                print(i, end=" ")
        print()
        for i in range(n):
            print(i, end=" ")
            for j in range(n):
                print(self.board.board[i][j].symbol.value if self.board.board[i][j] else '-', end=" ")
            print()
