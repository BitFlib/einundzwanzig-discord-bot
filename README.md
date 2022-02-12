# Einundzwanzig Discord Bot
Discord bot for bitcoin plebs. 

Contains functionality for converting currencies to sats and vice versa, receiving usefull bitcoin related values like moscow time or block time, and einundzwanzig podcast related stuff like returning the newest episode.

## How to run this bot locally on your maschine:
1. create file `.env` in the root directory of this project. Its content should look like this:
```
DISCORD_TOKEN=YOUR_SECRET_DISCORD_TOKEN
```


| :point_up:    | Make sure to replace `YOUR_SECRET_DISCORD_TOKEN` with your own DISCORD_TOKEN you received at [Discord Developer Console](https://canary.discord.com/developers/applications) |
|---------------|:------------------------|

2. Add the bot to your channel

3. execute `make run` to install all dependencies and run the bot

## Commands
- `!moskauzeit` (or short `!mz`): Returns the amount of sats you would receive for 1 USD also known as moscow time and the counterpart for EUR and CHF
- `!preis`: Returns the current price for 1 BTC in USD, EUR and CHF
