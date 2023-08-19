# commands.py
import os
from dotenv import load_dotenv
import nextcord
from nextcord.ext import commands
import json

load_dotenv()
BOT_TOKEN = os.getenv('DISCORD_TOKEN')
GUILD_ID = int(os.getenv('GUILD_ID'))

intents = nextcord.Intents.default()
intents.message_content = True
bot = commands.Bot(intents=intents)
WATCHLISTFILENAME = "watchlist.json"

@bot.slash_command(guild_ids=[GUILD_ID],
                   name="delete_media",
                   description="remove a movie or show from a watchlist")
async def delete_media(interaction: nextcord.Interaction, media_name, watchlist_name):
    """
    Removes a movie or show from a specified watchlist.

    Parameters:
    interaction (nextcord.Interaction): The interaction object representing the command invocation.
    media_name (str): The name of the movie or show to be removed.
    watchlist_name (str): The name of the watchlist from which the movie or show will be removed.

    Returns:
    None
    """
    # Read the JSON data
    watchlist_file = open(WATCHLISTFILENAME, 'r')
    watchlist_data = json.load(watchlist_file)
    watchlist_file.close()

    # Check if the watchlist exists
    watchlist_exists = False
    for watchlist in watchlist_data["watchlists"]:
        if watchlist["name"] == watchlist_name:
            watchlist_exists = True
            # Check if media exists in watchlist
            if media_name in watchlist["media"]:
                watchlist["media"].remove(media_name)
                response = f"Removed *{media_name}* from the **{watchlist_name}** watchlist!"
            else:
                response = f"*{media_name}* is not in the **{watchlist_name}** watchlist!"
            break

    if not watchlist_exists:
        response = f"The **{watchlist_name}** watchlist does not exist!"

    # Write the updated JSON data
    watchlist_file = open(WATCHLISTFILENAME, 'w')
    watchlist_file.write(json.dumps(watchlist_data))
    watchlist_file.close()

    await interaction.response.send_message(response)
