import nextcord
import utils

#Commands that have to do with users joining the watchlist

WATCHLISTFILENAME = "watchlist.json"
def watchlist_join(interaction: nextcord.Interaction, watchlist_name):
	# read the json to get all watchlist list
	watchlist_data = utils.read_watchlist_file(WATCHLISTFILENAME)

	# add participant to watchlist
	user_id = interaction.user.id
	watchlist = utils.get_watchlist(watchlist_data, watchlist_name)
	if (watchlist != None):
		# check duplication
		if (user_id in watchlist["participants"]):
			response = "You are already in this watchlist."

		else:
			watchlist["participants"].append(user_id)
			# write the change to json
			utils.write_watchlist_file(WATCHLISTFILENAME, watchlist_data)
			response = f"You have joined the {watchlist_name} watchlist."
	else:
		response = f"Watchlist named {watchlist_name} does not exist"
	return response
def watchlist_leave(interaction: nextcord.Interaction, watchlist_name):
	# read the json to get all watchlist list
	watchlist_data = utils.read_watchlist_file(WATCHLISTFILENAME)

	# Check if the watchlist exists
	user_id = interaction.user.id
	watchlist = utils.get_watchlist(watchlist_data, watchlist_name)
	if (watchlist != None):
		# Check if user id is in the participants list
		if (user_id in watchlist["participants"]):
			watchlist["participants"].remove(user_id)
			# write the change to json
			utils.write_watchlist_file(WATCHLISTFILENAME, watchlist_data)
			response = f"You have been removed from the {watchlist_name} watchlist."

		else:
			response = "You are not currently in this watchlist"
	else:
		response = f"Watchlist named {watchlist_name} does not exist"
	return response

async def watchlist_particpants(bot, watchlist_name):
	# read the json to get all watchlist list
	watchlist_data = utils.read_watchlist_file(WATCHLISTFILENAME)

	# Find watchlist
	watchlist = utils.get_watchlist(watchlist_data, watchlist_name)
	if (watchlist != None):
		# Print Members
		response = f"Participants of {watchlist_name} watchlist:\n"
		for user_id in watchlist["participants"]:
			user = await bot.fetch_user(user_id)  # This is an api call, must use await then get the name component step by step
			user_name = user.name
			response += "- " + user_name + "\n"
		if len(watchlist["participants"]) == 0:
			response = f"There are no participants in {watchlist_name} yet  :("
	else:
		response = f"Watchlist named {watchlist_name} does not exist"
	return response

def watchlist_notifyall(watchlist_name):
	# read the json to get all watchlist list
	watchlist_data = utils.read_watchlist_file(WATCHLISTFILENAME)
	# add participant to watchlist
	watchlist = utils.get_watchlist(watchlist_data, watchlist_name)
	if (watchlist != None):
		mentions = ' '.join(f'<@{user_id}>' for user_id in
		                    watchlist["participants"])  # Generate string of mentions in space-separated manner
		response = f'A watch party for the {watchlist_name} watchlist is starting soon! {mentions}'

	else:
		response = f"Watchlist named {watchlist_name} does not exist"
	return response
