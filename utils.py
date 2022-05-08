import interactions
import json
from datetime import datetime
import pytz
from dotenv import load_dotenv

load_dotenv()

TZ_SUFFIX = '#('
TIME_FORMAT = '%I:%M %p'

timezones = []
with open('timezones.json') as f:
    timezones = json.load(f)

def get_timezone(code: str):
    for timezone in timezones:
        if code.lower() == timezone['abbr'].lower():
            return timezone

    for timezone in timezones:  
        if timezone['text'].lower().find(code.lower()) != -1:
            return timezone

    return False

def get_matching_role(guild: interactions.Guild, abbr: str):
    for role in guild.roles:
        if role.name.find(abbr + TZ_SUFFIX) != -1:
            return role
    return None

def get_matching_timezone(role: interactions.Role):
    if role.name.find(TZ_SUFFIX) == -1:
        return None
    timezoneCode = role.name[:role.name.find(TZ_SUFFIX)]
    for timezone in timezones:
        if timezone['abbr'] == timezoneCode:
            return timezone
    return None

def get_current_name(timezone):
    tz_zone = pytz.timezone(timezone['utc'][0])
    tz_now = datetime.now(tz_zone).strftime(TIME_FORMAT)
    return '{}{}{}) - {}'.format(
        timezone['abbr'],
        TZ_SUFFIX,
        timezone['display'],
        tz_now
    )

async def update_role_name(guild: interactions.Guild, role: interactions.Role):
    timezone = get_timezone(role.name[:role.name.find(TZ_SUFFIX)])
    try:
        await guild.modify_role(role.id, get_current_name(timezone))
    except:
        print('updating role failed')

async def create_role_for_timezone(guild: interactions.Guild, timezone):
    await guild.create_role(get_current_name(timezone))
