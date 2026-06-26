# SOLID Priciples concepts
from abc import ABC, abstractmethod

class Notification(ABC):
    
    #notification of event
    @abstractmethod
    def send(self, recipent , message):
        pass


class EmailServices(Notification):
    def send(self,email, body):
        # email services
        print(f"Hello  {email} and body {body}")
        

class SMSService(Notification):
    def send(self,recipent,message):
        # SMS services
        print(f"Hi... {recipent}  and message {message}")
        
def notify_user(notification : Notification , recipent , message):
    notification.send(recipent,message)
        
        
email_n = EmailServices()
email_n.send('suvit@mail.com', 'Helll')


notify_user(EmailServices() , 'myemialname', 'name')
notify_user(SMSService() , 33441122, 'Message')
    
