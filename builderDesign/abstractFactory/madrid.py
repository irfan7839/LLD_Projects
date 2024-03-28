from capital_city import CapitalCity


# Concrete ProductB2


class Madrid(CapitalCity):
    def get_population(self) -> int:
        return 3200000

    def list_top_attraction(self) -> []:
        return ["Royal Palace", "Prado Museum", "Retire Park"]
