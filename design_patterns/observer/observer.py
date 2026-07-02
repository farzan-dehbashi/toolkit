class EventSystem:
    def __init__(self):
        self._subscribers = {}

    def subscribe(self, event, listener):
        if event not in self._subscribers:
            self._subscribers[event] = []
        self._subscribers[event].append(listener)

    def unsubscribe(self, event, listener):
        if event in self._subscribers:
            self._subscribers[event].remove(listener)

    def notify(self, event, data=None):
        for listener in self._subscribers.get(event, []):
            listener(data)


if __name__ == "__main__":
    events = EventSystem()

    def on_user_login(data):
        print(f"User logged in: {data}")

    def send_welcome_email(data):
        print(f"Sending welcome email to: {data}")

    events.subscribe("login", on_user_login)
    events.subscribe("login", send_welcome_email)
    events.notify("login", "farzan@example.com")
