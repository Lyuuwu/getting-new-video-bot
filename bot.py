import discord
import asyncio
import os
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='\\', intents=intents)

@bot.event
async def on_ready():
    print(f"目前登入身份 --> {bot.user}")

async def load_extensions():
    for filename in os.listdir('youtube_notification\cogs') :
        if filename.endswith(".py") :
            try:
                await bot.load_extension(f"cogs.{filename[:-3]}")
                print(f"load {filename[:-3]} successfully!")
            except Exception as e :
                print(e)

async def main():
    async with bot:
        await load_extensions()
        #TOKEN = "MTEzNTA3NDY0OTU3OTk5OTM4Mw.GiPWyV._qJ-twGDFCRA_wCI_oGGtmnD7WvkQik96j7hJ8"
        TOKEN_test = "MTEzNDg0OTE1NTI5MDg5ODUzMw.GsGv_2.LI5NvGk0mRhFEezRAzXAbIrBE72Taa72nScDTw"
        await bot.start(TOKEN_test)

if __name__ == "__main__":
    asyncio.run(main())