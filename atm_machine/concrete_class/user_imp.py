from interface.user import UserInterFace
from concrete_class.bank_account import BankAccountImp
class UserImp(UserInterFace):
    def __init__(self):
        self.username = None
        # self.user_id = None
        self.dob = None
        self.gender = None
        self.identity = None
        self.phone = None
        self.email = None
        self.password = None

    def create_user(self, username, password, dob, gender, identity, phone, email):
        self.username = username
        self.phone = phone
        self.password = password
        self.gender = gender
        self.identity = identity
        self.dob = dob
        self.email = email
        # self.generate_user_id()

    def get_user_details(self):
        return self

    def apply_for_bank_account(self):
        bank_account = BankAccountImp()
        bank_account.create_bank_account(self.username, self.password, self.identity, self.dob, self.gender)


    def apply_for_debit_card(self):
        pass

    def show_bank_balance(self):
        pass

    def deposit_money(self):
        pass

    def withdraw_money(self):
        pass

    def transfer_money(self):
        pass
