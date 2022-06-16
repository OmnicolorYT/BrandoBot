import discord
from discord.ext import commands, tasks
from itertools import cycle

status = cycle(['смотрю за сервером', 'модерирую чат', 'ищу музыку', 'пытаюсь не глючить', 'бешу администраторов',
                'подкатываю к телкам', 'хочу спать', 'хачу пиццу', 'делаю домашку 7 класса', 'прогуливаю пары'])


@tasks.loop(minutes=15)
async def statistics(self):
    guild = self.bot.get_guild(950855910857785414)
    channel_to_edit2 = self.bot.get_channel(987018845527101450)
    count = 0
    for entry_member in guild.members:
        if str(entry_member.status) == "online" or str(entry_member.status) == "idle":
            count += 1
    await channel_to_edit2.edit(name=f'Человек онлайн: {count - 1}')
    count2 = 0
    channel_to_edit3 = self.bot.get_channel(987018863575191662)
    for entry_voice_channel in guild.voice_channels:
        count2 = count2 + len(entry_voice_channel.members)
    await channel_to_edit3.edit(name=f'Общаются: {count2}')
    channel_to_edit = self.bot.get_channel(987018723514794094)
    await channel_to_edit.edit(name=f'Всего человек: {channel_to_edit.guild.member_count}')


@tasks.loop(seconds=10)
async def change_status(self):
    await self.bot.change_presence(activity=discord.Game(name=next(status)))


class Information(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        statistics.start(self)
        change_status.start(self)
        print('[log]information загружен')


def setup(bot):
    bot.add_cog(Information(bot))