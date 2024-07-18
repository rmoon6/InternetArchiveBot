import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from url_archive_utils import get_latest_archive_url

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print(f'NewsBot logged in as {client.user}')

@client.command()
async def archive(ctx, url: str):
    await ctx.send(get_latest_archive_url(url))

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Command not found.")
    else:
        raise error

def get_bot_token() -> str:
    return os.getenv('DISCORD_BOT_TOKEN')

client.run(get_bot_token())
