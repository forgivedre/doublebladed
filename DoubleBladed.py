import discord
from discord.ext import commands
import json
from discord_webhook import DiscordWebhook, DiscordEmbed
from colorama import Fore
import requests
import re
import os
import time
from time import strftime
from datetime import datetime
from discord.ext.commands import CommandNotFound
import random
import urllib
now = datetime.now() 

print(f"{Fore.RED}Connecting to DoubleBladed")
time.sleep(1.5)
os.system("cls")

with open("config.json") as f:

    config = json.load(f)

token = config.get("token")
prefix = config.get("prefix")

client = commands.Bot(command_prefix=prefix,self_bot=True)
client.remove_command(name="help")

@client.event
async def on_connect():
    print(f''' {Fore.RESET}
 ▓█████▄  ▒█████   █    ██  ▄▄▄▄    ██▓    ▓█████  ▄▄▄▄    ██▓    ▄▄▄      ▓█████▄ ▓█████ ▓█████▄ 
 ▒██▀ ██▌▒██▒  ██▒ ██  ▓██▒▓█████▄ ▓██▒    ▓█   ▀ ▓█████▄ ▓██▒   ▒████▄    ▒██▀ ██▌▓█   ▀ ▒██▀ ██▌
 ░██   █▌▒██░  ██▒▓██  ▒██░▒██▒ ▄██▒██░    ▒███   ▒██▒ ▄██▒██░   ▒██  ▀█▄  ░██   █▌▒███   ░██   █▌
 ░▓█▄   ▌▒██   ██░▓▓█  ░██░▒██░█▀  ▒██░    ▒▓█  ▄ ▒██░█▀  ▒██░   ░██▄▄▄▄██ ░▓█▄   ▌▒▓█  ▄ ░▓█▄   ▌
 ░▒████▓ ░ ████▓▒░▒▒█████▓ ░▓█  ▀█▓░██████▒░▒████▒░▓█  ▀█▓░██████▒▓█   ▓██▒░▒████▓ ░▒████▒░▒████▓  
  ▒▒▓  ▒ ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒ ░▒▓███▀▒░ ▒░▓  ░░░ ▒░ ░░▒▓███▀▒░ ▒░▓  ░▒▒   ▓▒█░ ▒▒▓  ▒ ░░ ▒░ ░ ▒▒▓  ▒ 
  ░ ▒  ▒   ░ ▒ ▒░ ░░▒░ ░ ░ ▒░▒   ░ ░ ░ ▒  ░ ░ ░  ░▒░▒   ░ ░ ░ ▒  ░ ▒   ▒▒ ░ ░ ▒  ▒  ░ ░  ░ ░ ▒  ▒ 
  ░ ░  ░ ░ ░ ░ ▒   ░░░ ░ ░  ░    ░   ░ ░      ░    ░    ░   ░ ░    ░   ▒    ░ ░  ░    ░    ░ ░  ░ 
    ░        ░ ░     ░      ░          ░  ░   ░  ░ ░          ░  ░     ░  ░   ░       ░  ░   ░    
  ░                              ░                      ░                   ░              ░         
                                                                  
 {Fore.LIGHTRED_EX}Logged In As: ({Fore.RESET}{client.user.name}{Fore.LIGHTRED_EX}) | ID: ({Fore.RESET}{client.user.id}{Fore.LIGHTRED_EX}) | Tag: ({Fore.RESET}{client.user.discriminator}{Fore.LIGHTRED_EX})

 {Fore.LIGHTRED_EX}Servers: ({Fore.RESET}{len(client.guilds)}{Fore.LIGHTRED_EX}) | Friends: ({Fore.RESET}{len(client.user.friends)}{Fore.LIGHTRED_EX})

 {Fore.LIGHTRED_EX}Prefix: ({Fore.RESET}{prefix}{Fore.LIGHTRED_EX}) 

    '''.replace('░', f'{Fore.LIGHTRED_EX}░{Fore.RESET}'))

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        pass
    else:
        pass

