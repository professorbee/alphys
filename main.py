import discord
from discord.ext import commands
import asyncio
from jikanpy import AioJikan
import json

bot = commands.Bot(command_prefix='>')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def search(ctx, search: str):
    async with AioJikan() as aio_jikan:
        userResult = await aio_jikan.search(search_type='anime', query=search)
        userResult = userResult['results'][0]
    userEmbed = discord.Embed(title=userResult['title'], url=userResult['url'], description=userResult['synopsis'])
    userEmbed.set_thumbnail(url=userResult['image_url'])
    await ctx.send("Here you go!", embed=userEmbed)

with open("config.json") as json_data_file:
    data = json.load(json_data_file)
    bot.run(data["token"])