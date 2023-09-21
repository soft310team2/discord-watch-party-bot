import utils

# Contains all the commands that are used for managing watchlist
# Contains the following commands:
# Create - Create a watchlist
# See all - See all watchlist
# Delete - Delete a watchlist
# Delete All - Delete all watchlist
# View - View contents of a watchlist

WATCHLISTFILENAME = "watchlist.json"

#Creates a new watchlist
def watchlist_create(watchlist_name):
	"""
	   Creates a watchlist

	   Parameters:
	   watchlist_name (str): The name of the watchlist to which the watched movies going to be displayed

	   Returns:
	   The response message
	   """
	# read the json to get all watchlist lists
	watchlist_data = utils.read_watchlist_file(WATCHLISTFILENAME)

	# Check if the watchlist exists already
	watchlist_exists = False
	for watchlist in watchlist_data["watchlists"]:
		if watchlist["name"] == watchlist_name:
			watchlist_exists = True

	# Only create the watchlist if it does not already exist
	if watchlist_exists:
		response = f"A watchlist named {watchlist_name} already exists!"
	else:
		# write in the new watchlist to the json
		watchlist_data["watchlists"].append({'name': watchlist_name, 'media': {}, 'participants': []})
		utils.write_watchlist_file(WATCHLISTFILENAME, watchlist_data)
		response = f"Created a new watchlist named {watchlist_name}. Add movies and shows to your new watchlist!"
	return response

# Sees all the watchlist
def watchlist_see_all():
	"""
	   See all watchlists

	   Parameters:
	   watchlist_name (str): The name of the watchlist to which the watched movies going to be displayed

	   Returns:
	   The response message
	   """
	# read the json to get all watchlist lists
	watchlist_data = utils.read_watchlist_file(WATCHLISTFILENAME)

	if len(watchlist_data["watchlists"]) == 0:  # Respond if there are no watchlists
		response = "You have no watchlists right now, create a watchlist with /create and you will see it here!"
	else:
		response = "Here are all of your watchlists!\n\n"
		for watchlist in watchlist_data["watchlists"]:  # Print every watchlist
			response += format_watchlist(watchlist)
   
	return response

# Format a watchlist
def format_watchlist(watchlist):
    name = watchlist["name"]
    response = f"{name}\n"
    
    if len(watchlist["media"]) == 0:  # Respond if watchlist has no media
        response += "- There are no items in this watchlist right now\n"
    else:
        for media in watchlist["media"]:  # Print every media item
            response += format_media(media, watchlist["media"].get(media))
            
    response += "\n\n"

    return response


# Format a media
def format_media(media, media_values):
    
    # Extract the tags for this media
    media_tags = media_values.get("tags", [])
    
    # Check if the medis have the media if not make the tag part become NONE
    if media_tags:
        tags_string = ', '.join(media_tags)  # Convert tags list to a comma-separated string
    else:
        tags_string = "NONE"
    
    # Check if the media is watched
    if media_values.get("status") == "watched":
        return ""

    # Add the media name and its associated tags to the response
    response = f"- {media} (Tags: {tags_string})\n"
    
    return response

    
# Deletes a watchlist
def watchlist_delete(watchlist_name):
	"""
	Delete a watchlist

	Parameters:
	watchlist_name (str): The name of the watchlist to which the watched movies going to be displayed

	Returns:
	The response message
	"""
	# read the json to get all watchlist list
	watchlist_data = utils.read_watchlist_file(WATCHLISTFILENAME)

	# Find watchlist
	watchlist = utils.get_watchlist(watchlist_data, watchlist_name)
	if (watchlist != None):
		watchlist_data["watchlists"].remove(watchlist)
		utils.write_watchlist_file(WATCHLISTFILENAME, watchlist_data)
		response = f"Removed watchlist named {watchlist_name}."

	else:
		response = f"Watchlist named {watchlist_name} does not exist"
	return response

# Deletes all watchlist
def watchlist_delete_all():
	"""
	Delete All watchlists


	Returns:
	The response message
	"""
	watchlist_data = utils.read_watchlist_file(WATCHLISTFILENAME)
	if len(watchlist_data["watchlists"]) == 0:
		response = "There are no watchlists for me to delete ¯\_(ツ)_/¯"
	else:
		watchlist_data = {"watchlists": []}
		utils.write_watchlist_file(WATCHLISTFILENAME, watchlist_data)
		response = "Removed all watchlists, use /create to make a new one!"
	return response

