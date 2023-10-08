import random
import re
import utils

# Commands that have to do with modifying an indivdual watchlist
# Add - adds a media to a watchlist
# Remove - removes a media from a watchlist
# Choose - chooses a random media from watchlist
# Clear - clears all the media from watchlist
# Add_tag - adds a tag to media
# Delete_tag - removes a tag from media
# Status - updates the watch status of a media
# Filter_by_tag - displays media based on a tag
# Random_select_by_tag - selects a random media to watch based on a tag
# Add_rating - adds a rating to a media
# View_rating - view a rating of a media
# Filter_rating - displays media based on a rating


WATCHLISTFILENAME = "watchlist.json"
VALID_TAGS = ["movie", "show", "animation", "documentary", "horror", "thriller", "sci-fi", "fantasy", "mystery",
              "comedy", "action", "adventure"]


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
        watchlist["media"][media_name] = {"status": "unwatched", "tags": [], "reviews": [], "description": "none", "rating": [-1, 0]}
        response = f"Added *{media_name}* to the **{watchlist_name}** watchlist!"
    else:
        response = f"*{media_name}* is already in the **{watchlist_name}** watchlist!"

    # Write the updated JSON data
    utils.write_watchlist_file(WATCHLISTFILENAME, watchlist_data)

    return response


# Delete media from watchlist
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


# Choose a media to watch at random from a watchlist
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


# Clear all media from a watchlist
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


# View a specific watchlist
def allWatched(mediaList):
    total = len(mediaList)
    watched = 0
    for media in mediaList:
        media_status = mediaList.get(media)
        if media_status["status"] == "watched":
            watched += 1;
    return total == watched


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
    elif allWatched(watchlist['media']):
        response = f"You've already watched everything in **{watchlist_name}**!"
    else:
        response = f"Here are all of the items in the **{watchlist_name}** watchlist!\n"
        for media in watchlist["media"]:  # Print every media item
            media_status = watchlist["media"].get(media)
            if media_status["status"] == "watched":
                continue
            response += f"- {media}\n"

    return response


# Adds a tag to a media
def add_tags(watchlist_name, media_name, tags):
    """
	    Allows users to add tags to media items in a watchlist
	    Args:
	        watchlist_name str: The name of a watchlist in which the media item the user wants to add tags to is in
	        media_name str: The name of the media item  (Movie/Show/Animation) the user wants to add tags to
	        tags str: The tags the user wants to add to the media item in some watchlist

	    Returns:
	    The response message

	    """
    # Read in JSON data
    watchlist_data = utils.read_watchlist_file(WATCHLISTFILENAME)
    watchlist, response = utils.get_watchlist(watchlist_data, watchlist_name)

    if watchlist is None:
        return response

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

    utils.write_watchlist_file(WATCHLISTFILENAME, watchlist_data)
    return response


# Removes a tag from media
def delete_tags(watchlist_name, media_name, tags):
    """
	    Allows users to delete tags from certain media items in some watchlist
	    Args:
	        watchlist_name: The name of the watchlist from which the user would like to delete tag(s)
	        media_name: The name of the media item in some watchlist from which the user would like to delete tag(s) from
	        tags: The existing tags in some media item in a watchlist

	    Returns:
	    The reseponse message

	    """
    # Read in the JSON data
    watchlist_data = utils.read_watchlist_file(WATCHLISTFILENAME)
    watchlist, response = utils.get_watchlist(watchlist_data, watchlist_name)

    if watchlist is None:
        return response

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
            response = f"The following tags are either invalid tags, or already do not exist in *{media_name}*, hence could not be removed: **{', '.join(invalid_tags)}**. *{media_name}* currently has the following tags: \n"
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

    utils.write_watchlist_file(WATCHLISTFILENAME, watchlist_data)
    return response


