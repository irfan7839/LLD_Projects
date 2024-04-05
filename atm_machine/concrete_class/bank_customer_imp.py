from interface.bank_custmers import BankCustomersInterface

class BankCustomerImp(BankCustomersInterface):

    def __init__(self):
        self.user_with_account = []
        self.total_customer = 0
