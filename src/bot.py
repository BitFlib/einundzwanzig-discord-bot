import os
from dotenv import load_dotenv
import discord

load_dotenv()

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user: 
        return
    
    print(f'Received message: {message.content}')
    await message.channel.send(message.content)

client.run(os.getenv('DISCORD_TOKEN'))