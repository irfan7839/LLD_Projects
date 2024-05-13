from concrete_class.card_imp import CardImp
from interface.user import UserInterFace
from concrete_class.bank_account import BankAccountImp
from concrete_class.bank_customer_imp import BankCustomerImp

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

    def create_user(self):
        username = input("Provide username for account")
        password = input("Provide password for account")
        dob = input("Provide your date of birth")
        gen = ['m', 'f']

        while True:
            gender = input("please select m for male and f for female")
            if gender not in gen:
                continue
            else:
                break
        identity = input("Provide identity card number for account")
        phone = input("Provide your phone number")
        email = input("Provide email for account")

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

    def apply_for_bank_account(self, account_type, bank):
        bank_account = BankAccountImp()
        bank_account.create_bank_account(self, account_type)
        bank.add_bank_customer(bank_account)
        print("Your bank account created successfully")


    def apply_for_debit_card(self, card_type, bank):
        card = CardImp()
        card.create_card(card_type, self.username, self)
        bank_account = self.get_bank_account(bank)
        bank_account.add_card(card)
        card_details = card.get_card_details()
        print('Your card created successfully ')
        return card_details


    def show_bank_balance(self, bank_customer):
        account = self.get_bank_account(bank_customer)
        print(f'Available Balance Rs. {account.balance}')
        return account.balance

        pass

    def deposit_money(self, bank_customer):
        account = self.get_bank_account(bank_customer)
        money = account.deposit_money()
        print(f'{money} deposited successfully')


    def withdraw_money(self, bank_customer):

        account = self.get_bank_account(bank_customer)
        account.withdrawal_money()
        pass

    def transfer_money(self):
        pass

    def get_bank_account(self, bank_customer):
        bank_account = bank_customer.get_bank_customer(self)
        return bank_account