@client.command()
async def help(ctx):
    time = now.strftime("%H:%M:%S")
    print(f" {Fore.LIGHTRED_EX}[{Fore.RESET}{time}{Fore.LIGHTRED_EX}] Command Used | {Fore.RESET}Help\n")
    member=ctx.author
    embed=discord.Embed(color=discord.Colour.dark_theme(),timestamp=ctx.message.created_at)
    embed.set_author(name="𝘿𝙤𝙪𝙗𝙡𝙚𝘽𝙡𝙖𝙙𝙚𝙙 𝙎𝙚𝙡𝙛𝙗𝙤𝙩",icon_url=member.avatar_url)
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_image(url='https://cdn.discordapp.com/attachments/801501455592062976/801713894837846046/image0.gif')
    embed.add_field(name="𝙈𝙤𝙙𝙚𝙧𝙖𝙩𝙞𝙤𝙣 🧊",value="`𝘋𝘪𝘴𝘱𝘭𝘢𝘺𝘴 𝘔𝘰𝘥𝘦𝘳𝘢𝘵𝘪𝘰𝘯 𝘊𝘰𝘮𝘮𝘢𝘯𝘥𝘴`",inline=False)
    embed.add_field(name="𝙎𝙩𝙖𝙩𝙪𝙨 🧊",value="`𝘋𝘪𝘴𝘱𝘭𝘢𝘺𝘴 𝘚𝘵𝘢𝘵𝘶𝘴 𝘊𝘰𝘮𝘮𝘢𝘯𝘥𝘴`",inline=False)
    embed.add_field(name="𝙁𝙪𝙣 🧊",value="`𝘋𝘪𝘴𝘱𝘭𝘢𝘺𝘴 𝘍𝘶𝘯 𝘊𝘰𝘮𝘮𝘢𝘯𝘥𝘴`",inline=False)
    embed.set_footer(text=f"Made by zav#7500 | requested by {member}")
    
    await ctx.send(embed=embed)

@client.command(aliases=['mod','helpmod'])
async def moderation(ctx):
    time = now.strftime("%H:%M:%S")
    print(f" {Fore.LIGHTRED_EX}[{Fore.RESET}{time}{Fore.LIGHTRED_EX}] Command Used | {Fore.RESET}Moderation\n")
    member=ctx.author
    embed=discord.Embed(color=discord.Colour.dark_theme(),timestamp=ctx.message.created_at)
    embed.set_author(name="𝘿𝙤𝙪𝙗𝙡𝙚𝘽𝙡𝙖𝙙𝙚𝙙 𝙎𝙚𝙡𝙛𝙗𝙤𝙩",icon_url=member.avatar_url)
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_image(url='https://cdn.discordapp.com/attachments/800811206691913748/800957509942509608/image0_3.gif')
    embed.add_field(name="𝘽𝙖𝙣 🧊",value="`𝘉𝘢𝘯𝘴 𝘔𝘦𝘯𝘵𝘪𝘰𝘯𝘦𝘥 𝘜𝘴𝘦𝘳`",inline=False)
    embed.add_field(name="𝙆𝙞𝙘𝙠 🧊",value="`𝘒𝘪𝘤𝘬𝘴 𝘔𝘦𝘯𝘵𝘪𝘰𝘯𝘦𝘥 𝘜𝘴𝘦𝘳`",inline=False)
    embed.add_field(name="𝙋𝙪𝙧𝙜𝙚 🧊",value="`𝘋𝘦𝘭𝘦𝘵𝘦𝘴 𝘌𝘯𝘵𝘦𝘳𝘦𝘥 𝘈𝘮𝘰𝘶𝘯𝘵 𝘖𝘧 𝘔𝘦𝘴𝘴𝘢𝘨𝘦𝘴`",inline=False)
    embed.add_field(name="𝙇𝙤𝙘𝙠 🧊",value="`𝘓𝘰𝘤𝘬𝘴 𝘈 𝘚𝘱𝘦𝘤𝘪𝘧𝘪𝘤 𝘊𝘩𝘢𝘯𝘯𝘦𝘭`",inline=False)
    embed.add_field(name="𝙐𝙣𝙡𝙤𝙘𝙠 🧊",value="`𝘜𝘯𝘭𝘰𝘤𝘬𝘴 𝘈 𝘚𝘱𝘦𝘤𝘪𝘧𝘪𝘤 𝘊𝘩𝘢𝘯𝘯𝘦𝘭`",inline=False)
    embed.set_footer(text=f"Made by zav#7500 | requested by {member}")
    
    await ctx.send(embed=embed)

