from abc import ABC, abstractmethod
class payment(ABC):
    def display(a):
        print(a)
    @abstractmethod
    def payment_choice(self,amount):
        pass
class card(payment):
    def payment_choice(self,amount):
        print('Payment choice: Card. Payment amount:',amount)
class cash(payment):
    def payment_choice(self,amount):
        print('Payment choice: Cash. Payment amount:',amount)        
obj=card()
obj1=cash()
obj.payment_choice(1236)
obj1.payment_choice(1236)
        
        
