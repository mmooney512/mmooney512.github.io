# ----------------------------------------------------------------------------
# step 4
# use the html lyric files saved locally and extract the lyrics
# ----------------------------------------------------------------------------

import csv
from bs4 import BeautifulSoup, Comment

test_level = 1000
base_dir = "/home/george/Documents/lyrics/Pink/"
dest_dir = "/home/george/Documents/lyrics/Pink_Lyrics/"
search_phrase = "third-party lyrics provider"

# ----------------------------------------------------------------------------
# step 4.01 
# open the saved .csv file from the local disk
# ----------------------------------------------------------------------------
csv_filename = base_dir + "pink_lyrics.csv"

song_links = {}

with open(csv_filename, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        song_links[row["song_name"]] = row["song_url"]

print(F"rows in file: {len(song_links)}")

counter = 0

# ----------------------------------------------------------------------------
# step 4.02 
# loop through the html files in the dictionary
# ----------------------------------------------------------------------------

for song_name in song_links:
    counter +=1
    if counter >= test_level:
        break
    print(F"Opening item: {counter} - {song_name}")

    with open(base_dir + song_name + '.html') as current_file:    
        read_html_file = current_file.read()
        
        # create the beautiful soup object
        lyric_page = BeautifulSoup(read_html_file, 'html.parser')
        # string to hold the lyric text
        lyric_text = ""
        for comment in lyric_page.findAll(text=lambda text:isinstance(text, Comment)):
            if search_phrase in comment:
                next_el = comment.next_element
                
                # search for the closing div 
                while next_el.name != "div":
                    if next_el.name is None:
                        #append the text to the lyric string
                        lyric_text = lyric_text + next_el.string

                    next_el = next_el.next_element

    # ----------------------------------------------------------------------------
    # step 4.03 
    # write the file to the local file
    # ----------------------------------------------------------------------------
    print(F"Saving file: {counter} - {song_name}.txt")
    with open(dest_dir + song_name + '.txt' ,'w') as text_file:
        text_file.write(lyric_text)
                
 