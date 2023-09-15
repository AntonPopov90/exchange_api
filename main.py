from fastapi import FastAPI
from exchange_rate import get_exchange_values
app = FastAPI()


@app.get('/')
def greeting():
    return {'message': 'Hi, for documentation'
            ' please visit localhost:8000/docs/'}


@app.get('/api/rates/')
def exchange_result(from_, to, value):
    """
    Exchange route:

    **Please write currency name rightly with uppercase. Example: USD, EUR**

    -**from** : currency from which you want convert

    -**to** : currency to which you want to convert

    -**value** : amount of currency

    """
    result = get_exchange_values(currency_from=from_,
                                 currency_to=to,
                                 value=value)
    return {'result': result}
