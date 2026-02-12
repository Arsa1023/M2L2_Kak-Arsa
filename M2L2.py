import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
############ Your Code ###################################
@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot,I am here to save the earth! but I need your help!🫵🏽 {bot.user}!')

############ Your Code ###################################

bot.run("MTQ3MTQ4NDcyMTQ0NjkxMjI3Mw.GthQh2.USoTs5DGssyext69uwtLAIRkhcmVZ7Ihm6XGT0")