import random
import nextcord


# Contains all commands that don't fit into the other categories
# Commands that are include:
# Ping
# Popcorn
# Help

# Returns pong to test that the bot is working
def ping():
	return "Pong!"

# Returns the number of popcorn scooped and kernels that the user has scooped

def popcorn(interaction: nextcord.Interaction):
	popcorn = random.randint(1, 100)
	kernels = random.randint(0, popcorn)
	response = f"{interaction.user.display_name} scooped {popcorn} bits of popcorn, "
	if kernels == 0:
		response += "and no kernels! :popcorn:"
		if popcorn == 100:
			response += " NOW THAT'S A BUTTERY BUCKET :butter:"
	elif kernels == popcorn:
		response += "but ALL OF THEM ARE JUST KERNELS :skull:"
	else:
		response += f"but {kernels} of them are just kernels!"
	return response


# Shows all the commands that the bots has
def help():
	'''
	A list of all the commands that are avaliable for the bot
	Returns:The list of commands that the bot has
	'''
	response = "Here are all of my commands:\n\n"
	response += "**/create** \n- create a new watchlist\n\n"
	response += "**/delete** \n- delete an existing watchlist\n\n"
	response += "**/deleteall** \n- delete all existing watchlists\n\n"
	response += "**/seeall** \n- see all watchlists\n\n"
	response += "**/add** \n- add a movie or show to a watchlist\n\n"
	response += "**/remove** \n- remove a movie or show from a watchlist\n\n"
	response += "**/clear** \n- remove all media from a watchlist\n\n"
	response += "**/view** \n- view the contents of a wishlist\n\n"
	response += "**/join** \n- join an existing watchlist\n\n"
	response += "**/leave** \n- leave from a joined watchlist\n\n"
	response += "**/participants** \n- view a watchlist's participants\n\n"
	response += "**/poke** \n- notify all participants of a watchlist\n\n"
	response += "**/choose** \n- select a random item from a watchlist\n\n"
	response += "**/status** \n- update watch status of a movie or show in a watchlist\n\n"
	response += "**/history** \n- display all the watched movies in a watchlist\n\n"
	response += "**/filter_by_tags** \n- display all the filtered movies based on tags in a watchlist\n\n"
	response += "**/random_select_by_tags** \n- display a random filtered movies based on tags in a watchlist\n\n"
	response += "**/add_tags** \n- Add any of the following tags to a media item: ***movie, show, animation, documentary, horror, thriller, sci-fi, fantasy, mystery, comedy, action, adventure*** \n\n"
	response += "**/delete_tags** \n- Remove added tags from a media item in some watchlist"
	response += "**/start_vote** \n- Starts a vote for the watchlist"
	response += "**/vote** \n- Adds a vote for a media in a watchlist"
	response += "**/delete_tags** \n- Remove added tags from a media item in some watchlist\n\n"
	response += "**/add_description** \n- Add the description to a media\n\n"
	response += "**/delete_description** \n- Delete the description to a media\n\n"
	response += "**/description** \n- View the description of a media\n\n"
	response += "**/add_review** \n- Add a review to a media in some watchlist \n\n"
	response += "**/see_reviews** \n- See all the reviews left by others in the server for some media \n\n"
	return response
