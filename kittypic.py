import discord
import os
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
#normalde yazının başında yazan $
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def kedy(ctx):
    foti_list = os.listdir("kitties")
    foti_name = random.choice(foti_list)
    with open(f'kitties/{foti_name}', "rb") as f:
        pickitty = discord.File(f)
    await ctx.send("KEDY!")
    await ctx.send(file=pickitty)

bot.run("your token here")
