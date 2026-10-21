from abc import ABC, abstractmethod

class NotificationService(ABC):
    @abstractmethod
    def send(self, to: str, title: str, body: str):
        pass

class EmailNotificationService(NotificationService):
    def send(self, to:str, title: str, body: str):
        print(f"Sending Email to {to}")
        print(f"Title: {title}")
        print(f"Body: {body}")

class SendGridEmailService:
    def send_email(self, recipient: str, subject:str, content: str):
        print(f"Sending Email via SendGrid to {recipient}")
        print(f"Subject: {subject}")
        print(f"Content: {content}")

class SendGridEmailAdapter(NotificationService):
    def __init__(self, send_grid_service: SendGridEmailService):
        self.send_grid_service=send_grid_service

    def send(self, to: str, title: str, body: str):
        self.send_grid_service.send_email(to, title, body)

class OrderService:
    def __init__(self, email_service: NotificationService):
        self.__email_service=email_service

    def create_order(self):
        self.__email_service.send("parth@gmail.com", "New order", "Order has been placed")

# ens=EmailNotificationService()
# os=OrderService(ens)
# os.create_order()

sgs=SendGridEmailService()
sga=SendGridEmailAdapter(sgs)
os=OrderService(sga)
os.create_order()