# Updates the status of a media
def watchlist_update_status(watch_status, media_name, watchlist_name):
    """
	    Updates the watch status of specified a movie or show in a watchlist.

	    Parameters:
	    watch_status (str): The watch status - unwatched, in progress or watched
	    media_name (str): The name of the movie or show to update watch status of.
	    watchlist_name (str): The name of the watchlist to which the movie or show to update watch status of

	    Returns:
	    The response message
	    """
    watch_status = watch_status.strip().lower()
    valid_statuses = ["unwatched", "in progress", "watched"]

    # Checks if valid status input
    if watch_status in valid_statuses:

        # Read the JSON data
        watchlist_data = utils.read_watchlist_file(WATCHLISTFILENAME)

        # Check if the watchlist exists
        watchlist, response = utils.get_watchlist(watchlist_data, watchlist_name)
        if watchlist is None:
            return response
        # Check if media already exists in watchlist
        if media_name in watchlist["media"]:
            media = watchlist["media"].get(media_name)
            media["status"] = watch_status
            response = f"Updated watch status of *{media_name}* to **{watch_status}** in the **{watchlist_name}** watchlist!"
        else:
            response = f"*{media_name}* is not in the **{watchlist_name}** watchlist! \nYou can add it with `/add {media_name}`"

        # Write the updated JSON data
        utils.write_watchlist_file(WATCHLISTFILENAME, watchlist_data)
    else:
        response = "Invalid watch status. Please choose from: unwatched, in progress, watched"
    return response


# Shows media based on tag
def filter_tags(watchlist_name, tags):
    """
	   Display all the media that filtered based on tags in a watchlist.
	   Args:
	       watchlist_name: The name of the watchlist to which the watched movies going to be displayed
	       tags: The tags that want to be based on to filter

	   Returns:
	   The response message

	   """

    # Read the JSON data
    watchlist_data = utils.read_watchlist_file(WATCHLISTFILENAME)

    # Convert input tags to a set
    input_tags_set = set([tag.strip().lower() for tag in tags.split(',')])

    # Check if all tags are valid
    if not input_tags_set.issubset(VALID_TAGS):
        invalid_tags = input_tags_set.difference(VALID_TAGS)
        response = f"The following tags are invalid: {', '.join(invalid_tags)}. Please use valid tags from the following: \n**{', '.join(VALID_TAGS)}**."

        return response

    # Check if the watchlist exists
    watchlist, response = utils.get_watchlist(watchlist_data, watchlist_name)
    if watchlist is None:
        return response
    if not watchlist["media"]:
        response = f"The {watchlist_name} watchlist is empty."
    else:
        matched_media = [media_name for media_name, media_content in watchlist["media"].items() if
                         input_tags_set.issubset(set(
                             media_content["tags"]))]  # using issubet instead of == would provide a narrow down search

        if matched_media:
            media_with_tags = [(name, ', '.join(watchlist["media"][name]["tags"])) for name in matched_media]
            response = f"Here are all of the filtered medias in the {watchlist_name} watchlist based on \"{tags}\" tags:\n"
            response += "\n".join([f"- {name} (Tags: {tags})" for name, tags in media_with_tags])
        else:
            response = "The Media doesn't exist based on provided tags!"
    return response


# Picks a media at random based on tag
def random_tags(watchlist_name, tags):
    """
	   Display a random selected media that filtered based on tags in a watchlist.
	   Args:
	       interaction: The interaction object representing the command invocation.
	       watchlist_name: The name of the watchlist to which the watched movies going to be displayed
	       tags: The tags that want to be based on to filter

	   Returns:
	   None

	   """

    # Read the JSON data
    watchlist_data = utils.read_watchlist_file(WATCHLISTFILENAME)

    # Convert input tags to a set
    input_tags_set = set([tag.strip().lower() for tag in tags.split(',')])

    # Check if all tags are valid
    if not input_tags_set.issubset(VALID_TAGS):
        invalid_tags = input_tags_set.difference(VALID_TAGS)
        response = f"The following tags are invalid: {', '.join(invalid_tags)}. Please use valid tags from the following: \n**{', '.join(VALID_TAGS)}**."
        return response

    # Check if the watchlist exists
    watchlist, response = utils.get_watchlist(watchlist_data, watchlist_name)
    if watchlist is None:
        return response
    if not watchlist["media"]:
        response = f"The {watchlist_name} watchlist is empty."
    else:
        matched_media = [media_name for media_name, media_content in watchlist["media"].items() if
                         input_tags_set.issubset(set(media_content["tags"]))]
        # random select the media from the marched_media set
        if matched_media:
            selected_media = random.choice(matched_media)
            selected_media_tags = ', '.join(watchlist["media"][selected_media]["tags"])

            response = f"Here's a randomly selected media from the {watchlist_name} watchlist based on \"{tags}\" tags:\n- {selected_media} (Tags: {selected_media_tags})"
        else:
            response = "The Media doesn't exist based on provided tags!"
    return response


