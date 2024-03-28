from abstractFactory.capital_city import CapitalCity
from abstractFactory.language import Language
from international_factory import InternationalFactory
from spanish import Spanish
from madrid import Madrid


# Concrete Factory 1


class SpainFactory(InternationalFactory):
    def create_language(self) -> Language:
        return Spanish()

    def create_capital(self) -> CapitalCity:
        return Madrid()
