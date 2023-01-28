import datetime, random

from discord import Color, Member, Embed
from discord.ext.commands import Context


# Get random number from min to max value & convert it to string
def rstr(min:int, max:int) -> str:

	randomString = str(random.randint(min, max))

	return randomString


# Get current date & time like '1 Oct 2022 12:34:56'
def getTime() -> str:

	dt = datetime.datetime.now()
	return f'[{dt:%d %h %Y %H:%M:%S}]'


# Create new Discord Embed message
def emb(ctx:Context, title:str, colour:Color, setAuthor:bool=True, member:Member=None) -> Embed:
	
	# Creating new Embed
	embed = Embed(
		title=title,
		colour=colour,
	)
	
	# If member is not specified, setting it to message author
	if not member:
		member = ctx.author
	
	# Getting member's avatar
	if setAuthor:

		embed.set_author(
			name=member.name,
			icon_url=member.avatar.url,
		)
	
	return embed