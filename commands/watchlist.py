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
def create(watchlist_name):
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
		watchlist_data["watchlists"].append({'name': watchlist_name, 'media': [], 'participants': []})
		utils.write_watchlist_file(WATCHLISTFILENAME, watchlist_data)
		response = f"Created a new watchlist named {watchlist_name}. Add movies and shows to your new watchlist!"
	return response

# Sees all the watchlist
def see_all():
	# read the json to get all watchlist lists
	watchlist_data = utils.read_watchlist_file(WATCHLISTFILENAME)

	if len(watchlist_data["watchlists"]) == 0:  # Respond if there are no watchlists
		response = "You have no watchlists right now, create a watchlist with /create and you will see it here!"
	else:
		response = "Here are all of your watchlists!\n\n"
		for watchlist in watchlist_data["watchlists"]:  # Print every watchlist
			name = watchlist["name"]
			response += f"{name}\n"
			if len(watchlist["media"]) == 0:  # Respond if watchlist has no media
				response += "- There are no items in this watchlist right now\n"
			else:
				for media in watchlist["media"]:  # Print every media item
					response += f"- {media}\n"
			response += "\n\n"
	return response

# Deletes a watchlist
def delete(watchlist_name):
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
def delete_all():
	watchlist_data = utils.read_watchlist_file(WATCHLISTFILENAME)
	if len(watchlist_data["watchlists"]) == 0:
		response = "There are no watchlists for me to delete ¯\_(ツ)_/¯"
	else:
		watchlist_data = {"watchlists": []}
		utils.write_watchlist_file(WATCHLISTFILENAME, watchlist_data)
		response = "Removed all watchlists, use /create to make a new one!"
	return response
def view(watchlist_name):
	# read the json to get all watchlist list
	watchlist_data = utils.read_watchlist_file(WATCHLISTFILENAME)
	# Find the watchlist
	watchlist = utils.get_watchlist(watchlist_data, watchlist_name)
	if (watchlist != None):
		if len(watchlist["media"]) == 0:
			response = f"The **{watchlist_name}** watchlist is empty."
		else:
			response = f"Here are all of the items in the **{watchlist_name}** watchlist!\n"
			for media in watchlist["media"]:  # Print every media item
				response += f"- {media}\n"
	else:
		response = f"Watchlist named {watchlist_name} does not exist."
	return response