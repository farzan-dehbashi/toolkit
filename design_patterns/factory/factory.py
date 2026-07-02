from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass


class EmailNotification(Notification):
    def send(self, message):
        print(f"Email: {message}")


class SMSNotification(Notification):
    def send(self, message):
        print(f"SMS: {message}")


class PushNotification(Notification):
    def send(self, message):
        print(f"Push: {message}")


def notification_factory(channel):
    channels = {
        "email": EmailNotification,
        "sms": SMSNotification,
        "push": PushNotification,
    }
    if channel not in channels:
        raise ValueError(f"Unknown channel: {channel}")
    return channels[channel]()


if __name__ == "__main__":
    for channel in ["email", "sms", "push"]:
        notification_factory(channel).send("Hello!")
