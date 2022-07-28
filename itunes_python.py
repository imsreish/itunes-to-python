import requests
import json
import urllib.request
import urllib.parse
import os
from bs4 import BeautifulSoup

# declare variable for search, convert it an encoded URL string, and
# declare variable to distinguish this search in search history:
# ADD YOUR SEARCH TO THE SEARCH STRING
search_string = "dua lipa"
converted_search = urllib.parse.quote(search_string)
search_result = (f'search_{converted_search}')

# fetch the search from the iTunes API, as a .json file:
json_data = requests.get(f'https://itunes.apple.com/search?term={converted_search}&media=music').json()

# check that a search history folder exists, and make one if it
# does not:
if not os.path.exists('search_history'):
            os.makedirs('search_history')

# now write the json data to a local .json file named as the
# search_result variable:
with open(f'search_history/{search_result}.json', 'w') as json_file:
    json.dump(json_data, json_file)

# declare a variable for the key:value pairs in the json, and
# loop thru them:
    jsonData = json_data["results"]
    for x in jsonData:

        # keys = x.keys()
        # in the loop, declare variables representing values
        # of certain keys:
        artist_name = x["artistName"]
        artist_name_encoded = urllib.parse.quote(artist_name)
        artist_id = x["artistId"]
        tracks = x["trackName"]
        track_id = x["trackId"]
        albums = x["collectionName"]
        albums_encoded = urllib.parse.quote(albums)
        album_art = x["artworkUrl100"]
        collection_id = x["collectionId"]

        print(f'Artist: {artist_name}')
        print(f'Artist ID: {artist_id}')
        print(f'Song: {tracks}')
        print(f'Track ID: {track_id}')
        print(f'Album: {albums}')
        print(f'Collection ID: {collection_id}')

        # check that a search results directory exists, and make
        # one it if does not. additionally, create subdirectories
        # for collections of each search result's album art and
        # artist profile images:
        if not os.path.exists('search_results'):
            os.makedirs('search_results')
            os.makedirs(f'search_results/{search_result}')
            os.makedirs(f'search_results/{search_result}/album_art')
            os.makedirs(f'search_results/{search_result}/artist_profiles')

        # check that in the search result's album art and artist
        # profile images directories that an additional subdirectory
        # for each album exists. this subdirectory is named by a
        # collection_id, as they are unique. add each album art to
        # each collection_id folder and name them after their
        # respective albums variable:
        if not os.path.exists(f'search_results/{search_result}/album_art/{collection_id}'):
            os.makedirs(f'search_results/{search_result}/album_art/{collection_id}')
        urllib.request.urlretrieve(album_art, f'search_results/{search_result}/album_art/{collection_id}/{albums_encoded}.png')

        # declare a variable for the value of the artist's url
        # page as returned by the API. use a GET request on the
        # returned value, which is a URL. when the HTML data is returned,
        # scrape it until an element with the "meta" tag and
        # "og:image" property are found. once this element is found,
        # obtain its URL. this is the URL of the artist profile image:
        artist_url = x["artistViewUrl"]
        r = requests.get(artist_url)
        soup = BeautifulSoup(r.content, 'html.parser')
        image = soup.find("meta", property="og:image")
        image_url = image["content"]
        
        # check within the artist_profiles subdirectory of the search
        # result that a further subdirectory named after the artist exists.
        # if it does not exist, create it, and populate it with the png of
        # the artist image we obtained via BeautifulSoup
        if not os.path.exists(f'search_results/{search_result}/artist_profiles/{artist_id}'):
            os.makedirs(f'search_results/{search_result}/artist_profiles/{artist_id}')
        urllib.request.urlretrieve(image_url, f'search_results/{search_result}/artist_profiles/{artist_id}/{artist_name_encoded}.png')