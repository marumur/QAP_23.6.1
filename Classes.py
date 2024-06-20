import requests
import json
from config import keys

class Calculator:
   def multiply(self, x, y):
       return x * y

   def division(self, x, y):
       return x / y

   def subtraction(self, x, y):
       return x - y

   def adding(self, x, y):
       return x + y
class ConvertionException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str ):

        if quote == base:
            raise ConvertionException(f'Нельзя конвертировать одинаковые валюты {base}!')
    
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {quote}!')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base}!')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество {amount}!')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]] * amount


        return total_base
