import requests

async def blocktime(message):
    try:
        block_height_tip = requests.get('https://mempool.space/api/blocks/tip/height', timeout=5)
        block_height_tip = block_height_tip.json()
    except requests.exceptions.RequestException as e:
        print(e)  
        response = 'Ein Fehler ist aufgetreten. Bitte versuche es spaeter erneut.'
        await message.channel.send(response)
        return
    response = f'Blockzeit: {block_height_tip}'
    await message.channel.send(response)
