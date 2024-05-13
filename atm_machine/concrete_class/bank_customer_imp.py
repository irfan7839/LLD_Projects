from interface.bank_custmers import BankCustomersInterface

class BankCustomerImp(BankCustomersInterface):

    def __init__(self):
        self.user_with_account = []
        self.total_customer = 0

    def add_bank_customer(self, bank_account):
        self.user_with_account.append(bank_account)
        self.total_customer += 1

    def get_bank_customer_from_card(self, card_details):
        for account in self.user_with_account:
            for card in account:
                if card.card_number == card_details:
                    return account
        print("No account found")
        return
    def get_bank_customer(self, user):
        for account in self.user_with_account:
            if user == account.user:
                return account
        print("No account found")

    def verify_card_details(self,account,pin_code):
        card = account.card[0]
        if card.verify_expiry() and card.pin_code == pin_code:
            return True
        return False
