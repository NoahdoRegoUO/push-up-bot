import discord
import json
import typing
#import datetime
#import asyncio
#import random
#import requests

from discord import message
from discord.ext import commands

config = json.load(open("config.json"))

bot = commands.Bot(
    command_prefix="!", 
    case_insensitive=True
)

@bot.event
async def on_ready():
    print("Bot is ready")

@bot.event
async def on_member_join(member):
    if member.id == bot.id:
        return
    channel = discord.utils.get(bot.guilds[0].channels, name="join")
    response = f"Welcome, {member.name}!"
    await channel.send(response)

"""
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    keywords = ["bingus", "plungus"]
    channel = message.channel
    for keyword in keywords:
        if keyword.lower() in message.content.lower():
            response = f"{message.author.mention} {keyword.lower()}"
    await channel.send(response)
"""

@bot.command()
async def add(ctx, amount: typing.Optional[int] = 0):
    
    if int(amount) > 0 and int(amount) < 10508:
        await ctx.send(f"{amount} push-ups added to your total.")
    else:
        await ctx.send("Insufficient amount of push-ups.")

@bot.command()
async def bingus(ctx, num: typing.Optional[int] = 1, user: typing.Optional[str] = ""):

    if num > 0 and num < 6 and user == "":
        for i in range(num):
            await ctx.send(f"bingus {ctx.message.author.mention}")
    elif num > 0 and num < 6 and user[0:2] == "<@":
        try:
            for i in range(num):
                await ctx.send(f"bingus {user}")
        except:
            await ctx.send(user)
    else:
        await ctx.send("come on now")

token = config["token"]
bot.run(token)