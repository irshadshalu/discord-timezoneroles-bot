import interactions
from utils import *
import os

bot = interactions.Client(token=os.getenv('BOT_TOKEN'))

@bot.command(
    name="create_role",
    description="Create a new role for a particular timezone",
    options=[
        interactions.Option(
            name="timezone",
            description="Enter the timezone for which you want to create a role for",
            type=interactions.OptionType.STRING,
            required=True,
        ),
    ]
)
async def create_role(ctx: interactions.CommandContext, timezone: str):
    valid_timezone = get_timezone(timezone)
    if not valid_timezone:
        return await ctx.send('Invalid timezone code, please use the abbreviation or the offset. eg: CET, UTC, +3, -5:30, etc.')

    guild = interactions.Guild(**await bot._http.get_guild(ctx.guild_id), _client=bot._http)
    matchingRole = get_matching_role(guild, valid_timezone['abbr'])
    if matchingRole:
        await update_role_name(guild, matchingRole)
        return await ctx.send('A timezone with this role already exists: <@&{}>'.format(matchingRole.id))
    await create_role_for_timezone(guild, valid_timezone)
    await ctx.send("Created a role for timezone: " + valid_timezone['text'])

bot.start()
