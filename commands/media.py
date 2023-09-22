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
	media_name (str): The name of the movie or show to be added.
	watchlist_name (str): The name of the watchlist to which the movie or show will be added.

	Returns:
	The response message
	"""
 	# Read the JSON data
	watchlist_data = utils.read_watchlist_file(WATCHLISTFILENAME)
     
	# Check if the watchlist exists
	watchlist, response = utils.get_watchlist(watchlist_data, watchlist_name)
 
	if watchlist is None:
		return response

	# Check if media already exists in watchlist
	if media_name not in watchlist["media"]:
		# Sets media to default unwatched and makes it a dictionary so easier access
		watchlist["media"][media_name] = {"status": "unwatched", "tags": []}
		response = f"Added *{media_name}* to the **{watchlist_name}** watchlist!"
	else:
		response = f"*{media_name}* is already in the **{watchlist_name}** watchlist!"

	# Write the updated JSON data
	utils.write_watchlist_file(WATCHLISTFILENAME, watchlist_data)

	return response

#Delete media from watchlist
def watchlist_delete_media(media_name, watchlist_name):
	"""
	Removes a movie or show from a specified watchlist.

	Parameters:
	media_name (str): The name of the movie or show to be removed.
	watchlist_name (str): The name of the watchlist from which the movie or show will be removed.

	Returns:
	The response message
	"""
	# Read the JSON data
	watchlist_data = utils.read_watchlist_file(WATCHLISTFILENAME)
 
	# Check if the watchlist exists
	watchlist, response = utils.get_watchlist(watchlist_data, watchlist_name)
 
	if watchlist is None:
		return response
	
	# Check if media exists in watchlist
	if media_name in watchlist["media"]:
		watchlist["media"].pop(media_name)
		response = f"Removed *{media_name}* from the **{watchlist_name}** watchlist!"
	else:
		response = f"*{media_name}* is not in the **{watchlist_name}** watchlist!"


	# Write the updated JSON data
	utils.write_watchlist_file(WATCHLISTFILENAME, watchlist_data)
	return response

#Choose a media to watch at random from a watchlist
def watchlist_choose(watchlist_name):
	"""
	Chooses a media in a watchlist at random

	Parameters:
	watchlist_name (str): The name of the watchlist to which the watched movies going to be displayed

	Returns:
	The response message
	"""
	
 	# Read the JSON data
	watchlist_data = utils.read_watchlist_file(WATCHLISTFILENAME)
 
	# Check if the watchlist exists
	watchlist, response = utils.get_watchlist(watchlist_data, watchlist_name)
 
	if watchlist is None:
		return response

	watchlist_length = len(watchlist["media"])
	if watchlist_length == 0:
		response = f"The **{watchlist_name}** watchlist is empty. \nYou can add items to it using '/add <media_name> {watchlist_name}'"
	else:
		selected_media = random.choice(list(watchlist["media"].keys()))
		response = f"Let's watch **{selected_media}** \nTime to get out the popcorn!"
	
	return response

#Clear all media from a watchlist
def watchlist_clear(watchlist_name):
	"""
	Removes all the media from the watchlist

	Parameters:
	watchlist_name (str): The name of the watchlist to which the watched movies going to be displayed

	Returns:
	The response message
	"""
	# Read the JSON data
	watchlist_data = utils.read_watchlist_file(WATCHLISTFILENAME)
     
	# Check if the watchlist exists
	watchlist, response = utils.get_watchlist(watchlist_data, watchlist_name)
 
	if watchlist is None:
		return response

	if len(watchlist["media"]) == 0:
		response = f"The **{watchlist_name}** watchlist is already empty."
	else:
		watchlist["media"] = []  # Clear the media list
		response = f"Cleared all media from the **{watchlist_name}** watchlist."

	# Write the updated JSON data
	utils.write_watchlist_file(WATCHLISTFILENAME, watchlist_data)
	
	return response

#View a specific watchlist
def watchlist_view(watchlist_name):
	"""
	Displays all the movies that have not been watched in a watchlist.

	Parameters:
	watchlist_name (str): The name of the watchlist to which the watched movies going to be displayed

	Returns:
	The response message
	"""
	# Read the JSON data
	watchlist_data = utils.read_watchlist_file(WATCHLISTFILENAME)
 
	# Check if the watchlist exists
	watchlist, response = utils.get_watchlist(watchlist_data, watchlist_name)
 
	if watchlist is None:
		return response

	if len(watchlist["media"]) == 0:
		response = f"The **{watchlist_name}** watchlist is empty."
	else:
		response = f"Here are all of the items in the **{watchlist_name}** watchlist!\n"
		for media in watchlist["media"]:  # Print every media item
			media_status = watchlist["media"].get(media)
			if media_status["status"] == "watched":
				continue
			response += f"- {media}\n"
	
	return response
