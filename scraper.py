##############################################################
# Program name: ICA Conference Site Scraper (Page Scraper)
# Version: 0.1-alpha
# By: Rodrigo Zamith
# License: MPL 2.0 (see LICENSE file in root folder)
# Additional thanks: 
##############################################################

import os
import re
import csv
from bs4 import BeautifulSoup

# Variables that need setting
output_file = "data.csv" # Label your data file


##### THE SCRIPT WILL TAKE IT FROM HERE #####
output_file = open(output_file, "wb")
output_file_wr = csv.writer(output_file, quoting=csv.QUOTE_ALL)

header = ["case_id", "case_title", "case_authors", "case_session", "case_unit", "case_type", "case_area", "case_time", "case_place"]
output_file_wr.writerow(header)

for page in os.listdir('pages/'):
    if page[-4:] == "html":
        filename = "pages/" + page
        print "Parsing file: " + filename
        
        fopen = open(filename, 'r')
        page = fopen.read()
        fopen.close
        
        page_soup = BeautifulSoup(page) # Soupify it for parsing
        for main_row in page_soup.find_all("tr", re.compile("worksheet_window__row__light|worksheet_window__row__dark")):
            for item_table in main_row.find_all("td", title="##"):
                try:
                    case_id = item_table.find("font", "headingtext").get_text().encode('latin-1', 'ignore')
                except AttributeError:
                    case_id = "None"
            for item_table in main_row.find_all("td", title="Summary"):
                try:
                    case_title = item_table.find("a", "search_headingtext").get_text().encode('latin-1', 'ignore')
                except AttributeError:
                    case_title = "None"
                case_authors = []
                for author in item_table.find_all("a", "search_fieldtext_name"):
                    case_authors.append(author.get_text().encode('latin-1', 'ignore'))
                try:
                    case_session = item_table.find(text=re.compile("In Session Submission:")).find_next().get_text().encode('latin-1', 'ignore')
                except AttributeError:
                    case_session = "None"
                try:
                    case_unit = item_table.find(text=re.compile("Unit:")).find_next().get_text().encode('latin-1', 'ignore')
                except AttributeError:
                    case_unit = "None"
                try:
                    case_type = item_table.find(text=re.compile("Individual Submission type:")).find_next().get_text().encode('latin-1', 'ignore')
                except AttributeError:
                    case_type = "None"
                try:
                    case_area = item_table.find(text=re.compile("Research Area[a-z]?:")).find_next().get_text().encode('latin-1', 'ignore')
                except AttributeError:
                    case_area = "None"
                try:
                    case_time = item_table.find(text=re.compile("Time:")).find_next().get_text().encode('latin-1', 'ignore')
                except AttributeError:
                    case_time = "None"
                try:
                    case_place = item_table.find(text=re.compile("Place:")).find_next().get_text().encode('latin-1', 'ignore')
                except AttributeError:
                    case_place = "None"
                
                line = [case_id, case_title, case_authors, case_session, case_unit, case_type, case_area, case_time, case_place]
                output_file_wr.writerow(line)
    
print "Finished!"
