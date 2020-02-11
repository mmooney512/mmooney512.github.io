# ----------------------------------------------------------------------------
# step 1 
# get the list of songs made by the artist
# ----------------------------------------------------------------------------

import requests

test_level = 1000

artist = "Rihanna"
get_page = "https://www.azlyrics.com/r/rihanna.html"

base_dir = "Documents/webscrap/lyrics/" + artist +"_html/"
html_filename = base_dir + artist + "_songs.html"


# ----------------------------------------------------------------------------
# step 1.01 
# go out to website, grab html page with song titles and save locally
# ----------------------------------------------------------------------------

# get the html page
song_page = requests.get(get_page)
# show the status of the page
print(F"Page: {get_page}  Status: {song_page.status_code}")

with open(html_filename ,'w') as html_file:
    html_file.write(song_page.text)

print(F"saved: {html_filename}")