import discord
import scrapetube
import datetime
from discord.ext import commands, tasks
from core.classes import Cog_Extension

async def print_new_video(self, video_id, video_title, channel_name):
  # The link to the video
  url = f"https://youtu.be/{video_id}"
  print(f"new video! {video_title}")
  for channel_id in self.discord_channel :
    # The channel you what to send message
    discord.channel = self.bot.get_channel(channel_id)

    # The key words that you want
    # If the title of the video includes one of these key words, then the bot sends message to a channel
    # Notice: the key words have hierarchy, when multiple key words that are satisfied,
    # the bot prioritizes the forefront key word
    if "更新" in video_title:
      await discord.channel.send(f"**{channel_name}**有新的更新資訊!!!\n{url}")
    elif "合作" in video_title:
      await discord.channel.send(f"**{channel_name}**有新的合作資訊!!!\n{url}")
    elif "預告" in video_title:
      await discord.channel.send(f"**{channel_name}**有新的英雄資訊!!!\n{url}")
    elif "特！級！信！件！" in video_title:
      await discord.channel.send(f"**{channel_name}**有新的特級信件!!!\n{url}")
  self.videos[channel_name].append(video_id)

class Youtube(Cog_Extension):
  def __init__(self, bot):
    self.bot = bot
    self.channels = {
        # "The name of the game or youtuber, etc." : "the link to the channel"
        "第七史詩": "https://youtube.com/@EpicSevenTW"
    }
    self.videos = {}
    # The channel where you want the bot send message
    self.discord_channel = [1142805471829438564, 984459486628544512]

  every_time = [
    datetime.time(hour=10, minute=30, tzinfo = datetime.timezone(datetime.timedelta(hours = 8))),
    datetime.time(hour=15, minute=30, tzinfo = datetime.timezone(datetime.timedelta(hours = 8))),
    datetime.time(hour=17, minute=30, tzinfo = datetime.timezone(datetime.timedelta(hours = 8)))
  ]

  @commands.Cog.listener()
  async def on_ready(self):
    self.do_check.start()

  @tasks.loop(time=every_time)
  async def do_check(self):
    await self.check.start()

  #(seconds = the interval you want, count = the time you want to re execute)
  @tasks.loop(seconds=10, count=360)
  async def check(self):
    # The channel name is used to get url at self.channels
    # You can change it to a list if you want multiple channel name
    channel_name = "第七史詩"
    videos = scrapetube.get_channel(channel_url=self.channels[channel_name],limit=10)
    video_ids = []
    video_titles = []
    
    for video in videos:
      video_ids.append(video['videoId'])
      video_titles.append(video['title']['runs'][0]['text'])
        
    if self.check.current_loop == 0:
      self.videos[channel_name] = video_ids
      print("It's running right now!!")
    
    for i in range(0, len(video_ids)):
      if (video_ids[i] in self.videos[channel_name]) :
        continue
      await print_new_video(self, video_ids[i], video_titles[i], channel_name)

async def setup(bot):
  await bot.add_cog(Youtube(bot))