@client.command(aliases=['helpstatus'])
async def status(ctx):
    time = now.strftime("%H:%M:%S")
    print(f" {Fore.LIGHTRED_EX}[{Fore.RESET}{time}{Fore.LIGHTRED_EX}] Command Used | {Fore.RESET}Status\n")
    member=ctx.author
    embed=discord.Embed(color=discord.Colour.dark_theme(),timestamp=ctx.message.created_at)
    embed.set_author(name="𝘿𝙤𝙪𝙗𝙡𝙚𝘽𝙡𝙖𝙙𝙚𝙙 𝙎𝙚𝙡𝙛𝙗𝙤𝙩",icon_url=member.avatar_url)
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_image(url='https://cdn.discordapp.com/attachments/803414709196816486/803841360372301874/image3.gif')
    embed.add_field(name="𝙎𝙩𝙧𝙚𝙖𝙢 🧊",value="`𝘚𝘵𝘳𝘦𝘢𝘮𝘪𝘯𝘨 𝘠𝘰𝘶𝘳 𝘔𝘦𝘴𝘴𝘢𝘨𝘦`",inline=False)
    embed.add_field(name="𝙋𝙡𝙖𝙮 🧊",value="`𝘗𝘭𝘢𝘺𝘪𝘯𝘨 𝘠𝘰𝘶𝘳 𝘔𝘦𝘴𝘴𝘢𝘨𝘦`",inline=False)
    embed.add_field(name="𝙒𝙖𝙩𝙘𝙝 🧊",value="`𝘞𝘢𝘵𝘤𝘩𝘪𝘯𝘨 𝘠𝘰𝘶𝘳 𝘔𝘦𝘴𝘴𝘢𝘨𝘦`",inline=False)
    embed.add_field(name="𝙇𝙞𝙨𝙩𝙚𝙣 🧊",value="`𝘓𝘪𝘴𝘵𝘦𝘯𝘪𝘯𝘨 𝘛𝘰 𝘠𝘰𝘶𝘳 𝘔𝘦𝘴𝘴𝘢𝘨𝘦`",inline=False)
    embed.add_field(name="𝘾𝙡𝙚𝙖𝙧 🧊",value="`𝘊𝘭𝘦𝘢𝘳𝘴 𝘠𝘰𝘶𝘳 𝘚𝘵𝘢𝘵𝘶𝘴`",inline=False)
    embed.set_footer(text=f"Made by zav#7500 | requested by {member}")
    
    await ctx.send(embed=embed)

@client.command(aliases=['helpfun'])
async def fun(ctx):
    time = now.strftime("%H:%M:%S")
    print(f" {Fore.LIGHTRED_EX}[{Fore.RESET}{time}{Fore.LIGHTRED_EX}] Command Used | {Fore.RESET}Fun\n")
    member=ctx.author
    embed=discord.Embed(color=discord.Colour.dark_theme(),timestamp=ctx.message.created_at)
    embed.set_author(name="𝘿𝙤𝙪𝙗𝙡𝙚𝘽𝙡𝙖𝙙𝙚𝙙 𝙎𝙚𝙡𝙛𝙗𝙤𝙩",icon_url=member.avatar_url)
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_image(url='https://cdn.discordapp.com/attachments/803414709196816486/803845997930872862/image4.gif')
    embed.add_field(name="𝙂𝙖𝙮𝙧𝙖𝙩𝙚 🧊",value="`𝘎𝘢𝘺𝘳𝘢𝘵𝘦 𝘚𝘰𝘮𝘦𝘰𝘯𝘦`",inline=False)
    embed.add_field(name="𝙎𝙞𝙢𝙥𝙧𝙖𝙩𝙚 🧊",value="`𝘚𝘪𝘮𝘱𝘳𝘢𝘵𝘦 𝘚𝘰𝘮𝘦𝘰𝘯𝘦`",inline=False)
    embed.add_field(name="𝙍𝙚𝙫𝙚𝙧𝙨𝙚 🧊",value="`𝘙𝘦𝘷𝘦𝘳𝘴𝘦 𝘠𝘰𝘶𝘳 𝘔𝘦𝘴𝘴𝘢𝘨𝘦`",inline=False)
    embed.add_field(name="8𝙗𝙖𝙡𝙡 🧊",value="`𝘍𝘰𝘳 8𝘣𝘢𝘭𝘭`",inline=False)
    embed.add_field(name="𝙎𝙖𝙮 🧊",value="`𝘚𝘦𝘯𝘥 𝘈 𝘔𝘦𝘴𝘴𝘢𝘨𝘦 𝘐𝘯 𝘌𝘮𝘣𝘦𝘥`",inline=False)
    embed.set_footer(text=f"Made by zav#7500 | requested by {member}")
    
    await ctx.send(embed=embed)

