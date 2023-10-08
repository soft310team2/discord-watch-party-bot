import os
from dotenv import load_dotenv
import nextcord
from nextcord.ext import commands
import random
import utils
# importing the other python files
from commands import misc, media, watchlist, participant

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
    utils.init_watchlist_json(WATCHLISTFILENAME)


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
    response = watchlist.watchlist_history(watchlist_name)
    await interaction.response.send_message(response)

@bot.slash_command(guild_ids=[GUILD_ID], name="start_vote", description="start a vote to determine what media to watch")
async def watchlist_vote_start(interaction: nextcord.Interaction, watchlist_name):
    """
    Notifies all the users in a watchlist that a vote is starting for all unwatched media in a watchlist
    Args:
        interaction(nextcord.Interaction): The interaction object representing the command invocation.
        watchlist_name: the watchlist name that the vote will start

    Returns:None

    """
    response = watchlist.watchlist_start_vote(interaction, watchlist_name)
    await interaction.response.send_message(response)

@bot.slash_command(guild_ids=[GUILD_ID], name="vote", description="add a vote to the watchlist")
async def watchlist_vote(interaction: nextcord.Interaction, watchlist_name, media_name):
    """

    Args:
        interaction: The interaction object representing the command invocation.
        watchlist_name: the watchlist name
        media_name: the media that the user is voting for
    Returns:
    """

    response = watchlist.watchlist_vote(interaction, watchlist_name, media_name)
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
    response = media.watchlist_view(watchlist_name)
    await interaction.response.send_message(response)


# ---------------------------------------------------------------------------
# Media Commands - Add tags to a specified media in a watchlist
# ---------------------------------------------------------------------------
# Functionality located in the media.py in commands folder
@bot.slash_command(guild_ids=[GUILD_ID], name="add_tags", description="Add tags to a media in watchlist",
                   default_member_permissions=EDIT_PERMISSION)
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

    response = media.add_tags(watchlist_name, media_name, tags)
    await interaction.response.send_message(response)


# ---------------------------------------------------------------------------
# Media Commands - Deletes a tag to a specified media in a watchlist
# ---------------------------------------------------------------------------
# Functionality located in the media.py in commands folder
@bot.slash_command(guild_ids=[GUILD_ID], name="delete_tags", description="Remove tags from a media in watchlist",
                   default_member_permissions=EDIT_PERMISSION)
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
    response = media.delete_tags(watchlist_name, media_name, tags)
    await interaction.response.send_message(response)


# ---------------------------------------------------------------------------
# Media Commands - Update watch status of specified media to watchlist
# ---------------------------------------------------------------------------
# Functionality located in the media.py in commands folder
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

    response = media.watchlist_update_status(watch_status, media_name, watchlist_name)
    await interaction.response.send_message(response)


# ---------------------------------------------------------------------------
# Media Commands - Filter media by a tag
# ---------------------------------------------------------------------------
# Functionality located in the media.py in commands folder
@bot.slash_command(guild_ids=[GUILD_ID], name="filter_by_tags",
                   description="view filtered medias based on tags in a watchlist")
async def filter_tags(interaction: nextcord.Interaction, watchlist_name, tags):
    """
    Display all the media that filtered based on tags in a watchlist.
    Args:
        interaction: The interaction object representing the command invocation.
        watchlist_name: The name of the watchlist to which the watched movies going to be displayed
        tags: The tags that want to be based on to filter

    Returns:
    None

    """
    response = media.filter_tags(watchlist_name, tags)
    await interaction.response.send_message(response)


# ---------------------------------------------------------------------------
# Media Commands - Pick a random media based on tag
# ---------------------------------------------------------------------------
# Functionality located in the media.py in commands folder
@bot.slash_command(guild_ids=[GUILD_ID], name="random_select_by_tags",
                   description="view a randomly seleted filtered media based on tags in a watchlist")
async def random_tags(interaction: nextcord.Interaction, watchlist_name, tags):
    """
    Display a random selected media that filtered based on tags in a watchlist.
    Args:
        interaction: The interaction object representing the command invocation.
        watchlist_name: The name of the watchlist to which the watched movies going to be displayed
        tags: The tags that want to be based on to filter

    Returns:
    None

    """
    response = media.random_tags(watchlist_name, tags)
    await interaction.response.send_message(response)


# ---------------------------------------------------------------------------
# Participant Commands - Join, leave, view or notifty watchlist participants
# ---------------------------------------------------------------------------
# Functionality located in the participant.py in commands folder
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

# Functionality located in the participant.py in commands folder
@bot.slash_command(guild_ids=[GUILD_ID], name="event", description="Create a watch party event for users")
async def create_event(interaction: nextcord.Interaction, media_name, location, date):
    """
    Create a discord event to watch the media

    Parameters:
    interaction (nextcord.Interaction): The interaction object representing the command invocation.
    media_name (str): The name of the media the event is about
    location (str): Where the media watching event will take place
    date (str): The date and time of when the event will take place

    Returns:
    None
    """
    response = await participant.create_event(interaction, media_name, location, date)
    await interaction.response.send_message(f"Created a watch party event for {media_name}!")

