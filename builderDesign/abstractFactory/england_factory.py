from abstractFactory.capital_city import CapitalCity
from abstractFactory.language import Language
from international_factory import InternationalFactory
from english import English
from london import London

#Concrete Factory 1


class EnglandFactory(InternationalFactory):
    def create_language(self) -> Language:
        return English()

    def create_capital(self) -> CapitalCity:
        return London()
