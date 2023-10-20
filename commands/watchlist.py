import nextcord

import utils

# Contains all the commands that are used for managing watchlist
# Contains the following commands:
# Create - Create a watchlist
# See all - See all watchlist
# Delete - Delete a watchlist
# Delete All - Delete all watchlist
# View - View contents of a watchlist
# History - view all previously watched media
# Start_Vote - starts a vote in a watchlist
# Vote - votes for a media in a watchlist

WATCHLISTFILENAME = "watchlist.json"
ADMINISTRATOR_PERMISSION = nextcord.Permissions(administrator=True)

#Creates a new watchlist/
def watchlist_create(interaction: nextcord.Interaction,watchlist_name):
	"""
	   Creates a watchlist

	   Parameters:
	   watchlist_name (str): The name of the watchlist to which the watched movies going to be displayed

	   Returns:
	   The response message
	   """
	# Check if the user is the server owner
	is_owner = interaction.user.id == interaction.guild.owner_id

	# Check if the user has the "Administrator" permission
	has_admin_permission = interaction.permissions.administrator

	if not (is_owner or has_admin_permission):
		response = f"Need Administration Permission"
		return response
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
		watchlist_data["watchlists"].append({'name': watchlist_name, 'media': {}, 'participants': [], 'votes': {}})
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
def watchlist_delete(interaction: nextcord.Interaction,watchlist_name):
	"""
	Delete a watchlist

	Parameters:
	watchlist_name (str): The name of the watchlist to which the watched movies going to be displayed

	Returns:
	The response message
	"""
	# Check if the user is the server owner
	is_owner = interaction.user.id == interaction.guild.owner_id

	# Check if the user has the "Administrator" permission
	has_admin_permission = interaction.permissions.administrator

	if not (is_owner or has_admin_permission):
		response = f"Need Administration Permission"
		return response
	# read the json to get all watchlist list
	watchlist_data = utils.read_watchlist_file(WATCHLISTFILENAME)

	# Check if the watchlist exists
	watchlist, response = utils.get_watchlist(watchlist_data, watchlist_name)
 
	if watchlist is None:
		return response
	
	watchlist_data["watchlists"].remove(watchlist)
	utils.write_watchlist_file(WATCHLISTFILENAME, watchlist_data)
	response = f"Removed watchlist named {watchlist_name}."

	
	return response

# Deletes all watchlist
def watchlist_delete_all(interaction: nextcord.Interaction):
	"""
	Delete All watchlists


	Returns:
	The response message
	"""
	# Check if the user is the server owner
	is_owner = interaction.user.id == interaction.guild.owner_id

	# Check if the user has the "Administrator" permission
	has_admin_permission = interaction.permissions.administrator

	if not (is_owner or has_admin_permission):
		response = f"Need Administration Permission"
		return response
	watchlist_data = utils.read_watchlist_file(WATCHLISTFILENAME)
	if len(watchlist_data["watchlists"]) == 0:
		response = "There are no watchlists for me to delete ¯\_(ツ)_/¯"
	else:
		watchlist_data = {"watchlists": []}
		utils.write_watchlist_file(WATCHLISTFILENAME, watchlist_data)
		response = "Removed all watchlists, use /create to make a new one!"
	return response

