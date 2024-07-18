import os
import discord
import urllib
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='!', intents=intents)

def find_latest_archive_timestamp(url):
    cleaned_url = urllib.parse.quote(url, safe='')
    timestamps_url = f'https://web.archive.org/__wb/sparkline?output=json&url={cleaned_url}&collection=web'

    payload = {}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Referer': f'https://web.archive.org/web/*/{url}'
    }

    response = requests.get(timestamps_url, headers=headers, data=payload)
    try:
        j = response.json()
    except:
        j = {}
    return dict(j).get('last_ts', '*') or '*'

@client.event
async def on_ready():
    print(f'NewsBot logged in as {client.user}')

@client.command()
async def archive(ctx, url: str):
    timestamp = find_latest_archive_timestamp(url)
    response = f'https://web.archive.org/web/{timestamp}/{url}'
    await ctx.send(response)

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        print("Command not found.")
    else:
        raise error

def get_bot_token() -> str:
    return os.getenv('DISCORD_BOT_TOKEN')

client.run(get_bot_token())
