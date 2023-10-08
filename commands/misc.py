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

    response += "**/create** \n- Create a new watchlist\n\n"
    response += "**/delete** \n- Delete an existing watchlist\n\n"
    response += "**/deleteall** \n- Delete all existing watchlists\n\n"
    response += "**/seeall** \n- See all watchlists\n\n"
    response += "**/add** \n- Add a movie or show to a watchlist\n\n"
    response += "**/remove** \n- Remove a movie or show from a watchlist\n\n"
    response += "**/clear** \n- Remove all media from a watchlist\n\n"
    response += "**/view** \n- View the contents of a wishlist\n\n"
    response += "**/join** \n- Join an existing watchlist\n\n"
    response += "**/leave** \n- Leave from a joined watchlist\n\n"
    response += "**/participants** \n- View a watchlist's participants\n\n"
    response += "**/poke** \n- Notify all participants of a watchlist\n\n"
    response += "**/choose** \n- Select a random item from a watchlist\n\n"
    response += "**/event** \n- Create a discord watchparty event\n\n"
    response += "**/status** \n- Update watch status of a movie or show in a watchlist\n\n"
    response += "**/history** \n- Display all the watched movies in a watchlist\n\n"
    response += "**/filter_by_tags** \n- Display all the filtered movies based on tags in a watchlist\n\n"
    response += "**/random_select_by_tags** \n- Display a random filtered movies based on tags in a watchlist\n\n"
    response += "**/add_tags** \n- Add any of the following tags to a media item: ***movie, show, animation, documentary, horror, thriller, sci-fi, fantasy, mystery, comedy, action, adventure*** \n\n"
    response += "**/delete_tags** \n- Remove added tags from a media item in some watchlist\n\n"
    response += "**/start_vote** \n- Starts a vote for the watchlist\n\n"
    response += "**/vote** \n- Adds a vote for a media in a watchlist\n\n"
    response += "**/add_description** \n- Add the description to a media\n\n"
    response += "**/delete_description** \n- Delete the description to a media\n\n"
    response += "**/description** \n- View the description of a media\n\n"
    response += "**/add_review** \n- Add a review to a media in some watchlist \n\n"
    response += "**/see_reviews** \n- See all the reviews left by others in the server for some media \n\n"
    response += "**/entitle_permission** \n- Give the user permission by userID \n\n"
    response += "**/remove_permission** \n- Remove the user permission by userID \n\n"
    response += "**/get_user_id** \n- Get user ID \n\n"
    response += "**/add_rating** \n- Add a rating to a media in some watchlist \n\n"
    response += "**/see_rating** \n- See average rating information of all media in a watchlist \n\n"
    response += "**/filter_by_rating** \n- Display all the filtered movies with a given rating or above in a watchlist\n\n"

    return response
