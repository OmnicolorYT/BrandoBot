import discord
from discord.ext import commands
from discord import Intents
import time
import youtube_dl
from discord.utils import get
import os
import wavelink

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('music загружен')


def setup(bot):
    bot.add_cog(Music(bot))
