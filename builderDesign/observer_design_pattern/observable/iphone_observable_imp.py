from observer_design_pattern.observable.stocks_observable import StockObservable


class IphoneObservableImp(StockObservable):
    def __init__(self):
        self.observer_list = []
        self.stock_count = 0

    def add(self, notify_observer):
        self.observer_list.append(notify_observer)

    def remove(self, notify_observer):
        self.observer_list.remove(notify_observer)

    def notify_subscribers(self):
        for observer in self.observer_list:
            observer.update()

    def set_stock_count(self, new_stock_added):
        if self.stock_count == 0:
            self.notify_subscribers()
        self.stock_count += new_stock_added

    def get_stock_count(self):
        return self.stock_count
