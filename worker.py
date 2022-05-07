import interactions
import time
import asyncio
import aioschedule as schedule
import time
from utils import *
import os

worker_interval = int(os.getenv('WORKER_INTERVAL_MINS', 5))
client = interactions.HTTPClient(token=os.getenv('BOT_TOKEN'))

# Goes through all guilds and updates every timezone role with latest time.
async def update_all_roles():
    guilds = await client.get_self_guilds()
    for _guild in guilds:
        guild = interactions.Guild(**_guild, _client=client)
        roles = await guild.get_all_roles()
        for role in roles:
            matchingTimezone = get_matching_timezone(role)
            if not matchingTimezone:
                continue
            await update_role_name(guild, role)

schedule.every(worker_interval).minutes.do(update_all_roles)
loop = asyncio.get_event_loop()
while True:
    loop.run_until_complete(schedule.run_pending())
    time.sleep(1)