# Add media description
def add_description(watchlist_name, media_name, description):
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

    # Read the JSON data
    watchlist_data = utils.read_watchlist_file(WATCHLISTFILENAME)

    # Check if the watchlist exists
    watchlist, response = utils.get_watchlist(watchlist_data, watchlist_name)
    if watchlist is None:
        return response
    # Check if media already exists in watchlist
    if media_name in watchlist["media"]:
        media = watchlist["media"].get(media_name)
        media["description"] = description
        response = f"Updated media description to *{media_name}* in the **{watchlist_name}** watchlist"
    else:
        response = f"*{media_name}* is not in the **{watchlist_name}** watchlist"

    # Update JSON file
    utils.write_watchlist_file(WATCHLISTFILENAME, watchlist_data)

    return response


# delete media description
def delete_description(watchlist_name, media_name):
    """
	Delete the description of a particular media

	Parameters:
    interaction (nextcord.Interaction): The interaction object representing the command invocation.
    watchlist_name (str): The name of the watchlist to which the watched movies going to be displayed
    media_name (str): The name of the movie or show to be examined.

    Returns:
    None
	"""

    # Read the JSON data
    watchlist_data = utils.read_watchlist_file(WATCHLISTFILENAME)

    # Check if the watchlist exists
    watchlist, response = utils.get_watchlist(watchlist_data, watchlist_name)
    if watchlist is None:
        return response
    # Check if media already exists in watchlist
    if media_name in watchlist["media"]:
        media = watchlist["media"].get(media_name)
        media["description"] = "none"
        response = f"Cleared media description to *{media_name}* in the **{watchlist_name}** watchlist"
    else:
        response = f"*{media_name}* is not in the **{watchlist_name}** watchlist"

    # Update JSON file
    utils.write_watchlist_file(WATCHLISTFILENAME, watchlist_data)

    return response


# Show media description
def watchlist_description(watchlist_name, media_name):
    """
    View the description of a particular media

    Parameters:
    interaction (nextcord.Interaction): The interaction object representing the command invocation.
    watchlist_name (str): The name of the watchlist to which the watched movies going to be displayed
    media_name (str): The name of the movie or show to be examined.

    Returns:
    None
	"""

    # Read the JSON data
    watchlist_data = utils.read_watchlist_file(WATCHLISTFILENAME)

    # Check if the watchlist exists
    watchlist, response = utils.get_watchlist(watchlist_data, watchlist_name)
    if watchlist is None:
        return response
    # Check if media already exists in watchlist
    if media_name in watchlist["media"]:
        media = watchlist["media"].get(media_name)
        description = media["description"]
        response = f"*{media_name}* : \n{description}"
    else:
        response = f"*{media_name}* is not in the **{watchlist_name}** watchlist"

    return response


def add_review(watchlist_name, media_name, review_text, user_name):
    """
    Lets users add reviews to some media item in a watchlist
    Args:
        watchlist_name: The name of the watchlist in which the media item is in
        media_name: The name of the media item the user wishes to review
        review_text: The review the user wants to leave
        user_name: The username of the user who is making the view (Obtained from interaction object)

    Returns:
        None

    """
    watchlist_data = utils.read_watchlist_file(WATCHLISTFILENAME)
    watchlist, response = utils.get_watchlist(watchlist_data, watchlist_name)

    # Ensure the watchlist exists, if not send the response indicating so
    if watchlist is None:
        return response

    if media_name in watchlist["media"]:
        # If the specified media item is actually in the said watchlist, then just simply append the review to the reviews object
        media = watchlist["media"].get(media_name)
        media["reviews"].append({"user": user_name, "review": review_text})
        response = f"Review has successfully been added to *{media_name}* by **{user_name}**!"
    else:
        response = f"The media *{media_name}* was not found in **{watchlist_name}**!"

    # Write the contents to the JSON file
    utils.write_watchlist_file(WATCHLISTFILENAME, watchlist_data)
    return response

def view_reviews(watchlist_name, media_name):
    """
    Lets users view all the reviews of a specified media item
    Args:
        watchlist_name: The name of the watchlist in which the media they would like to see reviews for is in
        media_name: The name of the media item for which users want to see reviews

    Returns:
        None

    """
    # Initial setup
    watchlist_data = utils.read_watchlist_file(WATCHLISTFILENAME)
    watchlist, response = utils.get_watchlist(watchlist_data, watchlist_name)

    # If the response is None, this means that response is not initialised, so we initialise it with an empty string for now
    if response is None:
        response = ""


    # If watchlist is None (Could not be found) return appropriate response
    if watchlist is None:
        return response

    if media_name in watchlist["media"]:
        media = watchlist["media"].get(media_name)
        # If the media item has no reviews, then we should let the user know with an appropriate response message
        if len(media["reviews"])== 0:
            response = f"**{media_name}** has not been reviewed by anyone yet... Be the first to review via **/add_review**"
        # If the media does have reviews, format the reviews and append to the response object
        for review in media["reviews"]:
            response += f"User **{review['user']}**: \n *{review['review']}*\n\n"

    return response

