# ZoneRoles Bot

Create timezone roles which updates with current time in that timezone. Use this bot to make timezone of a user visible in their profile.


## Usage

`/create_role timezone` - Create a timezone role with given timezone code or the offset


## Running the bot

1. Install dependencies with
    `poetry install`

If you're getting errors with `distutils` package on ubuntu/debian, try this:
    `sudo apt-get install python3.10-distutils`

2. Create a .env file and add your secret token

    BOT_TOKEN="YOUR_TOKEN_HERE"

3. Run the bot with
    `poetry shell`
    `python bot.py`

4. Run the worker which updates role times at regular intervals with
    `poetry shell`
    `python worker.py`