# ---------------------------------------------------------------------------
# Media Commands - Add description to a media
# ---------------------------------------------------------------------------
# Functionality located in the media.py in commands folder
@bot.slash_command(guild_ids=[GUILD_ID], name="add_description", description="add the description of a media")
async def add_description(interaction: nextcord.Interaction, watchlist_name, media_name, description):
    """
	Add the description to a particular media

	Parameters:
    interaction (nextcord.Interaction): The interaction object representing the command invocation.
    watchlist_name (str): The name of the watchlist to which the watched movies going to be displayed
    media_name (str): The name of the movie or show to be examined.
    description: the description of that media

    Returns:
    None
    """
    response = media.add_description(watchlist_name, media_name, description)
    await interaction.response.send_message(response)


# ---------------------------------------------------------------------------
# Media Commands - Delete description of a media
# ---------------------------------------------------------------------------
# Functionality located in the media.py in commands folder
@bot.slash_command(guild_ids=[GUILD_ID], name="delete_description", description="delete the description of a media")
async def delete_description(interaction: nextcord.Interaction, watchlist_name, media_name):
    """
	Delete the description of a particular media

	Parameters:
    interaction (nextcord.Interaction): The interaction object representing the command invocation.
    watchlist_name (str): The name of the watchlist to which the watched movies going to be displayed
    media_name (str): The name of the movie or show to be examined.
    description: the description of that media

    Returns:
    None
    """
    response = media.delete_description(watchlist_name, media_name)
    await interaction.response.send_message(response)


# ---------------------------------------------------------------------------
# Media Commands - View description to a media
# ---------------------------------------------------------------------------
# Functionality located in the media.py in commands folder
@bot.slash_command(guild_ids=[GUILD_ID], name="description", description="view the description of a media")
async def watchlist_description(interaction: nextcord.Interaction, watchlist_name, media_name):
    """
    View the description of a particular media

    Parameters:
    interaction (nextcord.Interaction): The interaction object representing the command invocation.
    watchlist_name (str): The name of the watchlist to which the watched movies going to be displayed
    media_name (str): The name of the movie or show to be examined.

    Returns:
    None
    """
    response = media.watchlist_description(watchlist_name, media_name)
    await interaction.response.send_message(response)

@bot.slash_command(guild_ids=[GUILD_ID], name="add_review", description="Add a review to an existing media")
async def add_review(interaction: nextcord.Interaction, watchlist_name, media_name, review_text):
    """
    Add a review to a media item in some watchlist

    Args:
        interaction: The interaction object representing the command invocation.
        watchlist_name: The name of the watchlist in which the media item specified is located in
        media_name: The name of the media item which the user wishes to review
        review_text: The review the user wishes to add to the media item

    Returns:
        None

    """
    response = media.add_review(watchlist_name, media_name, review_text, interaction.user.name)
    await interaction.response.send_message(response)


@bot.slash_command(guild_ids=[GUILD_ID], name="see_reviews", description="See all reviews for a media")
async def view_review(interaction: nextcord.Interaction, watchlist_name, media_name):
    response = media.view_reviews(watchlist_name, media_name)

    await interaction.response.send_message(response)

@bot.slash_command(guild_ids=[GUILD_ID], name="add_rating", description="Add a rating to an existing media")
async def add_review(interaction: nextcord.Interaction, watchlist_name, media_name, rating):
    """
    Add a rating to a media item in some watchlist

    Args:
        interaction: The interaction object representing the command invocation.
        watchlist_name: The name of the watchlist in which the media item specified is located in
        media_name: The name of the media item which you wish to rate
        rating: A 0-5 rating you wish to add to the media item. 

    Returns:
        None

    """
    response = media.add_rating(rating, media_name, watchlist_name)
    await interaction.response.send_message(response)


@bot.slash_command(guild_ids=[GUILD_ID], name="see_rating", description="See average rating information of all media in a watchlist")
async def view_rating(interaction: nextcord.Interaction, watchlist_name):
    response = media.view_rating(watchlist_name)

    await interaction.response.send_message(response)
    
# ---------------------------------------------------------------------------
# Media Commands - Filter media by a rating
# ---------------------------------------------------------------------------
# Functionality located in the media.py in commands folder
@bot.slash_command(guild_ids=[GUILD_ID], name="filter_by_rating",
                   description="view filtered medias by rating in a watchlist")
async def filter_rating(interaction: nextcord.Interaction, watchlist_name, rating):
    """
    Display all the media with at least a given rating in a watchlist.
    Args:
        interaction: The interaction object representing the command invocation.
        watchlist_name: The name of the watchlist to which the watched movies going to be displayed
        rating: The rating that media must meet or have above to be displayed

    Returns:
    None

    """
    response = media.filter_rating(watchlist_name, rating)
    await interaction.response.send_message(response)
    
bot.run(BOT_TOKEN)
