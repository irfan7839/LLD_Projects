class Players:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def create_player(self, name, symbol):
        self.name = name
        self.symbol = symbol
        print("User created successfully")
