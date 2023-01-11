import os
import discord
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

    if message.content.startswith('!pstart'):
        await channel.send('starting game')

client.run(os.getenv('TOKEN'))