# Adds rating to media item
def add_rating(rating, media_name, watchlist_name):
    """
	    Adds rating of specified a movie or show in a watchlist.

	    Parameters:
	    rating (str): The rating of the movie or show (0-5)
	    media_name (str): The name of the movie or show to add rating to.
	    watchlist_name (str): The name of the watchlist the movie or show is in.

	    Returns:
	    The response message
	    """
     # Checks if valid rating input
    if not is_rating_valid(rating):
        return "Invalid rating. Please choose a rating between 0 and 5"
    
    # Read the JSON data
    watchlist_data = utils.read_watchlist_file(WATCHLISTFILENAME)

    # Check if the watchlist exists
    watchlist, response = utils.get_watchlist(watchlist_data, watchlist_name)
    if watchlist is None:
        return response
    # Check if media already exists in watchlist
    if media_name in watchlist["media"]:
        media = watchlist["media"].get(media_name)
        new_rating = calc_average_rating(float(rating), media["rating"])
        media["rating"] = new_rating
        response = f"Added rating of **{rating}** to *{media_name}* in the **{watchlist_name}** watchlist!"
    else:
        response = f"*{media_name}* is not in the **{watchlist_name}** watchlist! \nYou can add it with `/add {media_name}`"

    # Write the updated JSON data
    utils.write_watchlist_file(WATCHLISTFILENAME, watchlist_data)
    
    return response


def calc_average_rating(rating, current_rating_info):
    # Keeps rating rounded to be consistent
    rating = round(rating, 1)
    # if not rating has been given previously
    if current_rating_info[0] == -1:
        return [rating, 1]
    else:
        # calculates new average rating
        num_of_ratings = current_rating_info[1] + 1
        new_rating = ((current_rating_info[0] * current_rating_info[1]) + rating) / num_of_ratings
        return [new_rating, num_of_ratings]
    
def is_rating_valid(rating):
    
    try:
        rating = float(rating)
        if 0 <= rating <= 5:
            return True
    except ValueError: 
        pass
    
    return False
    
# View ratings of all media in a watchlist
def view_rating(watchlist_name):
    """
	    View ratings of all media in a watchlist

	    Parameters:
	    watchlist_name (str): The name of the watchlist to show rating info on.

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
        response = f"Here are all of the items and it's rating in the **{watchlist_name}** watchlist!\n"
        for media in watchlist["media"]: 
            media_content = watchlist["media"].get(media)# Print every media item
            rating = media_content["rating"][0]
            num_of_rating = media_content["rating"][1]
            if rating == -1:
                response += f"- {media}: No ratings have been given\n"
            else:
                response += f"- {media}: {rating:.1f} ({num_of_rating})\n"

    return response

# Shows media based on rating (if its equal to or higher it is displayed)
def filter_rating(watchlist_name, rating):
    """
	   Display all the media that filtered based on rating in a watchlist.
	   Args:
	       watchlist_name: The name of the watchlist to which the watched movies going to be displayed
	       tags: The rating that want to be based on to filter

	   Returns:
	   The response message

	   """

    # Read the JSON data
    watchlist_data = utils.read_watchlist_file(WATCHLISTFILENAME)
    

    # Checks if valid rating input
    if not is_rating_valid(rating):
        return "Invalid rating. Please choose a rating between 0 and 5"

    # Check if the watchlist exists
    watchlist, response = utils.get_watchlist(watchlist_data, watchlist_name)
    if watchlist is None:
        return response
    if not watchlist["media"]:
        response = f"The {watchlist_name} watchlist is empty."
    else:
        # Gets all media of at least the given rating.
        matched_media = [media_name for media_name, media_content in watchlist["media"].items() if
                         round(media_content["rating"][0], 1) >= float(rating)]  # using issubet instead of == would provide a narrow down search

        if matched_media:
            response = f"Here are all of the filtered medias in the {watchlist_name} watchlist with a rating of at least **{rating}**:\n"
            response += "\n".join([f"- {name}: {watchlist['media'].get(name)['rating'][0]:.1f} ({watchlist['media'].get(name)['rating'][1]})" for name in matched_media])
        else:
            response = f"There is no media with the rating **{rating}** or above."
    return response