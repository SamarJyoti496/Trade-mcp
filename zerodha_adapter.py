import os
import logging
from kiteconnect import KiteConnect
from broker_interface import BrokerInterface

logging.basicConfig(level=logging.DEBUG)

class ZerodhaAdapter(BrokerInterface):
     def __init__(self, apikey, api_secret):
          self.apikey = apikey
          self.api_secret = api_secret
          self.access_token = os.getenv('ACCESS_TOKEN')
          self.kite = KiteConnect(api_key=self.apikey)
          self.login()

     def login(self):
        try:
          # data = self.kite.generate_session("request_token", api_secret=self.api_secret)
          self.kite.set_access_token(self.access_token)
          profile = self.kite.profile()
          logging.info(f"Successfully connected to Zerodha as {profile['user_name']}.")
        except Exception as e:
            logging.error(f"Zerodha login failed: {e}")
            raise
     
     def place_order(self, symbol, quantity, transaction_type, order_type="MARKET", product="CNC"):
          try:
               order_id = self.kite.place_order(tradingsymbol=symbol,
                                     exchange="NSE",
                                     transaction_type=transaction_type,
                                     quantity=quantity,
                                     order_type= order_type,
                                     variety="amo",
                                     validity="DAY",
                                     product=product)
               logging.info(f"Zerodha Order Placed: ID {order_id}")
               return order_id
          except Exception as err:
               logging.error(f"Zerodha order failed: {err}")
               return None

     def get_holdings(self) -> dict:
     #     print(type(self.kite.holdings()))
          holdings = self.kite.holdings()
          stocks_with_quantity = {}
          print(holdings[0])
          for stock in holdings:
              stocks_with_quantity[stock['tradingsymbol']] = stock["quantity"]
          return stocks_with_quantity