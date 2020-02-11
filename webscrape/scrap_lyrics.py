# ----------------------------------------------------------------------------
# step 3
# use the list of song titles and URLs and save html locally
# ----------------------------------------------------------------------------
import random
import csv
import time
import requests

test_level = 1000
starting_row = 204
ending_row = 400

artist = "Drake"
base_dir = "/home/george/Documents/webscrap/lyrics/" + artist + "_html/"

# ----------------------------------------------------------------------------
# step 3.01 
# open the saved .csv file from the local disk
# ----------------------------------------------------------------------------
csv_filename = base_dir + artist + "_lyrics.csv"

song_links = {}

with open(csv_filename, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        song_links[row["song_name"]] = row["song_url"]

print(F"rows in file: {len(song_links)}")


# ----------------------------------------------------------------------------
# step 3.02 
# go out to website, grab html page with lyrics, save locally
# ----------------------------------------------------------------------------

counter = 0

# loop through the song urls in the dictionary
for song_name in song_links:
    
    # check where we are in getting items from the dictionary
    if counter >= starting_row and counter <= ending_row:
        # get the html page
        lyric_page = requests.get(song_links[song_name])
    
        # if the page is successfully retrieved then save it
        if lyric_page.status_code == 200:
            with open(base_dir + song_name + '.html' ,'w') as html_file:
                html_file.write(lyric_page.text)
            print(F"Retreived item: {counter} - {song_name}")
        else:
            print(F"ERROR getting: {counter} - {song_links[song_name]}")

        # wait so we don't overload remote site
        time.sleep(random.randint(2,5))

    counter +=1

# end of file
