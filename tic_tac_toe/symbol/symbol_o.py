from tic_tac_toe.symbol.symbol_enum import SymbolType
from tic_tac_toe.symbol.symbols import Symbol


class SymbolO(Symbol):
    def __init__(self):
        super().__init__(SymbolType.SYMBOL_O)
