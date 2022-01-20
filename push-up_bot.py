import os
import discord
import json
import typing
#import datetime
#import asyncio
#import random
#import requests

# Extra discord libraries
from discord import message
from discord.ext import commands

# Replit database
from replit import db

# Web server hosting function
from keep_alive import keep_alive

bot = commands.Bot(command_prefix="!", case_insensitive=True)

<<<<<<< HEAD
# Bot events:
=======
>>>>>>> 1e75ef86a82779ebb24e847a290b601b72fcb920

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
    response = ""
    await channel.send(response)
"""
# Bot functions:

def confirm():
    pass

# Bot commands:


@bot.command()
async def add(ctx, amount: typing.Optional[int] = 0):

    if int(amount) > 0 and int(amount) < 10508:
<<<<<<< HEAD
        if ctx.message.author in db.keys():
            db[ctx.message.author] += amount
        else:
            db[ctx.message.author] = amount
=======
        if f"{ctx.message.author}" in db.keys():
            db[f"{ctx.message.author}"] += amount
        else:
            db[f"{ctx.message.author}"] = amount
>>>>>>> 1e75ef86a82779ebb24e847a290b601b72fcb920
        await ctx.send(f"{amount} push-ups added to your total.")
    else:
        await ctx.send("Insufficient amount of push-ups.")


@bot.command()
async def total(ctx):
<<<<<<< HEAD
    await ctx.send(db[ctx.message.author])
=======
    if f"{ctx.message.author}" in db.keys():
        total = db[f"{ctx.message.author}"]
    else:
        db[f"{ctx.message.author}"] = 0
        total = db[f"{ctx.message.author}"]  
    await ctx.send(f"You have done {total} push-ups.")

>>>>>>> 1e75ef86a82779ebb24e847a290b601b72fcb920

@bot.command()
async def bingus(ctx,
                 num: typing.Optional[int] = 1,
                 user: typing.Optional[str] = ""):

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


keep_alive()
token = os.environ['DISCORD_TOKEN']
bot.run(token)
