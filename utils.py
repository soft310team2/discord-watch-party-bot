import json
import os

# ---------------------------------------------------------------------------
# A bunch of utility helper methods
#   get_watchlist - Gets a specific watchlist given a name and returns it if it exists
#   read_watchlist_file - Reads all the data from a watchlist if it exists and returns the data
#   write_watchlist_file - Writes contents to a specified watchlist
#   init_watchlistJSON - Creates a new watchlist.json file if it does not exist when the bot starts
# ---------------------------------------------------------------------------
def get_watchlist(watchlist_data, watchlist_name):
    for watchlist in watchlist_data["watchlists"]:
        if watchlist["name"] == watchlist_name:
           return watchlist, None
    return None, f"The **{watchlist_name}** watchlist does not exist! \nYou can create it with `/create {watchlist_name}`"

def read_watchlist_file(watchlist_file_name):
    watchlist_file = open(watchlist_file_name, 'r')
    watchlist_data = json.load(watchlist_file)
    watchlist_file.close()
    return watchlist_data

def write_watchlist_file(watchlist_file_name, watchlist_data):
    watchlist_file = open(watchlist_file_name, 'w')
    watchlist_file.write(json.dumps(watchlist_data))
    watchlist_file.close()

def init_watchlist_json(watchlist_file_name):
    if not os.path.exists(watchlist_file_name):
        with open(watchlist_file_name, 'w') as file:
            json.dump({"watchlists": []}, file)