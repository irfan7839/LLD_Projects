from abc import ABC, abstractmethod


class StockObservable(ABC):
    @abstractmethod
    def add(self, notify_observer):
        pass

    @abstractmethod
    def remove(self, notify_observer):
        pass

    @abstractmethod
    def notify_subscribers(self):
        pass

    @abstractmethod
    def set_stock_count(self, new_stock_added):
        pass

    @abstractmethod
    def get_stock_count(self):
        pass
