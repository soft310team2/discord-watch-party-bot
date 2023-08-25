import json
def get_watchlist(watchlist_data, watchlist_name):
     for watchlist in watchlist_data["watchlists"]:
        if watchlist["name"] == watchlist_name:
           return watchlist
     return None

def read_watchlist_file(watchlist_file_name):
    watchlist_file = open(watchlist_file_name, 'r')
    watchlist_data = json.load(watchlist_file)
    watchlist_file.close()
    return watchlist_data

def write_watchlist_file(watchlist_file_name, watchlist_data):
    watchlist_file = open(watchlist_file_name, 'w')
    watchlist_file.write(json.dumps(watchlist_data))
    watchlist_file.close()