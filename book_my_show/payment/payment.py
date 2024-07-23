class Payment:
    def __init__(self):
        self.payment_id = None
        self.payment_status = None
        self.total_bill = None
        self.payment_mode = None

    def get_payment_id(self):
        return self.payment_id

    def get_payment_status(self):
        return self.payment_status

    def get_total_bill(self):
        return self.total_bill

    def get_payment_mode(self):
        return self.payment_mode

    def set_payment_id(self, payment_id):
        self.payment_id = payment_id

    def set_payment_status(self, payment_status):
        self.payment_status = payment_status

    def set_total_bill(self, total_bill):
        self.total_bill = total_bill

    def set_payment_mode(self, payment_mode):
        self.payment_mode = payment_mode
