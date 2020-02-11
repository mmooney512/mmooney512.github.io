import csv
import time
import requests

test_level = 1000
starting_row = 7
ending_row = 7
artist = "Rihanna"
base_dir = "Documents/ranks/" + artist + "/"

base_html = "https://www.billboard.com/music/" + artist.lower() +"/chart-history/HSI"
# ----------------------------------------------------------------------------
# step one 
# go out to website, grab html page with rankings, save locally
# ----------------------------------------------------------------------------

counter = starting_row
# check where we are in getting items from the dictionary
while counter >= starting_row and counter <= ending_row:
    # get the ranking page
    if counter > 1:
        get_page = base_html +"/" + str(counter)
    else:
        get_page = base_html
    print(F"Fetching: {get_page}")

    # get the html page
    ranking_page = requests.get(get_page)
    # show the status of the page
    print(F"Page: {counter}  Status: {ranking_page.status_code}")

    with open(base_dir + artist + '_' + str(counter) + '.html' ,'w') as html_file:
        html_file.write(ranking_page.text)
    
    # wait so we don't overload remote site
    if counter <= ending_row:
        time.sleep(3)
    
    counter +=1
