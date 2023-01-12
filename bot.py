import os
import discord
import asyncio
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')

@client.event
async def on_message(message):
    channel = message.channel
    user = message.author

    if message.content.startswith('!pstart'):
        pass


client.run(os.getenv('TOKEN'))