import utils
import random
# Commands that have to do with modifying an indivdual watchlist
# Add - adds a media to a watchlist
# Remove - removes a media from a watchlist
# Choose - chooses a random media from watchlist
# Clear - clears all the media from watchlist

WATCHLISTFILENAME = "watchlist.json"

# Adds media to watchlist
def watchlist_add(media_name, watchlist_name):
	"""
	    Adds a movie or show to a specified watchlist.

	    Parameters:
	    interaction (nextcord.Interaction): The interaction object representing the command invocation.
	    media_name (str): The name of the movie or show to be added.
	    watchlist_name (str): The name of the watchlist to which the movie or show will be added.

	    Returns:
	    None
	    """
	# Read the JSON data
	watchlist_data = utils.read_watchlist_file(WATCHLISTFILENAME)

	# Check if the watchlist exists
	watchlist = utils.get_watchlist(watchlist_data, watchlist_name)
	if (watchlist != None):
		# Check if media already exists in watchlist
		if media_name not in watchlist["media"]:
			watchlist["media"].append(media_name)
			response = f"Added *{media_name}* to the **{watchlist_name}** watchlist!"
		else:
			response = f"*{media_name}* is already in the **{watchlist_name}** watchlist!"
	else:
		response = f"The **{watchlist_name}** watchlist does not exist! \nYou can create it with `/watchlist_create {watchlist_name}`"

	# Write the updated JSON data
	utils.write_watchlist_file(WATCHLISTFILENAME, watchlist_data)

	return response

def watchlist_delete_media(media_name, watchlist_name):
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
	watchlist_data = utils.read_watchlist_file(WATCHLISTFILENAME)

	# Check if the watchlist exists
	watchlist = utils.get_watchlist(watchlist_data, watchlist_name)
	if (watchlist != None):
		# Check if media exists in watchlist
		if media_name in watchlist["media"]:
			watchlist["media"].remove(media_name)
			response = f"Removed *{media_name}* from the **{watchlist_name}** watchlist!"
		else:
			response = f"*{media_name}* is not in the **{watchlist_name}** watchlist!"

	else:
		response = f"The **{watchlist_name}** watchlist does not exist!"

	# Write the updated JSON data
	utils.write_watchlist_file(WATCHLISTFILENAME, watchlist_data)
	return response

def watchlist_choose(watchlist_name):
	watchlist_data = utils.read_watchlist_file(WATCHLISTFILENAME)

	watchlist = utils.get_watchlist(watchlist_data, watchlist_name)
	if (watchlist != None):
		watchlist_length = len(watchlist["media"])
		if watchlist_length == 0:
			response = f"The **{watchlist_name}** watchlist is empty. \nYou can add items to it using '/add <media_name> {watchlist_name}'"
		else:
			selected_media = random.choice(watchlist["media"])
			response = f"Let's watch **{selected_media}** \nTime to get out the popcorn!"
	else:
		response = f"The **{watchlist_name}** watchlist does not exist! \nYou can create it with `/create {watchlist_name}`"
	return response

def watchlist_clear(watchlist_name):
	# Read the JSON data
	watchlist_data = utils.read_watchlist_file(WATCHLISTFILENAME)

	# Find the watchlist
	watchlist = utils.get_watchlist(watchlist_data, watchlist_name)
	if (watchlist != None):
		if len(watchlist["media"]) == 0:
			response = f"The **{watchlist_name}** watchlist is already empty."
		else:
			watchlist["media"] = []  # Clear the media list
			response = f"Cleared all media from the **{watchlist_name}** watchlist."

		# Write the updated JSON data
		utils.write_watchlist_file(WATCHLISTFILENAME, watchlist_data)
	else:
		response = f"Watchlist named {watchlist_name} does not exist."
	return response
