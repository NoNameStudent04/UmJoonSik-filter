import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

client = commands.Bot(command_prefix = '')
client.remove_command("help")
token = 'Your T0ken Here :)'

@client.event
async def on_ready():
    print("엄.. 준..식..")
    print(client.user.id)
    print("----------------")
    game = discord.Game("엄 / 준 / 식 / 엄준식 [ 검열 ]")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.command(pass_context=True)
async def 엄(ctx):
    await ctx.channel.purge(limit=2)
    await ctx.send(":white_check_mark: **엄** 검열 완료")

@client.command(pass_context=True)
async def 준(ctx):
    await ctx.channel.purge(limit=2)
    await ctx.send(":white_check_mark: **준** 검열 완료")

@client.command(pass_context=True)
async def 식(ctx):
    await ctx.channel.purge(limit=2)
    await ctx.send(":white_check_mark: **식** 검열 완료")

@client.command(pass_context=True)
async def 엄준식(ctx):
    await ctx.channel.purge(limit=2)
    await ctx.send(":white_check_mark: **엄준식** 검열 완료")

@client.command(pass_context=True)
async def 식준엄(ctx):
    await ctx.channel.purge(limit=2)
    await ctx.send(":white_check_mark: **엄준식(식준엄)** 검열 완료")

@client.command(pass_context=True)
async def 엄식준(ctx):
    await ctx.channel.purge(limit=2)
    await ctx.send(":white_check_mark: **엄준식(엄식준)** 검열 완료")

@client.command(pass_context=True)
async def 준식엄(ctx):
    await ctx.channel.purge(limit=2)
    await ctx.send(":white_check_mark: **엄준식(준식엄)** 검열 완료")

client.run(token)