import requests


def get_exchange_values(currency_from: str, currency_to: str, value: float):
    """Get currency values from cbr json and convert it"""
    try:
        value == float(value)
    except ValueError:
        return {'message': 'value is not digit'}
    try:
        data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    except requests.exceptions.ConnectionError:
        return {'message': 'no internet connection'}
    try:
        if currency_to == 'RUB':
            return round(data['Valute'][currency_from]['Value'] * float(value), 2)
        elif currency_from == 'RUB':
            return round(float(value) / data['Valute'][currency_to]['Value'], 4)
        else:
            return (data['Valute'][currency_from]['Value'] *
                    float(value)) // data['Valute'][currency_to]['Value']
    except KeyError:
        return {'message': 'currency not found'}
