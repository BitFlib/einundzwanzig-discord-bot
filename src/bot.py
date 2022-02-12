import os
from dotenv import load_dotenv
import discord
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
        Returns the amount of sats you would receive
        for 1 USD also known as moscow time and the 
        counterpart for EUR and CHF
        '''
        await price.moscow_time(message)
        return

    if msg.startswith('!preis'):
        '''
        Returns the current price for 1 BTC in USD, EUR and CHF
        '''
        await price.price(message)
        return

    '''
    #############
    Default below
    #############
    '''

    print(f'Received message: {message.content}')
    await message.channel.send(message.content)

client.run(os.getenv('DISCORD_TOKEN'))
