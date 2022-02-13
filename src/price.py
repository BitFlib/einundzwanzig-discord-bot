import requests

def __get_exchange_rates():
    try:
        r = requests.get('https://api.coinbase.com/v2/exchange-rates?currency=BTC', timeout=5)
        price_rates = r.json()['data']['rates']
        return price_rates
    except requests.exceptions.RequestException as e:  
        print(e)
        return -1

def __us_to_de_float(us_float, target_precision):
    float_format = '{:,.' + str(target_precision) + 'f}'
    us_float = float_format.format(float(us_float))
    de_float = us_float.replace(',','#')
    de_float = de_float.replace('.',',')
    de_float = de_float.replace('#','.')
    return de_float

def __de_to_us_float(de_float, target_precision):
    float_format = '{:.' + str(target_precision) + 'f}'
    us_float = de_float.replace(',','.')
    us_float = float_format.format(float(us_float))
    return float(us_float)

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
        amount_sats = __us_to_de_float(amount_sats,0)
        amount_fiat = __us_to_de_float(amount_fiat,2)
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
        price_usd = __us_to_de_float(exchange_rates['USD'],2)
        response += f'\n\t{price_usd} USD/BTC'
        price_eur = __us_to_de_float(exchange_rates['EUR'],2)
        response += f'\n\t{price_eur} EUR/BTC'
        price_chf = __us_to_de_float(exchange_rates['CHF'],2)
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
            amount_fiat = message.content.split(' ')[2]
            amount_fiat = __de_to_us_float(amount_fiat,2)
        except:
            await message.reply('Fehlerhafte Eingabe. \nBeispielaufruf: !sats eur 100')
            return
        amount_sats = __us_to_de_float(amount_fiat/float(exchange_rates[currency]) * 100000000,0)
        amount_fiat = __us_to_de_float(amount_fiat,2)
        response = f'{amount_fiat} {currency} sind aktuell {amount_sats} sats.'
    else:
        response = 'Ein Fehler ist aufgetreten. \nBitte versuche es spaeter erneut.'
    await message.reply(response)
