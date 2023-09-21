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


# ---------------------------------------------------------------------------
# Misc Commands - Ping, Popcorn and Help commands
# ---------------------------------------------------------------------------
# Functionality located in the misc.py in commands folder
@bot.slash_command(guild_ids=[GUILD_ID], name="ping", description="pongs the user")
async def ping(interaction: nextcord.Interaction):
    response = misc.ping()
    await interaction.response.send_message(response)

@bot.slash_command(guild_ids=[GUILD_ID], name="popcorn", description="scoop some popcorn!")
async def popcorn(interaction: nextcord.Interaction):
    response = misc.popcorn(interaction)
    await interaction.response.send_message(response)

# Help Command
@bot.slash_command(guild_ids=[GUILD_ID], name="help", description="lists all commands and descriptions")
async def help(interaction: nextcord.Interaction):
    """
	   Displays all the commands of the bot

	   Parameters:
	   interaction (nextcord.Interaction): The interaction object representing the command invocation.


	   Returns:
	   None
	   """
    response = misc.help()
    await interaction.response.send_message(response)


# ---------------------------------------------------------------------------
# Watchlist Commands - Create, delete,see watchlists
# ---------------------------------------------------------------------------

# Functionality located in the watchlist.py in commands folder
@bot.slash_command(guild_ids=[GUILD_ID], name="seeall", description="see all watchlists")
async def watchlist_see_all(interaction: nextcord.Interaction):
    """
       See all the watchlists

       Parameters:
       interaction (nextcord.Interaction): The interaction object representing the command invocation.

       Returns:
       None
       """
    response = watchlist.watchlist_see_all()
    await interaction.response.send_message(response)

# Functionality located in the watchlist.py in commands folder
@bot.slash_command(guild_ids=[GUILD_ID], name="create",
                   description="create a new watchlist",
                   default_member_permissions=EDIT_PERMISSION)
async def watchlist_create(interaction: nextcord.Interaction, watchlist_name):
    """
       Creates a watchlist

       Parameters:
       interaction (nextcord.Interaction): The interaction object representing the command invocation.
       watchlist_name (str): The name of the watchlist to which the watched movies going to be displayed

       Returns:
       None
       """
    response = watchlist.watchlist_create(watchlist_name)
    await interaction.response.send_message(response)

# Located in the watchlist.py in commands folder
@bot.slash_command(guild_ids=[GUILD_ID],
                   name="deleteall", 
                   description="delete all existing watchlists", 
                   default_member_permissions=EDIT_PERMISSION)
async def watchlist_delete_all(interaction: nextcord.Interaction):
    """
        Delete all watchlists

        Parameters:
        interaction (nextcord.Interaction): The interaction object representing the command invocation.

        Returns:
        None
    """
    # read the json to get all watchlist list
    response = watchlist.watchlist_delete_all()
    await interaction.response.send_message(response)

# Functionality located in the watchlist.py in commands folder
@bot.slash_command(guild_ids=[GUILD_ID], name="delete",
                   description="delete an existing watchlist",
                   default_member_permissions=EDIT_PERMISSION)
async def watchlist_delete(interaction: nextcord.Interaction, watchlist_name):
    """
          Delete a watchlist

          Parameters:
          interaction (nextcord.Interaction): The interaction object representing the command invocation.
          watchlist_name (str): The name of the watchlist to which the watched movies going to be displayed

          Returns:
          None
          """
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
    """
        Adds a movie or show to a specified watchlist.

        Parameters:
        interaction (nextcord.Interaction): The interaction object representing the command invocation.
        media_name (str): The name of the movie or show to be added.
        watchlist_name (str): The name of the watchlist to which the movie or show will be added.

        Returns:
        None
        """
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
    """
    	    Removes a movie or show from a specified watchlist.

    	    Parameters:
    	    interaction (nextcord.Interaction): The interaction object representing the command invocation.
    	    media_name (str): The name of the movie or show to be removed.
    	    watchlist_name (str): The name of the watchlist from which the movie or show will be removed.

    	    Returns:
    	    None
    	    """
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
    """
        Chooses a media in a watchlist at random

        Parameters:
        interaction (nextcord.Interaction): The interaction object representing the command invocation.
        watchlist_name (str): The name of the watchlist to which the watched movies going to be displayed

        Returns:
        None
    """
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
    """
    		  Removes all the media from the watchlist

    		   Parameters:
    		   interaction (nextcord.Interaction): The interaction object representing the command invocation.
    		   watchlist_name (str): The name of the watchlist to which the watched movies going to be displayed

    		   Returns:
    		   None
    		   """
    response = media.watchlist_clear(watchlist_name)
    await interaction.response.send_message(response)


