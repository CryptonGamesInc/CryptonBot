import config.config as config, config.help as help

import lib.honeylib10 as lib

import discord
from discord.ext import commands


class Help(commands.Cog):

    def __init__(self, bot:commands.Bot):

        self.bot = bot

    @commands.command(aliases=['help', ''])
    async def __help(self, ctx:commands.Context):

        embed = lib.emb(
            ctx,
            f'Команды CryptonBot',
            discord.Color.red(),
        )
        
        for _command in help.HELP_TEXT:

            embed.add_field(

                name=f'**{config.BOT["PREFIX"]}{_command}**',
                value=help.HELP_TEXT[_command],
                inline=False,

            )

        await ctx.reply(embed=embed)


async def setup(bot:commands.Bot):

    await bot.add_cog(Help(bot))