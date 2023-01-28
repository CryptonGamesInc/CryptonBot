import lib.honeylib10 as lib

import discord
from discord.ext import commands


class Try(commands.Cog):

    def __init__(self, bot:commands.Bot):

        self.bot = bot

    @commands.command(aliases=['try'])
    async def __try(self, ctx:commands.Context, *args):

        if len(args) == 0:

            embed = lib.emb(
                ctx,
                'Использование: c!try <текст>.',
                discord.Color.red(),
            )

            await ctx.reply(embed=embed)

            return

        embed = lib.emb(
            ctx,
            f'`{ctx.author} Попытался {" ".join(args)}.`',
            discord.Color.blurple(),
            setAuthor=False,
        )

        #await ctx.message.delete()
        await ctx.reply(embed=embed)


async def setup(bot:commands.Bot):

    await bot.add_cog(Try(bot))