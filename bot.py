import discord
from discord.ext import commands
from properties_utils import get_bot_token

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print(f'NewsBot logged in as {client.user}')

@client.command()
async def hello(ctx):
    print(f'recieved a hello command')
    await ctx.send('Hello, world!')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Command not found.")
    else:
        raise error

client.run(get_bot_token())
