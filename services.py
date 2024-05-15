import requests
from config import Config
from utils import log_error


class CurrencyConverter:
    @staticmethod
    def get_rates(currency):
        try:
            response = requests.get(Config.API_URL.format(currency=currency))
            response.raise_for_status()
            return response.json()['rates']
        except requests.RequestException as e:
            log_error(f'Не удалось получить данные курса валют: {str(e)}')
            return None

    @staticmethod
    def convert(from_currency, to_currency, amount):
        rates = CurrencyConverter.get_rates(from_currency)
        if rates is None:
            return None, 'Ошибка API или недопустимая валюта, из которой нужно конвертировать'

        rate = rates.get(to_currency)
        if rate is None:
            return None, 'Недопустимая валюта, в которую нужно конвертировать'

        return round(rate * amount, 2), None
