from concrete_class.user_imp import UserImp
from concrete_class.bank_account import BankAccountImp
from concrete_class.bank_customer_imp import BankCustomerImp


class SelectTransactionOption:
    @staticmethod
    def select_transaction_type(bank, user):
        transaction = ['1', '2', '3', '4']
        while True:
            value = input('please select\n 1. for show balance \n 2. for deposit_money\n 3. for withdraw money\n  4. '
                          'Exit')
            if value not in transaction:
                print('please select correct option')
            elif value == '4':
                return
            else:
                if value == '1':
                    user.show_bank_balance(bank)
                elif value == '2':
                    user.deposit_money(bank)
                elif value == '3':
                    user.withdraw_money(bank)
    @staticmethod
    def select_card_transaction_type(bank, card_number):
        transaction = ['1', '2', '3', '4']
        account = bank.get_bank_customer_from_card(card_number)
        if not card:
            print("Card Not Valid")
            return
        i = 0
        while i < 3:
            pin_code = input('enter pin for card')
            if bank.verify_card_details(account,pin_code):

                while True:
                    value = input('please select\n 1. for show balance \n 2. for deposit_money\n 3. for withdraw money\n  4. '
                                  'Exit')
                    if value not in transaction:
                        print('please select correct option')
                    elif value == '4':
                        return
                    else:
                        if value == '1':
                            account.get_account_balance()
                        elif value == '2':
                            account.deposit_money()
                        elif value == '3':
                            account.withdraw_money()
            else:
                print(f'wrong pin {2 - i} attempt left')
                continue
        print("Due to multiple wrong attempt your card get blocked for 24 hrs"
              ""
              ""
              "")

if __name__ == '__main__':
    bank = BankCustomerImp()
    user1 = UserImp()
    user1.create_user()
    user1.apply_for_bank_account('saving', bank)
    card = user1.apply_for_debit_card('visa', bank)

    SelectTransactionOption.select_transaction_type(bank, user1)
