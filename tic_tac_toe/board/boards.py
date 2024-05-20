class Board:
    def __init__(self, n):
        self.board_size = n
        self.board = [[None for _ in range(n)] for _ in range(n)]

    def is_valid_move(self, i, j):
        if self.board[i][j] is None:
            return True
        return False

    def match_left_diagonal(self):
        n = self.board_size
        sym = self.board[0][0]
        for i in range(1, n):
            for j in range(1, n):
                if self.board[i][j] != sym:
                    return False
        return True

    def match_right_diagonal(self):
        n = self.board_size
        sym = self.board[0][n - 1]
        for i in range(1, n):
            for j in range(n - 2, -1, -1):
                if self.board[i][j] != sym:
                    return False
        return True

    def match_row(self, i):
        n = self.board_size
        sym = self.board[i][0]
        for j in range(1, n):
            if self.board[i][j] != sym:
                return False
        return True

    def match_col(self, j):
        n = self.board_size
        sym = self.board[0][j]
        for i in range(1, n):
            if self.board[i][j] != sym:
                return False
        return True

    def is_space_available(self):
        n = self.board_size
        for i in range(n):
            for j in range(n):
                if self.board[i][j] is None:
                    return True
        return False

    def add_piece(self, row, col, symbol):
        self.board[row][col] = symbol
