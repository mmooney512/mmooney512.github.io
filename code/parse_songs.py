# ----------------------------------------------------------------------------
# step 2 
# from the songs html file, parse the song titles and URLs to the lyrics
# ----------------------------------------------------------------------------

import csv
from bs4 import BeautifulSoup


artist = "Taylor-Swift"
searchword = "taylorswift"

base_dir = "/home/george/Documents/webscrap/lyrics/" + artist + "_html/"
song_list = base_dir + artist +"_songs.html" 

# ----------------------------------------------------------------------------
# step 2.01 
# open the saved html file from the local disk
# ----------------------------------------------------------------------------

with open(song_list) as song_html_file:
    read_data = song_html_file.read()


# ----------------------------------------------------------------------------
# step 2.02 
# parse the file using BeautifulSoup
# ----------------------------------------------------------------------------

# create the beautiful soup object
song_page = BeautifulSoup(read_data, 'html.parser')

# find all of the URLS in the webpage
links = song_page.find_all("a")

# root page of lyrics
root = "https://www.azlyrics.com"

# dictionary of song links
song_links ={}

for link in links:
    # check if the word pink and lyrcis is in the URL
    if searchword in link.get("href") and 'lyrics' in link.get("href"):
        # extract the URL
        song_link = link.get('href')
        # replace the relative URL with an absolute URL
        # store in the dictionary
        song_links[link.text] = root + song_link.replace(".." , "")

# prints out the URLS
for link_text in song_links:
    song_link = song_links[link_text]
    print (song_link)


# ----------------------------------------------------------------------------
# step 2.03 
# save the URLS to a local file
# use CSV
# ----------------------------------------------------------------------------
file_name = base_dir + artist + "_lyrics.csv"
with open(file_name,mode='w') as csv_file:
    field_names = ['song_name' ,'song_url']
    writer = csv.DictWriter(csv_file, fieldnames=field_names)
    # write header row in the csv file
    writer.writeheader()
    # write the output
    for link_text in song_links:
        writer.writerow({'song_name': link_text, 'song_url':song_links[link_text]})


# end