@client.command()
async def ban(ctx,member:discord.Member,*,reason=None):
    time = now.strftime("%H:%M:%S")
    print(f" {Fore.LIGHTRED_EX}[{Fore.RESET}{time}{Fore.LIGHTRED_EX}] Command Used | {Fore.RESET}Ban\n")
    try:
        await member.ban(reason=reason)
        embed=discord.Embed(color=discord.Colour.dark_theme(),timestamp=ctx.message.created_at,title=f"{member} Has Been Banned",description=f"Reason = `{reason}`")
        embed.set_footer(text=f"Responsible: {ctx.message.author}")
        await ctx.send(embed=embed)
    except:
        pass

@client.command()
async def kick(ctx,member:discord.Member,*,reason=None):
    time = now.strftime("%H:%M:%S")
    print(f" {Fore.LIGHTRED_EX}[{Fore.RESET}{time}{Fore.LIGHTRED_EX}] Command Used | {Fore.RESET}Kick\n")
    try:
        await member.kick(reason=reason)
        embed=discord.Embed(color=discord.Colour.dark_theme(),timestamp=ctx.message.created_at,title=f"{member} Has Been Kicked",description=f"Reason = `{reason}`")
        embed.set_footer(text=f"Responsible: {ctx.message.author}")
        await ctx.send(embed=embed)
    except:
        pass

@client.command(aliases=['listening'])
async def listen(ctx, *, message):
    time = now.strftime("%H:%M:%S")
    print(f" {Fore.LIGHTRED_EX}[{Fore.RESET}{time}{Fore.LIGHTRED_EX}] Command Used | {Fore.RESET}Listen\n")
    await ctx.message.delete()
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=message))

@client.command(aliases=["watching"])
async def watch(ctx, *, message):
    time = now.strftime("%H:%M:%S")
    print(f" {Fore.LIGHTRED_EX}[{Fore.RESET}{time}{Fore.LIGHTRED_EX}] Command Used | {Fore.RESET}Watch\n")
    await ctx.message.delete()
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,name=message))

@client.command(aliases=['playing'])
async def play(ctx, *, text):
  time = now.strftime("%H:%M:%S")
  print(f" {Fore.LIGHTRED_EX}[{Fore.RESET}{time}{Fore.LIGHTRED_EX}] Command Used | {Fore.RESET}Game\n")
  await ctx.message.delete()
  await client.change_presence(activity=discord.Game (name = text))
 
@client.command(aliases=['streaming'])
async def stream(ctx, *, text):
    time = now.strftime("%H:%M:%S")
    print(f" {Fore.LIGHTRED_EX}[{Fore.RESET}{time}{Fore.LIGHTRED_EX}] Command Used | {Fore.RESET}Stream\n")
    await ctx.message.delete()
    await client.change_presence(activity=discord.Streaming (url = "https://www.twitch.tv/apathyrunsyou", name= text)) 

@client.command()
async def clear(ctx):
    time = now.strftime("%H:%M:%S")
    print(f" {Fore.LIGHTRED_EX}[{Fore.RESET}{time}{Fore.LIGHTRED_EX}] Command Used | {Fore.RESET}Clear\n")
    await ctx.message.delete()
    await client.change_presence(status=discord.Status.dnd)

