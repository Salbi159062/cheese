import discord
from discord.ext import commands

# Basic setup with "Intents" (required to read messages)
intents = discord.Intents.default()
intents.message_content = True 

# Set your command prefix (e.g., !ping)
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def ping(ctx):
    await ctx.send('pong!')

# Replace 'YOUR_TOKEN' with your actual bot token
bot.run('YOUR_TOKEN')

