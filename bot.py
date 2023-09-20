import os
from dotenv import load_dotenv
import nextcord
from nextcord.ext import commands
import random
import json
import utils
# importing the other python files
from commands import misc, media, watchlist, participant

import re

load_dotenv()
BOT_TOKEN = os.getenv('DISCORD_TOKEN')
GUILD_ID = int(os.getenv('GUILD_ID'))

intents = nextcord.Intents.default()
intents.message_content = True
bot = commands.Bot(intents=intents)
WATCHLISTFILENAME = "watchlist.json"
# 8 = Admin
# 1024 = View Channel (Pretty much everyone)
EDIT_PERMISSION = 1024


# Called once bot is ready for further action.
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

# Functionality located in the misc.py in commands folder
@bot.slash_command(guild_ids=[GUILD_ID], name="ping", description="pongs the user")
async def ping(interaction: nextcord.Interaction):
    response = misc.ping()
    await interaction.response.send_message(response)

# Functionality located in the misc.py in commands folder
@bot.slash_command(guild_ids=[GUILD_ID], name="popcorn", description="scoop some popcorn!")
async def popcorn(interaction: nextcord.Interaction):
    response = misc.popcorn(interaction)
    await interaction.response.send_message(response)

# Functionality located in the misc.py in commands folder
# Help Command

@bot.slash_command(guild_ids=[GUILD_ID], name="help", description="lists all commands and descriptions")
async def help(interaction: nextcord.Interaction):
    response = misc.help()
    await interaction.response.send_message(response)


# ---------------------------------------------------------------------------
# Watchlist Commands - Create, delete,see watchlists
# ---------------------------------------------------------------------------

# Functionality located in the watchlist.py in commands folder
@bot.slash_command(guild_ids=[GUILD_ID], name="seeall", description="see all watchlists")
async def watchlist_see_all(interaction: nextcord.Interaction):
    response = watchlist.watchlist_see_all()
    await interaction.response.send_message(response)

# Functionality located in the watchlist.py in commands folder
@bot.slash_command(guild_ids=[GUILD_ID], name="create",
                   description="create a new watchlist",
                   default_member_permissions=EDIT_PERMISSION)
async def watchlist_create(interaction: nextcord.Interaction, watchlist_name):
    response = watchlist.watchlist_create(watchlist_name)
    await interaction.response.send_message(response)

# Located in the watchlist.py in commands folder
@bot.slash_command(guild_ids=[GUILD_ID],
                   name="deleteall", 
                   description="delete all existing watchlists", 
                   default_member_permissions=EDIT_PERMISSION)
async def watchlist_delete_all(interaction: nextcord.Interaction):
    # read the json to get all watchlist list
    response = watchlist.watchlist_delete_all()
    await interaction.response.send_message(response)

# Functionality located in the watchlist.py in commands folder
@bot.slash_command(guild_ids=[GUILD_ID], name="delete",
                   description="delete an existing watchlist",
                   default_member_permissions=EDIT_PERMISSION)
async def watchlist_delete(interaction: nextcord.Interaction, watchlist_name):
    response = watchlist.watchlist_delete(watchlist_name)
    await interaction.response.send_message(response)


# ---------------------------------------------------------------------------
# Media Commands - Add media to watchlist
# ---------------------------------------------------------------------------
# Functionality located in the media.py in commands folder
@bot.slash_command(guild_ids=[GUILD_ID],
                   name="add",
                   description="add a movie or show to a watchlist",
                   default_member_permissions=EDIT_PERMISSION)
async def watchlist_add(interaction: nextcord.Interaction, media_name, watchlist_name):

    response = media.watchlist_add(media_name, watchlist_name)
    await interaction.response.send_message(response)


# ---------------------------------------------------------------------------
# Media Commands - Remove media from watchlist
# ---------------------------------------------------------------------------
# Functionality located in the media.py in commands folder
@bot.slash_command(guild_ids=[GUILD_ID],
                   name="remove",
                   description="remove a movie or show from a watchlist",
                   default_member_permissions=EDIT_PERMISSION)
async def watchlist_delete_media(interaction: nextcord.Interaction, media_name, watchlist_name):
    response = media.watchlist_delete_media(media_name, watchlist_name)
    await interaction.response.send_message(response)
    
    
# ---------------------------------------------------------------------------
# Media Commands - Select a random media from watchlist
# ---------------------------------------------------------------------------
# Functionality located in the media.py in commands folder
@bot.slash_command(guild_ids=[GUILD_ID],
                   name="choose",
                   description="select a random item from a watchlist")
async def watchlist_choose(interaction: nextcord.Interaction, watchlist_name):
    response = media.watchlist_choose(watchlist_name)
    await interaction.response.send_message(response)


# ---------------------------------------------------------------------------
# Media Commands - Clear a specified watchlist by removing all its media
# ---------------------------------------------------------------------------
# Functionality located in the media.py in commands folder
@bot.slash_command(guild_ids=[GUILD_ID],
                   name="clear",
                   description="remove all media from a watchlist")
