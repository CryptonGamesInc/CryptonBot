

#
#
# Made by @crypton#1871
# Copyright (c) Crypton Games Inc. 2023.
# Join us: https://discord.gg/FaphmYsFNb
#
#

#
# LAST UPDATE: 27.01.2023.
#


def main():

    
    # Main imports
    import config.config as config, config.commands as _commands

    # Discord.py imports
    import discord
    from discord.ext import commands

    # Etc imports
    import logging


    logging.basicConfig(format='%(asctime)s %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)


    # Initializing bot
    bot = commands.Bot(
        command_prefix=config.BOT['PREFIX'],
        help_command=None,
        intents=discord.Intents.all(),
    )


    # Performing actions before bot has logged in Discord API
    @bot.event
    async def on_ready():

        print('\n')

        # Adding all commands to bot
        for _command in _commands.COMMANDS:

            await bot.load_extension(f'commands.{_command}')
            logging.info(f'[BOT] Loaded command: {_command}')

        print('\n')


        # Changing status displayed in bot's profile
        await bot.change_presence(
            status=discord.Status.online,
            activity=discord.Game(config.BOT['STATUS']),
        )


        logging.info(f'[BOT] Started as {bot.user}')


    # Logging all issued commands
    @bot.before_invoke
    async def __before_invoke(ctx:commands.Context):

        logging.info(f'[BOT] {ctx.author} issued command: {ctx.message.content}')

    
    # Done! Running bot
    bot.run(config.BOT['TOKEN'], reconnect=True)


# Python OOP magic
if __name__ == '__main__':

    main()