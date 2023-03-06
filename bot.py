import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

client = commands.Bot(command_prefix='$')

load_dotenv()


@client.event
async def on_ready():
    print('we have logged in as {0.user}'.format(client))

@client.command()
async def ping():
    await client.say('pong')

@client.event
async def on_message(message):
    if client.user.id != message.author.id:
        if 'test' in message.content:
            await client.send_message(message.channel, 'testing')

    await client.process_commands(message)

client.run(os.getenv('TOKEN'))