# ---------------------------------------------------------------------------
# Media Commands - View all media in a watchlist
# ---------------------------------------------------------------------------
# Functionality located in the media.py in commands folder
@bot.slash_command(guild_ids=[GUILD_ID], name="view", description="view the contents of a watchlist")
async def watchlist_view(interaction: nextcord.Interaction, watchlist_name):
    """
       Displays all the movies that have not been watched in a watchlist.

       Parameters:
       interaction (nextcord.Interaction): The interaction object representing the command invocation.
       watchlist_name (str): The name of the watchlist to which the watched movies going to be displayed

       Returns:
       None
       """
    response = watchlist.watchlist_view(watchlist_name)
    await interaction.response.send_message(response)

# ---------------------------------------------------------------------------
# Media Commands - Add tags to a specified media in a watchlist
# ---------------------------------------------------------------------------
@bot.slash_command(guild_ids=[GUILD_ID], name="add_tags", description="Add tags to a media in watchlist", default_member_permissions=EDIT_PERMISSION)
async def add_tags(interaction: nextcord.Interaction, watchlist_name, media_name, tags):
    """
    Allows users to add tags to media items in a watchlist
    Args:
        interaction (nextcord.Interaction): The interaction object representing the command invocation.
        watchlist_name str: The name of a watchlist in which the media item the user wants to add tags to is in
        media_name str: The name of the media item  (Movie/Show/Animation) the user wants to add tags to
        tags str: The tags the user wants to add to the media item in some watchlist

    Returns:
    None

    """

    # These are the tags from which the user can choose from
    VALID_TAGS = ["movie", "show", "animation", "documentary", "horror", "thriller", "sci-fi", "fantasy", "mystery", "comedy", "action", "adventure"]

    # Read in JSON data
    watchlist_data = utils.read_watchlist_file(WATCHLISTFILENAME)
    watchlist = utils.get_watchlist(watchlist_data, watchlist_name)

    if watchlist:
        if media_name in watchlist["media"]:
            # Obtain the media item and parse the tags the user has specified
            media = watchlist["media"].get(media_name)
            new_tags = [tag.strip().lower() for tag in re.split(r'[ ,]+', tags)]
            # Check which tags are valid/invalid from the ones provided by the user
            valid_tags = [tag for tag in new_tags if tag in VALID_TAGS]
            invalid_tags = [tag for tag in new_tags if tag not in VALID_TAGS]

            # If there are valid tags from the parsed tags, add them to the current tags and ensure there are no duplicate tags
            if valid_tags:
                media["tags"].extend(valid_tags)
                media["tags"] = list(set(media["tags"]))

            # If there are any invalid tags, then inform the user and list the valid tags they can instead choose from
            if invalid_tags:
                response = f"Failed to add the following tags to *{media_name}* : **{', '.join(invalid_tags)}**. \n\nPlease select tags from the following: \n**{', '.join(VALID_TAGS)}**"
            else:
                response = f"Succesfully added all tags to *{media_name}*"

        else:
            response = f"*{media_name}* not found in **{watchlist_name}**!"
    else:
        response = f"The **{watchlist_name}** watchlist does not exist!"

    utils.write_watchlist_file(WATCHLISTFILENAME, watchlist_data)
    await interaction.response.send_message(response)


@bot.slash_command(guild_ids=[GUILD_ID], name="delete_tags", description="Remove tags from a media in watchlist", default_member_permissions=EDIT_PERMISSION)
async def delete_tags(interaction: nextcord.Interaction, watchlist_name, media_name, tags):
    """
    Allows users to delete tags from certain media items in some watchlist
    Args:
        interaction (nextcord.Interaction): The interaction object representing the command invocation.
        watchlist_name: The name of the watchlist from which the user would like to delete tag(s)
        media_name: The name of the media item in some watchlist from which the user would like to delete tag(s) from
        tags: The existing tags in some media item in a watchlist

    Returns:
    None

    """
    # Read in the JSON data
    watchlist_data = utils.read_watchlist_file(WATCHLISTFILENAME)
    watchlist = utils.get_watchlist(watchlist_data, watchlist_name)

    if watchlist:
        # Ensure the media name is valid
        if media_name in watchlist["media"]:
            media = watchlist["media"].get(media_name)
            # Note that this uses regex to split the input tags based on ',' or simply a blank space to allow flexability in input
            deletion_tags = [tag.strip().lower() for tag in re.split(r'[ ,]+', tags)]

            # The new tags for the specified media item after removing the ones the user wants to delete
            new_tags = [tag for tag in media["tags"] if tag not in deletion_tags]
            # We should also find the invalid tags from the input to inform the user
            invalid_tags = [tag for tag in deletion_tags if tag not in media["tags"]]
            media["tags"] = list(set(new_tags))

            if invalid_tags:
                response = f"The following tags are either invalid tags, or already do not exist in *{media_name}*, hence could not be removed: **{', '.join(invalid_tags)}**. *{media_name}* currently has the followng tags: \n"
                response += "\n".join([f"- {name}" for name in media["tags"]])

            else:
                # Inform the user on the status of the tags for the specified media item
                if len(media["tags"]) > 0:
                    response = f"Tags successfully removed from *{media_name}*, *{media_name}* currently has the following tags:\n"
                    response += "\n".join([f"- {name}" for name in media["tags"]])
                else:
                    response = f"Tags successfully removed from *{media_name}*, *{media_name}* has no more tags, you can add some with **/add_tags**"
        else:
            response = f"*{media_name}* could not be found in the **{watchlist_name}** watchlist"

    else:
        response = f"The **{watchlist_name}** watchlist does not exist!"

    utils.write_watchlist_file(WATCHLISTFILENAME, watchlist_data)
    await interaction.response.send_message(response)


