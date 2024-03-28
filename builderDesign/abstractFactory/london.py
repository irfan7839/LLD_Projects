from capital_city import CapitalCity

# Concrete ProductB1


class London(CapitalCity):
    def get_population(self) -> int:
        return 8900000

    def list_top_attraction(self) -> []:
        return ["Tower Bridge", "Buckingham Palace", "Big Ben"]
