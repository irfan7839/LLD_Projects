import time
import datetime
import random

from interface.card import CardInterface


class CardImp(CardInterface):

    def __init__(self):
        self.card_type = None
        self.card_number = None
        self.expiry = None
        self.expiry_year = None
        self.expiry_month = None
        self.cvv = None
        self.name_on_card = None
        self.pin_code = None
        self.account = None

    def create_card(self, card_type, name):
        self.card_type = card_type
        self.name_on_card = name
        self.generate_card_number()
        self.generate_cvv()
        self.generate_expiry()

    def generate_card_number(self):
        timestamp = int(time.time() * 1000)

        random_part = random.randint(1000, 9999)

        card_number = str(timestamp) + str(random_part)

        self.card_number = card_number

    def generate_cvv(self):
        cvv = random.randint(100, 999)
        self.cvv = cvv

    def generate_expiry(self):
        current_date = datetime.datetime.now()
        expiry_year = current_date.year + 5
        expiry_month = current_date.month
        if expiry_year > current_date.year:
            expiry_month = random.randint(1, 12)
        else:
            expiry_month = random.randint(current_date.month, 12)

        return '{:02d}/{:02d}'.format(expiry_month, expiry_year % 100)

    def get_card_details(self):
        return self

    def create_pin(self, pin):
        self.pin_code = pin

    def add_account_number(self, account_number):
        self.account = account_number

    def verify_expiry(self):
        current_year = datetime.date.year
        current_month = datetime.date.month
        if self.expiry_year > current_year:
            return False
        elif self.expiry_year == current_year and self.expiry_month <= current_month:
            return False
        return True
