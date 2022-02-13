import requests

def __get_exchange_rates():
    try:
        r = requests.get('https://api.coinbase.com/v2/exchange-rates?currency=BTC', timeout=5)
        price_rates = r.json()['data']['rates']
        return price_rates
    except requests.exceptions.RequestException as e:  
        print(e)
        return -1

async def fiat(message):
    exchange_rates = __get_exchange_rates()
    if exchange_rates != -1:
        try:
            currency = str(message.content[1:4].upper())
            amount_sats = int(message.content.split(' ')[1])
        except:
            await message.reply('Fehlerhafte Eingabe. \nBeispielaufruf: !eur 100')
            return
        exchange_rate_fiat = float(exchange_rates[currency])
        amount_fiat = float(exchange_rate_fiat / 100000000 * amount_sats)
        amount_sats = '{:,.0f}'.format(amount_sats)
        amount_fiat = '{:,.2f}'.format(amount_fiat)
        response = f'{amount_sats} sats sind aktuell {amount_fiat} {currency}'
    else:
        response = 'Ein Fehler ist aufgetreten. \nBitte versuche es spaeter erneut.'
    await message.reply(response)

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
        response = 'Ein Fehler ist aufgetreten. \nBitte versuche es spaeter erneut.'
    await message.reply(response)


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
        response = 'Ein Fehler ist aufgetreten. \nBitte versuche es spaeter erneut.'
    await message.reply(response)

async def sats(message):
    exchange_rates = __get_exchange_rates()
    if exchange_rates != -1:
        try:
            currency = str(message.content.split(' ')[1])
            if(currency.lower() == 'eur') or (currency.lower() == 'chf') or (currency.lower() == 'usd'):
                currency = currency.upper()
            else:
                raise ValueError()
            amount_fiat = float(message.content.split(' ')[2])
        except:
            await message.reply('Fehlerhafte Eingabe. \nBeispielaufruf: !sats eur 100')
            return
        amount_sats = '{:,.0f}'.format(amount_fiat/float(exchange_rates[currency]) * 100000000)
        amount_fiat = '{:,.2f}'.format(amount_fiat)
        response = f'{amount_fiat} {currency} sind aktuell {amount_sats} sats.'
    else:
        response = 'Ein Fehler ist aufgetreten. \nBitte versuche es spaeter erneut.'
    await message.reply(response)