# ---------------------------------------------------------------------------
# Media Commands - Update watch status of specified media to watchlist
# ---------------------------------------------------------------------------

@bot.slash_command(guild_ids=[GUILD_ID], name="status",
                   description="update watch status of a movie or show in a watchlist")
async def watchlist_update_status(interaction: nextcord.Interaction, watch_status, media_name, watchlist_name):
    """
    Updates the watch status of specified a movie or show in a watchlist.

    Parameters:
    interaction (nextcord.Interaction): The interaction object representing the command invocation.
    watch_status (str): The watch status - unwatched, in progress or watched
    media_name (str): The name of the movie or show to update watch status of.
    watchlist_name (str): The name of the watchlist to which the movie or show to update watch status of

    Returns:
    None
    """
    watch_status = watch_status.strip().lower()
    valid_statuses = ["unwatched", "in progress", "watched"]

    # Checks if valid status input
    if watch_status in valid_statuses:

        # Read the JSON data
        watchlist_data = utils.read_watchlist_file(WATCHLISTFILENAME)

        # Check if the watchlist exists
        watchlist = utils.get_watchlist(watchlist_data, watchlist_name)
        if (watchlist != None):
            # Check if media already exists in watchlist
            if media_name in watchlist["media"]:
                media = watchlist["media"].get(media_name)
                media["status"] = watch_status
                response = f"Updated watch status of *{media_name}* to **{watch_status}** in the **{watchlist_name}** watchlist!"
            else:
                response = f"*{media_name}* is not in the **{watchlist_name}** watchlist! \nYou can add it with `/add {media_name}`"
        else:
            response = f"The **{watchlist_name}** watchlist does not exist! \nYou can create it with `/create {watchlist_name}`"

        # Write the updated JSON data
        utils.write_watchlist_file(WATCHLISTFILENAME, watchlist_data)

        await interaction.response.send_message(response)

    else:
        await interaction.response.send_message(
            "Invalid watch status. Please choose from: unwatched, in progress, watched")

# ---------------------------------------------------------------------------
# Participant Commands - Join, leave, view or notifty watchlist participants
# ---------------------------------------------------------------------------

@bot.slash_command(guild_ids=[GUILD_ID], name="join", description="join an existing watchlist")
async def watchlist_join(interaction: nextcord.Interaction, watchlist_name):
    """
        Joins the user to the watchlist

        Parameters:
        interaction (nextcord.Interaction): The interaction object representing the command invocation.
        watchlist_name (str): The name of the watchlist to which the watched movies going to be displayed

        Returns:
        None
        """
    response = participant.watchlist_join(interaction, watchlist_name)
    await interaction.response.send_message(response)

# Functionality located in the participant.py in commands folder
@bot.slash_command(guild_ids=[GUILD_ID], name="leave", description="leave from a joined watchlist")
async def watchlist_leave(interaction: nextcord.Interaction, watchlist_name):
    """
            User leaves the watchlist

            Parameters:
            interaction (nextcord.Interaction): The interaction object representing the command invocation.
            watchlist_name (str): The name of the watchlist to which the watched movies going to be displayed

            Returns:
            None
            """
    response = participant.watchlist_leave(interaction, watchlist_name)
    await interaction.response.send_message(response)

# Functionality located in the participant.py in commands folder
@bot.slash_command(guild_ids=[GUILD_ID], name="participants", description="view a watchlist's participants")
async def watchlist_participants(interaction: nextcord.Interaction, watchlist_name):
    """
    See all user in the watchlist

    Parameters:
    interaction (nextcord.Interaction): The interaction object representing the command invocation.
    watchlist_name (str): The name of the watchlist to which the watched movies going to be displayed

    Returns:
    None
    """
    response = await participant.watchlist_particpants(bot, watchlist_name)
    await interaction.response.send_message(response)

# Functionality located in the participant.py in commands folder
@bot.slash_command(guild_ids=[GUILD_ID], name="poke", description="notify all participants of a watchlist")
async def watchlist_notifyall(interaction: nextcord.Interaction, watchlist_name):
    """
    Notify all users in a watchlist

    Parameters:
    interaction (nextcord.Interaction): The interaction object representing the command invocation.
    watchlist_name (str): The name of the watchlist to which the watched movies going to be displayed

    Returns:
    None
    """
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
