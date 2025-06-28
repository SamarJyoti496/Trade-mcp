from abc import ABC, abstractmethod

class BrokerInterface(ABC):

     @abstractmethod
     def login(self):
          pass

     @abstractmethod
     def place_order(self, symbol, quantity, ):
          pass

     # @abstractmethod
     # def get_ltp(self, symbol):
     #      pass

     @abstractmethod
     def get_holdings(self):
          pass

     # @abstractmethod
     # def get_positions(self):
     #      pass
     