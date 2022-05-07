# ZoneRoles Bot

Create timezone roles which updates with current time in that timezone. Use this bot to make timezone of a user visible in their profile.


## Usage

`/create_role timezone` - Create a timezone role with given timezone code or the offset


## Running the bot

1. Install dependencies with

    `poetry install`

2. Create a .env file and add your secret token

    BOT_TOKEN="YOUR_TOKEN_HERE"

2. Run the bot with

    `poetry run bot.py`
    
or

    `poetry shell`
    `python bot.py`

3. Run the worker which updates role times at regular intervals with
    
    `poetry run worker.py`

or

    `poetry shell`
    `python worker.py`