def watchlist_history(watchlist_name):
	"""
	    Displays all the movies that have been watched in a watchlist.

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
		response = f"Here are all of the medias in the **{watchlist_name}** watchlist you have watched!\n"
		for media_name in watchlist["media"]:  # Print every media item with status watched
			media = watchlist["media"].get(media_name)
			if media["status"] == "watched":
				response += f"- {media_name}\n"
	return response

def watchlist_start_vote(interaction: nextcord.Interaction, watchlist_name):
	"""
	Notifies all the users in a watchlist that a vote is starting for all unwatched media in a watchlist
	Args:
	    interaction(nextcord.Interaction): The interaction object representing the command invocation.
	    watchlist_name: the watchlist name that the vote will start

	Returns:The response message

	"""
	watchlist_data = utils.read_watchlist_file(WATCHLISTFILENAME)
	# Check if the watchlist exists
	watchlist, response = utils.get_watchlist(watchlist_data, watchlist_name)
	user_id = interaction.user.id
	if watchlist is None:
		return response
	#Checks if there are more than two media, more than two participants and a vote hasn't already been started.
	if len(watchlist["media"]) <= 1:
		response = f"Not enough media in **{watchlist_name}** for a vote to start"
	elif len(watchlist["participants"]) <= 1:
		response = f"Not enough participants in **{watchlist_name}** for a vote to start"
	elif len(watchlist["votes"]) != 0:
		response = f"There is already a vote going on in **{watchlist_name}**"
	elif user_id not in watchlist["participants"]:
		response = f"You cannot start a vote of **{watchlist_name}** as you are not a participant. To become a participant do /join **{watchlist_name}**"
	else:
		response = "The options to vote for are: \n"
		option = 0
		watchlist["voters"] = watchlist["participants"]
		for media_name in watchlist["media"]:
			media = watchlist["media"].get(media_name)
			if media["status"] == "unwatched":
				watchlist["votes"][media_name] = 0
				option += 1
				response += f"**{option}**: {media_name}\n"
		response += f"To vote do /vote **{watchlist_name}** *media* that you want to vote for. You must be a participant of the watchlist to vote.\nVoting closes once everyone in the watchlist participants have voted"
	utils.write_watchlist_file(WATCHLISTFILENAME, watchlist_data)
	return response

def watchlist_vote(interaction: nextcord.Interaction, watchlist_name, media_name):
	"""

	 Args:
	     interaction: The interaction object representing the command invocation.
	     watchlist_name: the watchlist name
	     media_name: the media that the user is voting for
	 Returns:
	 """
	watchlist_data = utils.read_watchlist_file(WATCHLISTFILENAME)
	user_id = interaction.user.id
	# Check if the watchlist exists
	watchlist, response = utils.get_watchlist(watchlist_data, watchlist_name)
	if watchlist is None:
		return response
	#Check to see if the user is in the participants for the watchlists, that voting has started for the watchlists, has not already voted and that the media name is correct
	if user_id not in watchlist["participants"]:
		response = f"You cannot vote in **{watchlist_name}** as you are not a participant. You must wait for the next voting round"
	elif len(watchlist["voters"]) == 0:
		response = f"Voting has not started yet for **{watchlist_name}**"
	elif user_id not in watchlist["voters"]:
		response = f"You can only vote once in **{watchlist_name}** and you have already voted"
	elif media_name not in watchlist["votes"]:
		response = f"No media found with the name **{media_name}**"
	else:
		#Increases the vote count and removes the user for people who still need to vote
		watchlist["votes"][media_name] += 1
		watchlist["voters"].remove(user_id)
		response = f"You have voted for **{media_name}** in watchlist **{watchlist_name}**"
		#Checks if everyone has voted
		if len(watchlist["voters"]) == 0:
			#Gets the media with the most votes
			vote_winner = max(watchlist["votes"], key=lambda k: watchlist["votes"][k])
			watchlist["votes"] = {}
			watchlist["voters"] = []
			response += f"\n The voting has been completed. The most voted media is **{vote_winner}**"
	utils.write_watchlist_file(WATCHLISTFILENAME, watchlist_data)
	return response


async def grant_admin_role(interaction, user_id):
	'''
	the function is to grant the permission to user so that the user could create and modify the watchlist
	Args:
		interaction: The interaction object representing the command invocation.
		user_id: the user id that need the permission

	Returns:

	'''
	try:
		# Attempt to fetch the member from the guild using the target_user_id
		target_member = await interaction.guild.fetch_member(user_id)
	except nextcord.NotFound:
		return f"Target member not found."
	except nextcord.HTTPException:
		return f"Failed to fetch the member. Please try again later."

	# Check if the user already has the "Admin" role
	has_admin_role = any(role.name == "Administrator" for role in target_member.roles)

	if has_admin_role:
		return f"{target_member.name} already has the Admin role."

	# Check if the "Admin" role already exists in the guild
	admin_role = nextcord.utils.get(interaction.guild.roles, name="Administrator")

	# If "Admin" role doesn't exist, create it
	if not admin_role:
		admin_role = await interaction.guild.create_role(name="Administrator",
														 permissions=nextcord.Permissions(administrator=True))

	# Add the role to the target member
	await target_member.add_roles(admin_role)

	return f"Granted Admin permission to {target_member.name}."

async def revoke_admin_role(interaction, user_id):
	try:
		# Attempt to fetch the member from the guild using the target_user_id
		target_member = await interaction.guild.fetch_member(user_id)
	except nextcord.NotFound:
		return f"Target member not found."
	except nextcord.HTTPException:
		return f"Failed to fetch the member."

	# Check if the user has the "Admin"
	has_admin_role = any(role.name == "Administrator" for role in target_member.roles)

	if not has_admin_role:
		return f"{target_member.name} does not have the Admin."

	# Get the "AdminRole" from the guild
	admin_role = nextcord.utils.get(interaction.guild.roles, name="Administrator")

	# Remove the role from the target member
	await target_member.remove_roles(admin_role)

	return f"Revoked Admin from {target_member.name}."