# itunes-to-python
A script to grab artist images from an artist's apple music page after searching the itunes API (the itunes API doesn't expose this data). Images are automatically fetched and stored locally.

## How it works:

#### A variable for search is declared, converted to an encoded URL string, and the search is submitted to the iTunes API. The result comes back as a .json file.

#### A check is made that a search_history folder exists, and one is made if it does not.

#### Then the returned json data is written to a local .json file named as the search_result variable.

#### A variable for the key:value pairs in the json is declared and looped thru.

#### In the loop, variables  representing values of certain JSON keys are declared. This is to help with identifying what's happening in the terminal output.

#### Another check is made that a search_results directory exists, and one is made it if does not. Additionally, subdirectories for collections of each search result's album art and artist profile images are created.

#### Another check is performed in the search result's album art and artist profile images directories that an additional subdirectory for each album exists. These subdirectories are named by a collection_id, as they are unique. Each album art is added to each collection_id folder named after their respective albums variable.

#### A variable for the value of the artist's url page as returned by the API is declared. A new GET request is performed on the returned value, which is a URL. When the HTML data is returned, it is scraped until an element with the "meta" tag and "og:image" property are found. Once this element is found,  its URL is obtained. This is the URL of the artist profile image.

#### A final check is performed -- within the artist_profiles subdirectory of the search result that a further subdirectory named after the artist exists. If it does not exist, it is created, and populated with the png of the artist image we obtained via BeautifulSoup.
