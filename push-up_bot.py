import os
import discord
import json
import typing
import asyncio
#import random
#import requests
#import datetime

# Extra discord libraries
#from discord import message
from discord.ext import commands

# Replit database
from replit import db

# Web server hosting function
from keep_alive import keep_alive

bot = commands.Bot(command_prefix="!", case_insensitive=True)


# Bot events:

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


# Bot functions:

def confirm():
    pass

# Bot commands:

@bot.command()
async def add(ctx, amount: typing.Optional[int] = 0):

    if int(amount) > 0 and int(amount) < 10508:
        if f"{ctx.message.author}" in db.keys():
            db[f"{ctx.message.author}"] += amount
        else:
            db[f"{ctx.message.author}"] = amount
        await ctx.send(f"{amount} push-ups added to your total.")
    else:
        await ctx.send("Insufficient amount of push-ups.")


@bot.command()
async def remove(ctx, amount: typing.Optional[int] = 0):
    if f"{ctx.message.author}" in db.keys():
        if int(amount) <= db[f"{ctx.message.author}"] and int(amount) > 0:
            db[f"{ctx.message.author}"] -= amount
            await ctx.send(f"{amount} push-ups removed from your total.")
        else:
            
            await ctx.send("Insufficient amount of push-ups to remove.")
    else:
        db[f"{ctx.message.author}"] = 0
        await ctx.send("You have 0 push-ups!")


@bot.command()
async def total(ctx):
    if f"{ctx.message.author}" in db.keys():
        total = db[f"{ctx.message.author}"]
    else:
        db[f"{ctx.message.author}"] = 0
        total = db[f"{ctx.message.author}"]  
    await ctx.send(f"You have done {total} push-ups.")


@bot.command()
async def time(ctx):
    channel = ctx.message.channel
    message = await channel.send('Timer started, react with 👍 to stop')
    await message.add_reaction('👍')
    
    def check(reaction, user):
        return user == ctx.message.author and str(reaction.emoji) == '👍'

    try:
        reaction, user = await bot.wait_for('reaction_add', timeout=60.0, check=check)
    except asyncio.TimeoutError:
        await channel.send('Time limit reached')
    else:
        await channel.send('Your time is ___')

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
