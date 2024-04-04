from abc import ABC, abstractmethod


class CardReaderInterface(ABC):

    @abstractmethod
    def get_user_by_card(self, card):
        pass

    @abstractmethod
    def match_card_pin(self, pin):
        pass

    @abstractmethod
    def get_bank_details_by_card(self):
        pass
