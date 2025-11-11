from subscriber import Subscriber

class Subscriber1(Subscriber):
    def __init__(self, name):
        self.name = name

    def on_message(self, message):
        print(f"Subscriber {self.name} received message: {message.get_content()}")