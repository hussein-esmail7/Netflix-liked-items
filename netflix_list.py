"""
netflix_list.py
Hussein Esmail
Created: 2021 04 _
Updated: 2021 04 18
Description: This program inputs the HTML file of a Netlix liked list on desktop, and outputs the names of each liked item as a simple list. This program exists so that when you want a list of all your Netflix items, you don't have to write them all out in a text document or on paper.
"""

from bs4 import BeautifulSoup   # To view the list items in the HTML file
import sys                      # To input the HTML file 

# sys.argv[1] = File name to search
if len(sys.argv) < 2: # If the HTML file location was not inputted
    html_file_location = input("HTML file location: ")
else: 
    html_file_location = sys.argv[1]

with open(html_file_location) as fp:
    soup = BeautifulSoup(fp, "html.parser")
    items = soup.find_all("a")
    # print(f"{len(items)-7} items.") 
    for item in items[3:-4]:
        """
        Reason for 3:-4 :
        Entry 0: "Netflix"
        Entry 0: "Gifts"
        Entry 0: "{USER} - Account & Settings"
        ... Movies list ...
        Entry -4: "facebook"
        Entry -3: "instagram"
        Entry -2: "twitter"
        Entry -1: "youtube"
        """
        try: 
            print(item["aria-label"]) # Print the item name
        except:
            pass
