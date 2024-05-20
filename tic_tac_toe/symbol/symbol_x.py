from tic_tac_toe.symbol.symbol_enum import SymbolType
from tic_tac_toe.symbol.symbols import Symbol


class SymbolX(Symbol):
    def __init__(self):
        super().__init__(SymbolType.SYMBOL_X)
