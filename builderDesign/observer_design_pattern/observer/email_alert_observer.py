from observer_design_pattern.observer.observer_interface import ObserverInterface


def _send_mail(email, subject, body):
    print(f'msg sent to {email}')


class EmailObserver(ObserverInterface):
    def __init__(self, email_id, observable):
        self.email = email_id
        self.observable = observable

    def update(self):
        _send_mail(self.email, 'stock update', "product is in stock hurry up!")

