from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def notify(self, message):
        pass


# class Email(Notification):
#     def notify(self, message, email):
#         print(f'Send {message} to {email}')
#
#
# class Sms(Notification):
#     def notify(self, message, phone):
#         print(f'Send {message} to {phone}')

class Email(Notification):
    def __init__(self, email):
        self.email = email

    def notify(self, message):
        print(f'Send {message} to {self.email}')


class Sms(Notification):
    def __init__(self, phone):
        self.phone = phone

    def notify(self, message):
        print(f'Send {message} to {self.phone}')


class Contact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone


# class NotificationManager:
#     def __init__(self, notification, contact):
#         self.notification = notification
#         self.contact = contact
#
#     def send(self, message):
#         if isinstance(self.notification, Email):
#             self.notification.notify(message, self.contact.email)
#         elif isinstance(self.notification, Sms):
#             self.notification.notify(message, self.contact.phone)

class NotificationManager:
    def __init__(self, notification):
        self.notification = notification

    def send(self, message):
        self.notification.notify(message)


if __name__ == '__main__':
    ct = Contact('Hello', 'john@test.com', '12345')
    notification_manager = NotificationManager(Email(ct.email))
    notification_manager.send("Hello")

    notification_manager = NotificationManager(Sms(ct.phone))
    notification_manager.send("Hello")

    # notification_manager = NotificationManager(Email(), ct)
    # notification_manager.send('hello')

    # notification_manager = NotificationManager(Sms(), ct)
    # notification_manager.send('hello')
    pass
    # notification = Sms()
    # notification.notify('Hello', 'john@test.com')
