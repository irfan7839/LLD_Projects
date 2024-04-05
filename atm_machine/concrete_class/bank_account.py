from interface.bank_account import BankAccountInterface


class BankAccountImp(BankAccountInterface):

    def __init__(self):
        self.user = None
        self.balance = 0
        self.account_type = None
        # self.branch = None
        # self.IFSC = None
        self.cards = []

    def create_bank_account(self, user, account_type):
        self.user = user
        self.account_type = account_type

    def deposit_money(self, amount):
        self.balance += amount
        return self.balance

    def withdrawal_money(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print('Insufficient Fund')

    def get_account_balance(self, card):
        return self.balance

    def add_card(self, card):
        self.cards.append(card)

    def remove_card(self, card):
        self.cards.remove(card)

    def find_card(self, card_type):
        for card in self.cards:
            if card.card_type == card_type:
                print(f'Card of type {card_type} already exist.')
                return True
        return False

    def get_card_details(self, card_type):
        for card in self.cards:
            if card.card_type == card_type:
                return card
        print('None Card Found')
        return False

