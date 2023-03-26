class Message:
    def __init__(self, sender, receiver, message):
        self.sender = sender
        self.receiver = receiver
        self.message = message

class MessagingSystem:
    def __init__(self):
        self.messages = []

    def send_message(self, sender, receiver, message):
        new_message = Message(sender, receiver, message)
        self.messages.append(new_message)

    def view_messages(self, receiver):
        receiver_messages = [msg for msg in self.messages if msg.receiver == receiver]
        return receiver_messages

# Example usage:
messaging_system = MessagingSystem()
messaging_system.send_message("Alice", "Bob", "Hey Bob, how's it going?")
messaging_system.send_message("Bob", "Alice", "Not bad, thanks! How about you?")
messaging_system.send_message("Alice", "Bob", "I'm doing pretty well too, thanks!")
print(messaging_system.view_messages("Bob")) # Output: [Message(sender='Alice', receiver='Bob', message="Hey Bob, how's it going?"), Message(sender='Alice', receiver='Bob', message='I'm doing pretty well too, thanks!')]
