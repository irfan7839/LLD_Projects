from observable.iphone_observable_imp import IphoneObservableImp
from observer.email_alert_observer import EmailObserver
from observer.mobile_alert_observer import MobileObserver


class Store:
    iphone_observable = IphoneObservableImp()
    observer1 = EmailObserver('abc@gmail.com', iphone_observable)
    observer2 = MobileObserver('def@gmail.com', iphone_observable)
    # observer3 = EmailObserver('abc@gmail.com', iphone_observable)
    # observer4 = EmailObserver('abc@gmail.com', iphone_observable)
    iphone_observable.add(observer1)
    iphone_observable.add(observer2)
    # iphone_observable.set_stock_count(0)

    print(iphone_observable.get_stock_count())
    # iphone_observable.notify_subscribers()
