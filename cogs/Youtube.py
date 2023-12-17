import discord
import scrapetube
from discord.ext import commands, tasks
from core.classes import Cog_Extension

class Youtube(Cog_Extension):

  def __init__(self, bot):
    self.bot = bot
    self.channels = {
        "第七史詩": "https://youtube.com/@EpicSevenTW"
    }
    self.videos = {}
    self.discord_channel = [1142805471829438564, 984459486628544512]

  @commands.Cog.listener()
  async def on_ready(self):
    self.check.start()

  @tasks.loop(seconds=10)
  async def check(self):
    channel_name = "第七史詩"
    videos = scrapetube.get_channel(channel_url=self.channels[channel_name],limit=10)
    video_ids = []
    video_titles = []
    
    for video in videos:
      video_ids.append(video['videoId'])
      video_titles.append(video['title']['runs'][0]['text'])
        
    if self.check.current_loop == 0:
      self.videos[channel_name] = video_ids
    
    for i in range(0, len(video_ids)):
      if (video_ids[i] in self.videos[channel_name]) :
        continue
      
      url = f"https://youtu.be/{video_ids[i]}"
      print(f"new video! {video_titles[i]}")
      
      for channel_id in self.discord_channel :
        discord.channel = self.bot.get_channel(channel_id)
        if "更新" in video_titles[i]:
          await discord.channel.send(f"**{channel_name}**有新的更新資訊!!!\n{url}")
        elif "合作" in video_titles[i]:
          await discord.channel.send(f"**{channel_name}**有新的合作資訊!!!\n{url}")
        elif "預告" in video_titles[i]:
          await discord.channel.send(f"**{channel_name}**有新的英雄資訊!!!\n{url}")
        elif "特！級！信！件！" in video_titles[i]:
          await discord.channel.send(f"**{channel_name}**有新的特級信件!!!\n{url}")

      self.videos[channel_name].append(video_ids[i])

    print(self.videos[channel_name])


async def setup(bot):
  await bot.add_cog(Youtube(bot))