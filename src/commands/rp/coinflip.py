import lib.honeylib10 as lib

from random import randint

import discord
from discord.ext import commands


class Coinflip(commands.Cog):

    def __init__(self, bot:commands.Bot):

        self.bot = bot

    @commands.command(aliases=['coinflip'])
    async def __coinflip(self, ctx:commands.Context):

        results = {
            1: 'Орел',
            2: 'Решка',
        }

        result = results.get(randint(1, 2))

        embed = lib.emb(
            ctx,
            f'Монетка прозвенела, и выпадает...\n***{result}***!',
            discord.Color.gold(),
        )

        #await ctx.message.delete()
        await ctx.reply(embed=embed)


async def setup(bot:commands.Bot):

    await bot.add_cog(Coinflip(bot))