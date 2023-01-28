import lib.honeylib10 as lib

import discord
from discord.ext import commands


class Me(commands.Cog):

    def __init__(self, bot:commands.Bot):

        self.bot = bot

    @commands.command(aliases=['me'])
    async def __me(self, ctx:commands.Context, *args):

        if len(args) == 0:

            print(len(args))

            embed = lib.emb(
                ctx,
                'Использование: c!me <текст>.',
                discord.Color.red(),
            )

            await ctx.reply(embed=embed)

            return

        embed = lib.emb(
            ctx,
            f'`{ctx.author} {" ".join(args)}.`',
            discord.Color.blue(),
            setAuthor=False,
        )

        #await ctx.message.delete()
        await ctx.reply(embed=embed)


async def setup(bot:commands.Bot):

    await bot.add_cog(Me(bot))