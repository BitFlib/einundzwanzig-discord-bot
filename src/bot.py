import os
from dotenv import load_dotenv
import discord
import mempool
import price

load_dotenv()

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user: 
        return

    msg = message.content.lower()

    '''
    ############################
    Price related commands below
    ############################
    '''
    
    if msg.startswith('!mz') or msg.startswith('!moskauzeit'):
        '''
        Returns the amount of sats you would receive for 1 USD also known as moscow time and the 
        counterpart for EUR and CHF
        parameters: none
        example: !mz
        '''
        await price.moscow_time(message)
        return

    if msg.startswith('!preis'):
        '''
        Returns the current price for 1 BTC in USD, EUR and CHF
        parameters: none
        example: !preis
        '''
        await price.price(message)
        return

    if msg.startswith('!sats'):
        '''
        Returns the amount of sats for a given currency and currency amount
        parameters: [1]: currency, [2]: amount_fiat
        example: !sats eur 420,69
        '''
        await price.sats(message)
        return

    if msg.startswith('!usd') or msg.startswith('!eur') or msg.startswith('!chf'):
        '''
        Returns the amount of given currency (dependend on command) for a given amount of sats
        parameters: [1]: amount_sats
        example: !usd 100000
        '''
        await price.fiat(message)
        return

    '''
    ##############################
    Mempool related commands below
    ##############################
    '''

    if msg.startswith('!bz') or msg.startswith('!blockzeit'):
        '''
        Returns the current height tip of mainnet blockchain (also known as blocktime)
        parameters: none
        example: !bz
        '''
        await mempool.blocktime(message)
        return

client.run(os.getenv('DISCORD_TOKEN'))
