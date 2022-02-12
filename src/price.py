import requests

def __get_exchange_rates():
    try:
        r = requests.get('https://api.coinbase.com/v2/exchange-rates?currency=BTC', timeout=5)
        price_rates = r.json()['data']['rates']
        return price_rates
    except requests.exceptions.RequestException as e:  
        print(e)
        return -1

async def moscow_time(message):
    exchange_rates = __get_exchange_rates()
    if exchange_rates != -1:
        response = 'Moskau Zeit:'
        price_usd = float(exchange_rates['USD'])
        mt_usd = int(1/price_usd * 100000000)
        response += f'\n\t{mt_usd} sats/USD'
        price_eur = float(exchange_rates['EUR'])
        mt_eur = int(1/price_eur * 100000000)
        response += f'\n\t{mt_eur} sats/EUR'
        price_chf = float(exchange_rates['CHF'])
        mt_chf = int(1/price_chf * 100000000)
        response += f'\n\t{mt_chf} sats/CHF'
    else:
        response = 'Ein Fehler ist aufgetreten. Bitte versuche es spaeter erneut.'
    await message.channel.send(response)


async def price(message):
    exchange_rates = __get_exchange_rates()
    if exchange_rates != -1:
        response = 'Aktueller Preis:'
        price_usd = '{:,.2f}'.format(float(exchange_rates['USD']))
        response += f'\n\t{price_usd} USD/BTC'
        price_eur = '{:,.2f}'.format(float(exchange_rates['EUR']))
        response += f'\n\t{price_eur} EUR/BTC'
        price_chf = '{:,.2f}'.format(float(exchange_rates['CHF']))
        response += f'\n\t{price_chf} CHF/BTC'
    else:
        response = 'Ein Fehler ist aufgetreten. Bitte versuche es spaeter erneut.'
    await message.channel.send(response)