async def watchlist_clear(interaction: nextcord.Interaction, watchlist_name):
    response = media.watchlist_clear(watchlist_name)
    await interaction.response.send_message(response)


# ---------------------------------------------------------------------------
# Media Commands - View all media in a watchlist
# ---------------------------------------------------------------------------
# Functionality located in the media.py in commands folder
@bot.slash_command(guild_ids=[GUILD_ID], name="view", description="view the contents of a watchlist")
async def watchlist_view(interaction: nextcord.Interaction, watchlist_name):

    response = watchlist.watchlist_view(watchlist_name)
    await interaction.response.send_message(response)

# ---------------------------------------------------------------------------
# Participant Commands - Join, leave, view or notifty watchlist participants
# ---------------------------------------------------------------------------

@bot.slash_command(guild_ids=[GUILD_ID], name="join", description="join an existing watchlist")
async def watchlist_join(interaction: nextcord.Interaction, watchlist_name):
    response = participant.watchlist_join(interaction, watchlist_name)
    await interaction.response.send_message(response)

# Functionality located in the participant.py in commands folder
@bot.slash_command(guild_ids=[GUILD_ID], name="leave", description="leave from a joined watchlist")
async def watchlist_leave(interaction: nextcord.Interaction, watchlist_name):
    response = participant.watchlist_leave(interaction, watchlist_name)
    await interaction.response.send_message(response)

# Functionality located in the participant.py in commands folder
@bot.slash_command(guild_ids=[GUILD_ID], name="participants", description="view a watchlist's participants")
async def watchlist_participants(interaction: nextcord.Interaction, watchlist_name):
    response = await participant.watchlist_particpants(bot, watchlist_name)
    await interaction.response.send_message(response)

# Functionality located in the participant.py in commands folder
@bot.slash_command(guild_ids=[GUILD_ID], name="poke", description="notify all participants of a watchlist")
async def watchlist_notifyall(interaction: nextcord.Interaction, watchlist_name):
    response = participant.watchlist_notifyall(watchlist_name)
    await interaction.response.send_message(response)





@bot.slash_command(guild_ids=[GUILD_ID], name="history", description="view all the watched medias in a watchlist")
async def watchlist_history(interaction: nextcord.Interaction, watchlist_name):
    """
    Displays all the movies that have been watched in a watchlist.

    Parameters:
    interaction (nextcord.Interaction): The interaction object representing the command invocation.
    watchlist_name (str): The name of the watchlist to which the watched movies going to be displayed

    Returns:
    None
    """
    # Read the JSON data
    watchlist_data = utils.read_watchlist_file(WATCHLISTFILENAME)

    # Check if the watchlist exists
    watchlist = utils.get_watchlist(watchlist_data, watchlist_name)
    if (watchlist != None):
        if len(watchlist["media"]) == 0:
            response = f"The **{watchlist_name}** watchlist is empty."
        else:
            response = f"Here are all of the medias in the **{watchlist_name}** watchlist you have watched!\n"
            for media_name in watchlist["media"]:  # Print every media item with status watched
                media = watchlist["media"].get(media_name)
                if media["status"] == "watched":
                    response += f"- {media_name}\n"
    else:
        response = f"Watchlist named {watchlist_name} does not exist."

    await interaction.response.send_message(response)



"""
Displays all the media that filtered based on tags in a watchlist.
Args:
    interaction: The interaction object representing the command invocation.
    watchlist_name: The name of the watchlist to which the watched movies going to be displayed
    tags: The tags that want to be based on to filter

Returns:
None

"""
@bot.slash_command(guild_ids=[GUILD_ID], name="filter_by_tags", description="view filtered medias based on tags in a watchlist")
async def filter_tags(interaction: nextcord.Interaction, watchlist_name,tags):

    # Read the JSON data
    watchlist_data = utils.read_watchlist_file(WATCHLISTFILENAME)

    # Check if the watchlist exists
    watchlist = utils.get_watchlist(watchlist_data, watchlist_name)
    if watchlist:
        if not watchlist["media"]:
            response = f"The {watchlist_name} watchlist is empty."
        else:
            input_tags_set = set([tag.strip().lower() for tag in tags.split(',')])  # Convert input tags to a set
            matched_media = [media_name for media_name, media_content in watchlist["media"].items() if
                             input_tags_set.issubset(set(media_content["tags"]))] # using the issubset function istead of ==. Since it would gradually narrow down based on the tags provided

            if matched_media:
                response = f"Here are all of the filtered medias in the {watchlist_name} watchlist based on \"{tags}\" tags:\n"
                response += "\n".join([f"- {name}" for name in matched_media])
            else:
                response = "The Media doesn't exist based on provided tags!"
    else:
        response = f"Watchlist named {watchlist_name} does not exist."

    await interaction.response.send_message(response)

bot.run(BOT_TOKEN)