@client.command(name='8ball')
async def _ball(ctx, *, question):
    time = now.strftime("%H:%M:%S")
    print(f" {Fore.LIGHTRED_EX}[{Fore.RESET}{time}{Fore.LIGHTRED_EX}] Command Used | {Fore.RESET}8ball\n")
    await ctx.message.delete()
    responses = [
        'As I see it, yes.',
        'Ask again later.',
        'Better not tell you now.',
        'Cannot predict now.',
        'Concentrate and ask again.',
        'Don’t count on it.',
        'It is certain.',
        'It is decidedly so.',
        'Most likely.',
        'My reply is no.',
        'My sources say no.',
        'Outlook not so good.',
        'Outlook good.',
        'Reply hazy, try again.',
        'Signs point to yes.',
        'Very doubtful.',
        'Without a doubt.',
        'Yes.',
        'Yes – definitely.',
        'You may rely on it.'
    ]
    answer = random.choice(responses)
    embed = discord.Embed(color=discord.Colour.dark_theme(),timestamp=ctx.message.created_at)
    embed.add_field(name="**Question:**", value=f"{question}", inline=False)
    embed.add_field(name="**Answer:**", value=f"{answer}", inline=False)
    embed.set_author(name="DoubleBladed - 8 Ball game") 
    embed.set_footer(text=f"Made by zav#7500 | requested by {client.user}")
    await ctx.send(embed=embed)
    
@client.command()
async def gayrate(ctx, member: discord.Member):
  time = now.strftime("%H:%M:%S")
  print(f" {Fore.LIGHTRED_EX}[{Fore.RESET}{time}{Fore.LIGHTRED_EX}] Command Used | {Fore.RESET}Gayrate\n")
  x = random.randint(1,100)
  embed=discord.Embed(color=discord.Colour.dark_theme(),timestamp=ctx.message.created_at,title=f"Gayrate",description=f'{member.mention} is {x}% gay.')
  embed.set_footer(text=f"Made by zav#7500 | requested by {client.user}")
  await ctx.send(embed=embed)

@client.command()
async def simprate(ctx, member: discord.Member):
  time = now.strftime("%H:%M:%S")
  print(f" {Fore.LIGHTRED_EX}[{Fore.RESET}{time}{Fore.LIGHTRED_EX}] Command Used | {Fore.RESET}Simprate\n")
  x = random.randint(1,100)
  embed=discord.Embed(color=discord.Colour.dark_theme(),timestamp=ctx.message.created_at,title=f"Gayrate",description=f'{member.mention} is {x}% simp.')
  embed.set_footer(text=f"Made by zav#7500 | requested by {client.user}")
  await ctx.send(embed=embed)

@client.command()
async def say(ctx, msg):
    time = now.strftime("%H:%M:%S")
    print(f" {Fore.LIGHTRED_EX}[{Fore.RESET}{time}{Fore.LIGHTRED_EX}] Command Used | {Fore.RESET}Say\n")
    await ctx.message.delete()
    embed=discord.Embed(color=discord.Colour.dark_theme(),timestamp=ctx.message.created_at,title=f"{msg}")
    embed.set_footer(text=f"Made by zav#7500 | requested by {client.user}")
    await ctx.send(embed=embed)

@client.command()
async def reverse(ctx,message):
    time = now.strftime("%H:%M:%S")
    print(f" {Fore.LIGHTRED_EX}[{Fore.RESET}{time}{Fore.LIGHTRED_EX}] Command Used | {Fore.RESET}Reverse\n")
    await ctx.message.delete()
    message = message[::-1]
    await ctx.send(message)

@client.command()
async def purge(ctx,amount:int):
  time = now.strftime("%H:%M:%S")
  print(f" {Fore.LIGHTRED_EX}[{Fore.RESET}{time}{Fore.LIGHTRED_EX}] Command Used | {Fore.RESET}Purge\n")
  await ctx.message.delete()
  async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == client.user).map(lambda m:m):
    try:
      await message.delete()
    except:
      pass

@client.command()
async def lock(ctx,channel:discord.TextChannel):
  time = now.strftime("%H:%M:%S")
  print(f" {Fore.LIGHTRED_EX}[{Fore.RESET}{time}{Fore.LIGHTRED_EX}] Command Used | {Fore.RESET}Lock\n")
  try:
    await ctx.channel.set_permissions(ctx.guild.default_role,send_messages=False)
  except:
    pass

@client.command()
async def unlock(ctx,channel:discord.TextChannel):
  time = now.strftime("%H:%M:%S")
  print(f" {Fore.LIGHTRED_EX}[{Fore.RESET}{time}{Fore.LIGHTRED_EX}] Command Used | {Fore.RESET}Unlock\n")
  try:
    await ctx.channel.set_permissions(ctx.guild.default_role,send_messages=True)
  except:
    pass

client.run(token,bot=False)
