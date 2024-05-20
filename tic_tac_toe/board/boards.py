class Board:
    def __init__(self):
        self.size = 0
        self.board = [[]]

    def create_board(self, n):
        self.size = n
        self.board = [["" for _ in range(n)] for _ in range(n)]

