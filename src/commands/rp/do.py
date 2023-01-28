import lib.honeylib10 as lib

import discord
from discord.ext import commands


class Do(commands.Cog):

    def __init__(self, bot:commands.Bot):

        self.bot = bot

    @commands.command(aliases=['do'])
    async def __do(self, ctx:commands.Context, *args):

        if len(args) == 0:

            embed = lib.emb(
                ctx,
                'Использование: c!do <текст>.',
                discord.Color.green(),
            )

            await ctx.reply(embed=embed)

            return

        embed = lib.emb(
            ctx,
            f'`{ctx.author} Успешно смог {" ".join(args)}!`',
            discord.Color.red(),
            setAuthor=False,
        )

        #await ctx.message.delete()
        await ctx.reply(embed=embed)


async def setup(bot:commands.Bot):

    await bot.add_cog(Do(bot))