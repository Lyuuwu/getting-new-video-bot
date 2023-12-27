
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
        My_token = "your token"
        await bot.start(My_token)

if __name__ == "__main__":
    asyncio.run(main())
