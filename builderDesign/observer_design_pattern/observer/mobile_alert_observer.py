from observer_design_pattern.observer.observer_interface import ObserverInterface


def _send_msg_on_mobile(username, subject, body):
    print(f'msg sent to {username}')


class MobileObserver(ObserverInterface):
    def __init__(self, email_id, observable):
        self.username = email_id
        self.observable = observable

    def update(self):
        _send_msg_on_mobile(self.username, 'stock update', "product is in stock hurry up!")

